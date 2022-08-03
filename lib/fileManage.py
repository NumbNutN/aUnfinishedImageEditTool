from lib.share import SI
import cv2
import numpy as np
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from ui.ui_MainWindow import Ui_MainWindow

import cv2
from lib.share import SI
from lib.resize import Resize
from ui.ui_HistoryFile import Ui_historyFile
from lib.transparent import Transparent
from lib.processingQueue import ProcessingQueue
from lib.edgeDetection import EdgeDetection

class FIleMenu(QWidget,Ui_historyFile):
    '''
    这个类负责管理文件选项卡,功能包括
        1. def __init__(self): 为主窗口的文件选项卡设置触发事件，同时加载历史打开文件窗口
        2. def readFile(self,filePath): 打开一个图片的封装函数，用于替代cv2.imread()来解决路径不能包含中文的问题
        3. def OpenFile(self,openType,filePath = None,img = None): 实现该工具的三种文件打开方式，把图片装载在历史图片队列里并显示在

    '''

    OPENFILEFROMCUSTOMIZEPATH = 100    #调出资源管理器的路径选择供用户挑选
    OPENFILEFROMEXISTPATH = 101        #从系统记录的已有路径调取
    OPENFILEFROMMEMORY = 102           #从内存中存在的图片调取

    def __init__(self):
        SI.mainWindow.fileOpenAction.triggered.connect(lambda: self.OpenFile(self.OPENFILEFROMCUSTOMIZEPATH))
        SI.mainWindow.saveAsAction.triggered.connect(self.SaveFile)
        SI.mainWindow.cleanHistoryAction.triggered.connect(self.WrapOutHistory)
        SI.historyFilePath = []

        #读取历史图片路径
        #txt中记录的图片地址从上到下为从新到旧
        with open ("./historyFile.txt",'r') as file:
            for path in file:
                SI.historyFilePath.append(path.strip())

        #print(SI.historyFilePath)

        #加载最近打开图片窗口
        super().__init__()
        self.setupUi(self)
        # qfile_historyFile_stats = QFile("./HistoryFile.ui")
        # qfile_historyFile_stats.open(QFile.ReadOnly)
        # qfile_historyFile_stats.close()
        # SI.historyPathViewUi = QUiLoader().load(qfile_historyFile_stats)
        SI.mainWindow.recentFileAction.triggered.connect(self.ViewRecentFile)
        self.listHistoryFile.itemClicked.connect(self.RecentFileShowCurrentItem)
        self.btnVerifyHistoryFile.clicked.connect(self.SelectAnHistoryFile)

    #兼容中文的读取方案
    def readFile(self,filePath):
        if filePath:
            raw_data = np.fromfile(filePath,dtype=np.uint8)
            img = cv2.imdecode(raw_data,cv2.IMREAD_UNCHANGED)
            return img
        else:
            return None


    def OpenFile(self,openType,filePath = None,img = None):
        if (openType == self.OPENFILEFROMCUSTOMIZEPATH):
            filePath,fileType = QFileDialog.getOpenFileName(
                SI.mainWindow,
                "选择图片路径",
                r"d:",
                "(*.png *.jpg *.bmp)"
            )
            SI.cvImg = self.readFile(filePath)
            print("Open a file from customaize path")

        elif (openType == self.OPENFILEFROMEXISTPATH):
            SI.cvImg = self.readFile(filePath)
            print("Open a file from existing path")

        elif (openType == self.OPENFILEFROMMEMORY):
            SI.cvImg = img
            print("Open a file from memory")

        if SI.cvImg is not None:
            SI.processingImgQueue.insert(0,SI.cvImg)
            SI.processingImgQueue.insert(0, SI.cvImg)
            SI.ShowBGRPic(SI.processingImgQueue[0],SI.mainWindow.labelImgViewpot)
            SI.oriW = SI.curW = SI.cvImg.shape[1]
            SI.oriH = SI.curH = SI.cvImg.shape[0]
            SI.resize = Resize()
            Resize.showImgInfoRefresh(Resize)

            #历史记录最多存储10条，超过10条以队列的形式从队尾顶出
            if len(SI.historyFilePath) >= 10:
                SI.historyFilePath.pop()
            SI.historyFilePath.insert(0,filePath)

            #每次更新状态后重新写最近打开历史记录文件
            with open ("./historyFile.txt",'w') as file:
                    for path in SI.historyFilePath:
                        if path is not None:
                            file.write(path+'\n')
            print(SI.historyFilePath)


        # 直接将磁盘文件加载为QPixmap格式的方法
        # img = QPixmap(filePath)
        # self.ui.labelImgViewpot.setPixmap(img)

        # #适当调整图片大小的逻辑
        # if(SI.cvImg.shape[1]>1280 or SI.cvImg.shape[0]>720):
        #     SI.mainWindow.labelImgViewpot.setMaximumSize(1280,int(1280/SI.curW*SI.curH))


    def SaveFile(self):
        filePath = QFileDialog.getExistingDirectory(SI.mainWindow,"选择保存的路径")
        print(filePath+"/TempName.jpg")

        cv2.imwrite(filePath+"/TempName.jpg",SI.processingImgQueue[0])

    def WrapOutHistory(self):
        SI.historyFilePath = []
        with open("./historyFile.txt",'w') as file:
            file.write('')

    def RenewListFileHistory(self):
        self.listHistoryFile.clear()
        for path in SI.historyFilePath:
            self.listHistoryFile.addItem(path)

    def ViewRecentFile(self):
        self.RenewListFileHistory()
        self.show()

    def RecentFileShowCurrentItem(self):
        path = self.listHistoryFile.currentItem().text()
        imgCvPreview = self.readFile(path)
        SI.ShowBGRPic(imgCvPreview,self.labelHistoryPreview)

        # try:
        #     channelsNum = imgCvPreview.shape[2]
        # except IndexError:
        #     channelsNum = 2
        #     imgType = "?"
        # else:
        #     imgType = "RGB888"
        channelsNum = SI.returnChannelNum(imgCvPreview)
        imgType = SI.returnImgType(imgCvPreview)

        self.labelPreviewInfo.setText(
            "size: "+str(imgCvPreview.shape[1])+'x'+str(imgCvPreview.shape[0])+'\t'+
            "channels: "+str(channelsNum)+'\t'+"type: "+imgType)

    def SelectAnHistoryFile(self):
        path = self.listHistoryFile.currentItem().text()
        self.OpenFile(self.OPENFILEFROMEXISTPATH,filePath=path)
        self.hide()


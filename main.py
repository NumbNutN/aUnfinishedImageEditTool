import numpy as np
from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from PySide2.QtGui import QPixmap ,QImage
import cv2
from lib.share import SI
from lib.resize import Resize
from lib.transparent import Transparent
from lib.processingQueue import ProcessingQueue
from lib.edgeDetection import EdgeDetection



class FIleMenu:
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
        SI.ui.fileOpenAction.triggered.connect(lambda: self.OpenFile(self.OPENFILEFROMCUSTOMIZEPATH))
        SI.ui.saveAsAction.triggered.connect(self.SaveFile)
        SI.ui.cleanHistoryAction.triggered.connect(self.WrapOutHistory)
        SI.historyFilePath = []

        #读取历史图片路径
        #txt中记录的图片地址从上到下为从新到旧
        with open ("./historyFile.txt",'r') as file:
            for path in file:
                SI.historyFilePath.append(path.strip())

        #print(SI.historyFilePath)

        #加载最近打开图片窗口
        qfile_historyFile_stats = QFile("./HistoryFile.ui")
        qfile_historyFile_stats.open(QFile.ReadOnly)
        qfile_historyFile_stats.close()
        SI.historyPathViewUi = QUiLoader().load(qfile_historyFile_stats)
        SI.ui.recentFileAction.triggered.connect(self.ViewRecentFile)
        SI.historyPathViewUi.listHistoryFile.itemClicked.connect(self.RecentFileShowCurrentItem)
        SI.historyPathViewUi.btnVerifyHistoryFile.clicked.connect(self.SelectAnHistoryFile)

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
                SI.ui,
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
            SI.ShowBGRPic(SI.processingImgQueue[0],SI.ui.labelImgViewpot)
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
        #     SI.ui.labelImgViewpot.setMaximumSize(1280,int(1280/SI.curW*SI.curH))


    def SaveFile(self):
        filePath = QFileDialog.getExistingDirectory(SI.ui,"选择保存的路径")
        print(filePath+"/TempName.jpg")

        cv2.imwrite(filePath+"/TempName.jpg",SI.processingImgQueue[0])

    def WrapOutHistory(self):
        SI.historyFilePath = []
        with open("./historyFile.txt",'w') as file:
            file.write('')

    def RenewListFileHistory(self):
        SI.historyPathViewUi.listHistoryFile.clear()
        for path in SI.historyFilePath:
            SI.historyPathViewUi.listHistoryFile.addItem(path)

    def ViewRecentFile(self):
        self.RenewListFileHistory()
        SI.historyPathViewUi.show()

    def RecentFileShowCurrentItem(self):
        path = SI.historyPathViewUi.listHistoryFile.currentItem().text()
        imgCvPreview = self.readFile(path)
        SI.ShowBGRPic(imgCvPreview,SI.historyPathViewUi.labelHistoryPreview)

        # try:
        #     channelsNum = imgCvPreview.shape[2]
        # except IndexError:
        #     channelsNum = 2
        #     imgType = "?"
        # else:
        #     imgType = "RGB888"
        channelsNum = SI.returnChannelNum(imgCvPreview)
        imgType = SI.returnImgType(SI,imgCvPreview)

        SI.historyPathViewUi.labelPreviewInfo.setText(
            "size: "+str(imgCvPreview.shape[1])+'x'+str(imgCvPreview.shape[0])+'\t'+
            "channels: "+str(channelsNum)+'\t'+"type: "+imgType)

    def SelectAnHistoryFile(self):
        path = SI.historyPathViewUi.listHistoryFile.currentItem().text()
        self.OpenFile(self.OPENFILEFROMEXISTPATH,filePath=path)
        SI.historyPathViewUi.hide()




class TabWidget:
    def __init__(self):
        SI.ui.tabWidgetFunction.currentChanged.connect(self.TabChange)

    def TabChange(self):
        print(SI.ui.tabWidgetFunction.currentIndex())
        if not(np.array_equal(SI.processingImgQueue[0],SI.processingImgQueue[1])):
            SI.processingImgQueue.insert(0,SI.processingImgQueue[0])
        print("Image Edit Stack: "+str(len(SI.processingImgQueue)))
        SI.ShowBGRPic(SI.processingImgQueue[0],SI.ui.labelImgViewpot)
        SI.advancedinfo.InfoRefresh()


class GrayScale:
    def __init__(self):
        SI.ui.cboxCvtToGrayScale.stateChanged.connect(self.TranToGrayScal)

    def TranToGrayScal(self):
        if (SI.ui.cboxCvtToGrayScale.isChecked()):
            SI.processingImgQueue[0] = cv2.cvtColor(SI.processingImgQueue[1],cv2.COLOR_BGR2GRAY)
            SI.ShowGrayPic(SI.processingImgQueue[0],SI.ui.labelImgViewpot)
            print("ConvertToGrayScale")
        else:
            SI.processingImgQueue[0] = SI.processingImgQueue[1]
            SI.ShowBGRPic(SI.processingImgQueue[0], SI.ui.labelImgViewpot)
            print("ReturnToColor")
        SI.PrintSimpleImgInfo(SI.processingImgQueue[0], SI.ui.labelShowImgInfo)


class AdvancedInfo:
    def __init__(self):
        pass

    def InfoRefresh(self):
        SI.ui.textBrowser.setText(
        "当前图像属性：\n"\
        "图片尺寸: %dx%d\t"\
        "通道数: %d\n"\
        "图片类型: %s\t"\
        "位深度: %d\n"\
        "----------------------\n"\
        "状态：\n"\
        "图片处理历史队列数: %d\n"
             % (SI.curW, SI.curH,SI.imgChannel,SI.returnImgType(SI,SI.processingImgQueue[0]),SI.returnColorDepth(SI,SI.processingImgQueue[0]),len(SI.processingImgQueue)))

app = QApplication([])

qfile_stats = QFile("main.ui")
qfile_stats.open(QFile.ReadOnly)
qfile_stats.close()
SI.ui = QUiLoader().load(qfile_stats)
SI.InitImg(SI)
SI.ShowBGRPic(SI.processingImgQueue[0],SI.ui.labelImgViewpot)


SI.fileMenu = FIleMenu()
SI.resize = Resize()
SI.tabwidget = TabWidget()
SI.advancedinfo = AdvancedInfo()
SI.grayscale = GrayScale()
SI.edgedetection = EdgeDetection()
SI.transparent = Transparent()
SI.processingqueue = ProcessingQueue()

SI.ui.show()
app.exec_()
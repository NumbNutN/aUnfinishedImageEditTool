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

class FIleMenu:

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

        print(SI.historyFilePath)

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
        raw_data = np.fromfile(filePath,dtype=np.uint8)
        img = cv2.imdecode(raw_data,cv2.IMREAD_COLOR)
        return img

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

        SI.showCvImg.insert(0,SI.cvImg)
        SI.showCvImg.insert(0, SI.cvImg)
        SI.ShowPic(SI.showCvImg[0],SI.ui.labelShowImg)
        SI.oriCvW = SI.showCvW = SI.cvImg.shape[1]
        SI.oriCvH = SI.showCvH = SI.cvImg.shape[0]
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
        # self.ui.labelShowImg.setPixmap(img)

        # #适当调整图片大小的逻辑
        # if(SI.cvImg.shape[1]>1280 or SI.cvImg.shape[0]>720):
        #     SI.ui.labelShowImg.setMaximumSize(1280,int(1280/SI.showCvW*SI.showCvH))


    def SaveFile(self):
        filePath = QFileDialog.getExistingDirectory(SI.ui,"选择保存的路径")
        print(filePath+"/TempName.jpg")

        cv2.imwrite(filePath+"/TempName.jpg",SI.showCvImg[0])

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
        SI.ShowPic(imgCvPreview,SI.historyPathViewUi.labelHistoryPreview)

        try:
            channelsNum = imgCvPreview.shape[2]
        except IndexError:
            channelsNum = 2
            imgType = "?"
        else:
            imgType = "RGB888"

        SI.historyPathViewUi.labelPreviewInfo.setText(
            "size: "+str(imgCvPreview.shape[1])+'x'+str(imgCvPreview.shape[0])+'\t'+
            "channels: "+str(channelsNum)+'\t'+"type: "+imgType)

    def SelectAnHistoryFile(self):
        path = SI.historyPathViewUi.listHistoryFile.currentItem().text()
        self.OpenFile(self.OPENFILEFROMEXISTPATH,filePath=path)
        SI.historyPathViewUi.hide()




class EdgeDetection:

    tempSobelImg = None
    tempFlipImg = None

    def __init__(self):
        SI.ui.cBoxCvtMargin.stateChanged.connect(self.FindEdge)
        SI.ui.bGroupMarginBackground.buttonClicked.connect(self.PositiveAndNegativeChange)
        #默认正面
        SI.ui.radioButtonPositive.setChecked(True)

        # 设置宽度滑块最大/小值
        SI.ui.sliderMarginAdjustStrength.setMinimum(0)
        SI.ui.sliderMarginAdjustStrength.setMaximum(255)

        # 设置步长
        SI.ui.sliderMarginAdjustStrength.setSingleStep(1)

        # 设置当前值
        SI.ui.sliderMarginAdjustStrength.setValue(127)
        SI.ui.labelEdgeStrength.setText(str(SI.ui.sliderMarginAdjustStrength.value()))

        # 设置刻度的位置，刻度在下方
        SI.ui.sliderMarginAdjustStrength.setTickPosition(QSlider.TicksBelow)

        # 设置刻度的间隔
        SI.ui.sliderMarginAdjustStrength.setTickInterval(int(1 / 5 * 255))

        # 设置控件的信号处理函数
        SI.ui.sliderMarginAdjustStrength.valueChanged.connect(self.AdjustStrength)


    def FindEdge(self):
        if (SI.ui.cBoxCvtMargin.isChecked()):
            grayImg = cv2.cvtColor(SI.showCvImg[0],cv2.COLOR_BGR2GRAY)
            sobelx = cv2.Sobel(grayImg, -1, 1, 0, ksize=3)
            sobely = cv2.Sobel(grayImg, -1, 0, 1, ksize=3)
            self.tempSobelImg = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
            self.tempFlipImg = self.FlipImg(self.tempSobelImg)
            self.PositiveAndNegativeChange()
            #SI.showCvImg[0] = self.tempSobelImg
            #SI.ShowGrayPic(SI.showCvImg[0], SI.ui.labelShowImg)
        else:
            SI.showCvImg[0] = SI.showCvImg[1]
            SI.ShowPic(SI.showCvImg[0], SI.ui.labelShowImg)
        SI.PrintSimpleImgInfo(SI.showCvImg[0], SI.ui.labelShowImgInfo)

        print(SI.showCvImg[0].shape)

        # cv2.imshow("window", SI.showCvImg[0])
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # SI.ShowGrayPic(SI.showCvImg[0], SI.ui.labelShowImg)

    def AdjustStrength(self):
        if (SI.ui.radioButtonNagetive.isChecked()):
            #SI.showCvImg[0] = cv2.inRange(self.tempFlipImg,255 - SI.ui.sliderMarginAdjustStrength.value(),256)
            SI.showCvImg[0] = cv2.inRange(self.tempSobelImg,0, SI.ui.sliderMarginAdjustStrength.value())

        else:
            SI.showCvImg[0] = cv2.inRange(self.tempSobelImg, 255 - SI.ui.sliderMarginAdjustStrength.value(), 255)

        SI.ShowPic(SI.showCvImg[0], SI.ui.labelShowImg)
        SI.ui.labelEdgeStrength.setText(str(SI.ui.sliderMarginAdjustStrength.value()))

    def FlipImg(self,img):
        newImg = np.copy(img)
        i = 0
        j = 0
        while i < newImg.shape[0]:
            while j < newImg.shape[1]:
                newImg[i][j] = 255 - img[i][j]
                j += 1
            j = 0
            i += 1
        return newImg

    def PositiveAndNegativeChange(self):
        if(SI.ui.cBoxCvtMargin.isChecked()):

            if(SI.ui.radioButtonPositive.isChecked()):
                SI.showCvImg[0] = self.tempSobelImg
                print("positive")
            else:
                SI.showCvImg[0] = self.tempFlipImg
                SI.print_img_txt(SI.showCvImg[0])
                print("negative")
            SI.ShowGrayPic(SI.showCvImg[0], SI.ui.labelShowImg)





class TabWidget:
    def __init__(self):
        SI.ui.tabWidgetFunction.currentChanged.connect(self.TabChange)

    def TabChange(self):
        print(SI.ui.tabWidgetFunction.currentIndex())
        if not(np.array_equal(SI.showCvImg[0],SI.showCvImg[1])):
            SI.showCvImg.insert(0,SI.showCvImg[0])
        print("Image Edit Stack: "+str(len(SI.showCvImg)))
        SI.ShowPic(SI.showCvImg[0],SI.ui.labelShowImg)
        SI.advancedinfo.InfoRefresh()


class GrayScale:
    def __init__(self):
        SI.ui.cboxCvtToGrayScale.stateChanged.connect(self.TranToGrayScal)

    def TranToGrayScal(self):
        if (SI.ui.cboxCvtToGrayScale.isChecked()):
            SI.showCvImg[0] = cv2.cvtColor(SI.showCvImg[1],cv2.COLOR_BGR2GRAY)
            SI.ShowGrayPic(SI.showCvImg[0],SI.ui.labelShowImg)
            print("ConvertToGrayScale")
        else:
            SI.showCvImg[0] = SI.showCvImg[1]
            SI.ShowPic(SI.showCvImg[0], SI.ui.labelShowImg)
            print("ReturnToColor")
        SI.PrintSimpleImgInfo(SI.showCvImg[0], SI.ui.labelShowImgInfo)


class AdvancedInfo:
    def __init__(self):
        pass

    def InfoRefresh(self):
        SI.ui.labelQueueNum.setText("图片处理历史队列数： "+str(len(SI.showCvImg)))

app = QApplication([])

qfile_stats = QFile("ImgMargin.ui")
qfile_stats.open(QFile.ReadOnly)
qfile_stats.close()
SI.ui = QUiLoader().load(qfile_stats)
SI.InitImg(SI)
SI.ShowPic(SI.showCvImg[0],SI.ui.labelShowImg)


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
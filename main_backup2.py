import numpy as np
from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from PySide2.QtGui import QPixmap ,QImage
import cv2
from lib.share import SI
from lib.resize import Resize

class FIleMenu:
    def __init__(self):
        SI.ui.fileOpenAction.triggered.connect(self.OpenFile)
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
        SI.historyPathViewUi.btnVerifyHistoryFile.clicked.connect(self.VerifyHistoryFile)



    #兼容中文的读取方案
    def readFile(self,filePath):
        raw_data = np.fromfile(filePath,dtype=np.uint8)
        img = cv2.imdecode(raw_data,cv2.IMREAD_COLOR)
        return img

    def OpenFile(self):
        filePath,fileType = QFileDialog.getOpenFileName(
            SI.ui,
            "选择图片路径",
            r"d:",
            "(*.png *.jpg *.bmp)"
        )

        SI.cvImg = self.readFile(filePath)
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
        cv2.imwrite("TempName.jpg",SI.showCvImg[0])

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

    def VerifyHistoryFile(self):
        SI.historyPathViewUi.hide()




class EdgeDetection:

    tempSobelImg = None
    tempFlipImg = None
    temp2 = None
    def __init__(self):
        SI.ui.cBoxCvtMargin.stateChanged.connect(self.FindEdge)
        SI.ui.bGroupMarginBackground.buttonClicked.connect(self.PositiveAndNegativeChange)
        #默认正面
        #SI.ui.radioButtonPositive.setDown(True)

        # 设置宽度滑块最大/小值
        SI.ui.sliderMarginAdjustStrength.setMinimum(0)
        SI.ui.sliderMarginAdjustStrength.setMaximum(255)

        # 设置步长
        SI.ui.sliderMarginAdjustStrength.setSingleStep(1)

        # 设置当前值
        SI.ui.sliderMarginAdjustStrength.setValue(255)

        # 设置刻度的位置，刻度在下方
        SI.ui.sliderMarginAdjustStrength.setTickPosition(QSlider.TicksBelow)

        # 设置刻度的间隔
        SI.ui.sliderMarginAdjustStrength.setTickInterval(int(1 / 5 * 255))

        # 设置控件的信号处理函数
        SI.ui.sliderMarginAdjustStrength.valueChanged.connect(self.AdjustStrength)


    def FindEdge(self):
        if (SI.ui.cBoxCvtMargin.isChecked()):
            sobelx = cv2.Sobel(SI.showCvImg[0], -1, 1, 0, ksize=3)
            sobely = cv2.Sobel(SI.showCvImg[0], -1, 0, 1, ksize=3)
            self.tempSobelImg = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
            cv2.imshow("window", self.tempSobelImg)
            cv2.waitKey(0)
            SI.showCvImg[0] = self.tempSobelImg
            self.temp2 = self.tempSobelImg
            print(np.array_equal(self.tempSobelImg,self.temp2))
            cv2.imshow("window", self.tempSobelImg)
            cv2.waitKey(0)
            self.tempFlipImg = self.FlipImg(self.tempSobelImg)
            cv2.imshow("window", self.tempSobelImg)
            cv2.waitKey(0)
            print(np.array_equal(self.tempSobelImg,self.tempFlipImg))
            cv2.imshow("window", self.tempSobelImg)
            cv2.waitKey(0)
            cv2.imshow("window", self.tempFlipImg)
            cv2.waitKey(0)

            cv2.destroyAllWindows()


        else:
            SI.showCvImg[0] = SI.showCvImg[1]
        SI.ShowPic(SI.showCvImg[0], SI.ui.labelShowImg)

        # cv2.imshow("window", SI.showCvImg[0])
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # SI.ShowGrayPic(SI.showCvImg[0], SI.ui.labelShowImg)

    def AdjustStrength(self):
        pass

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
        print(SI.ui.radioButtonPositive.isChecked())
        if(SI.ui.radioButtonPositive.isChecked()):
            SI.showCvImg[0] = self.tempSobelImg
            print("positive")
        else:
            SI.showCvImg[0] = self.tempFlipImg
            print("negative")
        SI.ShowGrayPic(SI.showCvImg[0], SI.ui.labelShowImg)
        print(np.array_equal(self.tempSobelImg,self.tempFlipImg))








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
            SI.ShowPic(SI.showCvImg[0],SI.ui.labelShowImg)
            print("ConvertToGrayScale")
        else:
            SI.showCvImg[0] = SI.showCvImg[1]
            SI.ShowPic(SI.showCvImg[0], SI.ui.labelShowImg)
            print("ReturnToColor")


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

SI.ui.show()
app.exec_()
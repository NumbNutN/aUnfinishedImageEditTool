import numpy as np
from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from PySide2.QtGui import QPixmap ,QImage
import cv2
from lib.share import SI

class FIleMenu:
    def __init__(self):
        SIobj.ui.fileOpenAction.triggered.connect(self.OpenFile)
        SIobj.ui.saveAsAction.triggered.connect(self.SaveFile)
        SIobj.ui.cleanHistoryAction.triggered.connect(self.WrapOutHistory)
        SIobj.historyFilePath = []

        #读取历史图片路径
        #txt中记录的图片地址从上到下为从新到旧
        with open ("./historyFile.txt",'r') as file:
            for path in file:
                SIobj.historyFilePath.append(path.strip())

        print(SIobj.historyFilePath)

        #加载最近打开图片窗口
        qfile_historyFile_stats = QFile("./HistoryFile.ui")
        qfile_historyFile_stats.open(QFile.ReadOnly)
        qfile_historyFile_stats.close()
        SIobj.historyPathViewUi = QUiLoader().load(qfile_historyFile_stats)
        SIobj.ui.recentFileAction.triggered.connect(self.ViewRecentFile)
        SIobj.historyPathViewUi.listHistoryFile.itemClicked.connect(self.RecentFileShowCurrentItem)
        SIobj.historyPathViewUi.btnVerifyHistoryFile.clicked.connect(self.VerifyHistoryFile)



    #兼容中文的读取方案
    def readFile(self,filePath):
        raw_data = np.fromfile(filePath,dtype=np.uint8)
        img = cv2.imdecode(raw_data,cv2.IMREAD_COLOR)
        return img

    def OpenFile(self):
        filePath,fileType = QFileDialog.getOpenFileName(
            SIobj.ui,
            "选择图片路径",
            r"d:",
            "(*.png *.jpg *.bmp)"
        )

        SIobj.cvImg = self.readFile(filePath)
        SIobj.showCvImg.insert(0,self.cvImg)
        SIobj.ShowPic(SIobj.showCvImg,SIobj.ui.labelShowImg)
        SIobj.oriCvW = SIobj.showCvW = SIobj.cvImg.shape[1]
        SIobj.oriCvH = SIobj.showCvH = SIobj.cvImg.shape[0]
        SIobj.resize = Resize()
        Resize.showImgInfoRefresh(Resize)

        #历史记录最多存储10条，超过10条以队列的形式从队尾顶出
        if len(SIobj.historyFilePath) >= 10:
            SIobj.historyFilePath.pop()
        SIobj.historyFilePath.insert(0,filePath)
        #每次更新状态后重新写最近打开历史记录文件
        with open ("./historyFile.txt",'w') as file:
            for path in SIobj.historyFilePath:
                file.write(path+'\n')
        print(SIobj.historyFilePath)





        # 直接将磁盘文件加载为QPixmap格式的方法
        # img = QPixmap(filePath)
        # self.ui.labelShowImg.setPixmap(img)

        # #适当调整图片大小的逻辑
        # if(SIobj.cvImg.shape[1]>1280 or SIobj.cvImg.shape[0]>720):
        #     SIobj.ui.labelShowImg.setMaximumSize(1280,int(1280/SIobj.showCvW*SIobj.showCvH))


    def SaveFile(self):
        filePath = QFileDialog.getExistingDirectory(SIobj.ui,"选择保存的路径")
        cv2.imwrite("TempName",SIobj.showCvImg[0])

    def WrapOutHistory(self):
        SIobj.historyFilePath = []
        with open("./historyFile.txt",'w') as file:
            file.write('')

    def RenewListFileHistory(self):
        SIobj.historyPathViewUi.listHistoryFile.clear()
        for path in SIobj.historyFilePath:
            SIobj.historyPathViewUi.listHistoryFile.addItem(path)

    def ViewRecentFile(self):
        self.RenewListFileHistory()
        SIobj.historyPathViewUi.show()

    def RecentFileShowCurrentItem(self):
        path = SIobj.historyPathViewUi.listHistoryFile.currentItem().text()
        imgCvPreview = self.readFile(path)
        SIobj.ShowPic(imgCvPreview,SIobj.historyPathViewUi.labelHistoryPreview)

        try:
            channelsNum = imgCvPreview.shape[2]
        except IndexError:
            channelsNum = 2
            imgType = "?"
        else:
            imgType = "RGB888"

        SIobj.historyPathViewUi.labelPreviewInfo.setText(
            "size: "+str(imgCvPreview.shape[1])+'x'+str(imgCvPreview.shape[0])+'\t'+
            "channels: "+str(channelsNum)+'\t'+"type: "+imgType)

    def VerifyHistoryFile(self):
        SIobj.historyPathViewUi.hide()




class EdgeDetection:
    pass

class TabWidget:
    def __init__(self):
        SIobj.ui.tabWidgetFunction.currentChanged.connect(self.TabChange)

    def TabChange(self):
        print(SIobj.ui.tabWidgetFunction.currentIndex())
        if not(np.array_equal(SIobj.showCvImg[0],SIobj.showCvImg[1])):
            SIobj.showCvImg.insert(SIobj.showCvImg,0)
        print(len(SIobj.showCvImg))

class Resize:
    def __init__(self):

        #设置宽度滑块最大/小值
        SIobj.ui.sliderW.setMinimum(1)
        SIobj.ui.sliderW.setMaximum(SIobj.oriCvW)
        # 设置高度滑块最大/小值
        SIobj.ui.sliderH.setMinimum(1)
        SIobj.ui.sliderH.setMaximum(SIobj.oriCvH)
        #设置步长
        SIobj.ui.sliderW.setSingleStep(1)
        SIobj.ui.sliderH.setSingleStep(1)

        #设置当前值
        SIobj.ui.sliderW.setValue(SIobj.oriCvW)
        SIobj.ui.sliderH.setValue(SIobj.oriCvH)

        #设置刻度的位置，刻度在下方
        SIobj.ui.sliderW.setTickPosition(QSlider.TicksBelow)
        SIobj.ui.sliderH.setTickPosition(QSlider.TicksBelow)

        #设置刻度的间隔
        SIobj.ui.sliderW.setTickInterval(int(1 / 5*SIobj.oriCvW))
        SIobj.ui.sliderH.setTickInterval(int(1 / 5 * SIobj.oriCvH))

        #设置控件的信号处理函数
        SIobj.ui.sliderW.valueChanged.connect(self.SliderChangeW)
        SIobj.ui.sliderH.valueChanged.connect(self.SliderChangeH)
        
        #设置步长调节器的最大/小值
        SIobj.ui.sBoxResizeW.setMaximum(SIobj.oriCvW)
        SIobj.ui.sBoxResizeH.setMaximum(SIobj.oriCvH)
        SIobj.ui.sBoxResizeW.setMinimum(1)
        SIobj.ui.sBoxResizeH.setMinimum(1)
        
        #设置步长调节器
        SIobj.ui.sBoxResizeW.setWrapping(True)
        SIobj.ui.sBoxResizeH.setWrapping(True)
        
        #设置步长调节器的信号处理函数
        SIobj.ui.sBoxResizeW.valueChanged.connect(self.CustomizeSizeW)
        SIobj.ui.sBoxResizeH.valueChanged.connect(self.CustomizeSizeH)

        #设置步长调节器的初始值
        SIobj.ui.sBoxResizeW.setValue(SIobj.oriCvW)
        SIobj.ui.sBoxResizeH.setValue(SIobj.oriCvH)


        # #固定缩放比控件
        # SIobj.ui.bGroupFixedRatio.buttonClicked.connect(self.changeFixedRatioRule)


    #resize的两个个重要全局影响选项
    # 1- 是否选择了固定缩放比    SIobj.ui.cboxFixedRatio.isChecked()
    # 2- 调节模式为百分比还是像素


    def ChangeSizeAndResize(self,dir):
        if (SIobj.ui.cboxFixedRatio.isChecked()):
            if(dir=="w"):
                SIobj.showCvH = int(SIobj.showCvW / SIobj.oriCvW * SIobj.oriCvH)
            elif(dir=="h"):
                SIobj.showCvW = int(SIobj.showCvH / SIobj.oriCvH * SIobj.oriCvW)

        SIobj.showCvImg[0] = cv2.resize(SIobj.showCvImg[1], (SIobj.showCvW, SIobj.showCvH))


    def showImgInfoRefresh(self):
        #更新图片下端尺寸
        SIobj.ui.labelShowImgInfo.setText("Size:%dx%d" %(SIobj.showCvW,SIobj.showCvH))
        #更新滑动条下方的尺寸
        SIobj.ui.labelSliderWInfo.setText(str(SIobj.showCvW))
        SIobj.ui.labelSliderHInfo.setText(str(SIobj.showCvH))

        #下面的改动会调用这些控件的回调函数导致极大的性能浪费，最严重时，会触发python递归函数栈满溢出导致程序异常中止，（python最多递归1000层）
        #对所有的控件进行信号屏蔽
        SIobj.ui.sBoxResizeW.blockSignals(True)
        SIobj.ui.sBoxResizeH.blockSignals(True)
        SIobj.ui.sliderW.blockSignals(True)
        SIobj.ui.sliderH.blockSignals(True)
        #更新自定义数字筐的尺寸
        SIobj.ui.sBoxResizeW.setValue(SIobj.showCvW)
        SIobj.ui.sBoxResizeH.setValue(SIobj.showCvH)
        #请自行设置滑动条的数据
        SIobj.ui.sliderW.setValue(SIobj.showCvW)
        SIobj.ui.sliderH.setValue(SIobj.showCvH)

        #取消屏蔽
        SIobj.ui.sBoxResizeW.blockSignals(False)
        SIobj.ui.sBoxResizeH.blockSignals(False)
        SIobj.ui.sliderW.blockSignals(False)
        SIobj.ui.sliderH.blockSignals(False)

    '''
    这个函数是W滑动条的Trigger
    判断内容包括
     1.是否固定缩放比  SIobj.ui.cboxFixedRatio.isChecked()
       固定则要同时移动另一个滑动条
       
       
    会更改图片下端、自定义缩放比筐的尺寸
    '''
    def SliderChangeW(self):
        SIobj.showCvW = SIobj.ui.sliderW.value()
        #print(SIobj.showCvW/SIobj.oriCvW)
        # 原方案  换算比例
        # SIobj.showCvImg = self.resizeShowImg(SIobj.cvImg,0,0,fx=SIobj.showCvW/SIobj.oriCvW)
        # SIobj.showCvH = SIobj.showCvImg.shape[0]
        # SIobj.ui.sliderH.setValue(SIobj.showCvH)

        self.ChangeSizeAndResize("w")

        SIobj.ShowPic(SIobj.showCvImg[0], SIobj.ui.labelShowImg)
        print("debug4")
        #更改图片信息尺寸
        self.showImgInfoRefresh()
        

    def SliderChangeH(self):
        SIobj.showCvH = SIobj.ui.sliderH.value()
        self.ChangeSizeAndResize("h")
        SIobj.ShowPic(SIobj.showCvImg[0], SIobj.ui.labelShowImg)
        print("debug3")
        # 更改图片信息尺寸
        self.showImgInfoRefresh()

    '''
    这个函数是W滑动条的Trigger
    判断内容包括
        1.是否固定缩放比  SIobj.ui.cboxFixedRatio.isChecked()
          固定则要设置另一个单位和
        2.单位是像素还是比例，按要求调节显示的单位
    '''

    def CustomizeSizeW(self):
        SIobj.showCvW = SIobj.ui.sBoxResizeW.value()
        self.ChangeSizeAndResize("w")
        SIobj.ShowPic(SIobj.showCvImg[0], SIobj.ui.labelShowImg)
        print(SIobj.showCvW, SIobj.showCvH)
        print("Debug")
        # 更改图片信息尺寸
        self.showImgInfoRefresh()

    def CustomizeSizeH(self):
        SIobj.showCvH = SIobj.ui.sBoxResizeH.value()
        self.ChangeSizeAndResize("h")
        SIobj.ShowPic(SIobj.showCvImg[0], SIobj.ui.labelShowImg)
        print("debug2")
        # 更改图片信息尺寸
        self.showImgInfoRefresh()

class GrayScale:
    def __init__(self):
        pass

    def TranToGrayScal(self):
        SIobj.showCvImg[0] = cv2.cvtColor(SIobj.showCvImg[1],cv2.COLOR_BGR2GRAY)


app = QApplication([])

qfile_stats = QFile("ImgMargin.ui")
qfile_stats.open(QFile.ReadOnly)
qfile_stats.close()
SIobj = SI()
SIobj.ui = QUiLoader().load(qfile_stats)
SIobj.InitImg()
SIobj.ShowPic(SIobj.showCvImg[0],SIobj.ui.labelShowImg)


SIobj.fileMenu = FIleMenu()
SIobj.resize = Resize()
SIobj.tabwidget = TabWidget()

SIobj.ui.show()
app.exec_()
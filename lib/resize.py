from lib.share import SI
import cv2
import numpy as np
from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider

class Resize:
    def __init__(self):

        # 设置宽度滑块最大/小值
        SI.ui.sliderW.setMinimum(1)
        SI.ui.sliderW.setMaximum(SI.oriW)
        # 设置高度滑块最大/小值
        SI.ui.sliderH.setMinimum(1)
        SI.ui.sliderH.setMaximum(SI.oriH)
        # 设置步长
        SI.ui.sliderW.setSingleStep(1)
        SI.ui.sliderH.setSingleStep(1)

        # 设置当前值
        SI.ui.sliderW.setValue(SI.oriW)
        SI.ui.sliderH.setValue(SI.oriH)

        # 设置刻度的位置，刻度在下方
        SI.ui.sliderW.setTickPosition(QSlider.TicksBelow)
        SI.ui.sliderH.setTickPosition(QSlider.TicksBelow)

        # 设置刻度的间隔
        SI.ui.sliderW.setTickInterval(int(1 / 5 * SI.oriW))
        SI.ui.sliderH.setTickInterval(int(1 / 5 * SI.oriH))

        # 设置控件的信号处理函数
        SI.ui.sliderW.valueChanged.connect(self.SliderChangeW)
        SI.ui.sliderH.valueChanged.connect(self.SliderChangeH)

        # 设置步长调节器的最大/小值
        SI.ui.sBoxResizeW.setMaximum(SI.oriW)
        SI.ui.sBoxResizeH.setMaximum(SI.oriH)
        SI.ui.sBoxResizeW.setMinimum(1)
        SI.ui.sBoxResizeH.setMinimum(1)

        # 设置步长调节器
        SI.ui.sBoxResizeW.setWrapping(True)
        SI.ui.sBoxResizeH.setWrapping(True)

        # 设置步长调节器的信号处理函数
        SI.ui.sBoxResizeW.valueChanged.connect(self.CustomizeSizeW)
        SI.ui.sBoxResizeH.valueChanged.connect(self.CustomizeSizeH)

        # 设置步长调节器的初始值
        SI.ui.sBoxResizeW.setValue(SI.oriW)
        SI.ui.sBoxResizeH.setValue(SI.oriH)

        #默认像素缩放模式
        SI.ui.rbtnResizePixel.setChecked(True)


    # resize的两个个重要全局影响选项
    # 1- 是否选择了固定缩放比    SI.ui.cboxFixedRatio.isChecked()
    # 2- 调节模式为百分比还是像素

    def ChangeSizeAndResize(self, dir):
        if (SI.ui.cboxFixedRatio.isChecked()):
            if (dir == "w"):
                SI.curH = int(SI.curW / SI.oriW * SI.oriH)
            elif (dir == "h"):
                SI.curW = int(SI.curH / SI.oriH * SI.oriW)

        SI.processingImgQueue[0] = cv2.resize(SI.processingImgQueue[1], (SI.curW, SI.curH))

    def showImgInfoRefresh(self):
        # 更新图片下端尺寸
        SI.PrintSimpleImgInfo(SI.processingImgQueue[0],SI.ui.labelShowImgInfo)
        #SI.ui.labelShowImgInfo.setText("Size:%dx%d" % (SI.curW, SI.curH))
        # 更新滑动条下方的尺寸
        SI.ui.labelSliderWInfo.setText(str(SI.curW))
        SI.ui.labelSliderHInfo.setText(str(SI.curH))

        # 下面的改动会调用这些控件的回调函数导致极大的性能浪费，最严重时，会触发python递归函数栈满溢出导致程序异常中止，（python最多递归1000层）
        # 对所有的控件进行信号屏蔽
        SI.ui.sBoxResizeW.blockSignals(True)
        SI.ui.sBoxResizeH.blockSignals(True)
        SI.ui.sliderW.blockSignals(True)
        SI.ui.sliderH.blockSignals(True)
        # 更新自定义数字筐的尺寸
        SI.ui.sBoxResizeW.setValue(SI.curW)
        SI.ui.sBoxResizeH.setValue(SI.curH)
        # 请自行设置滑动条的数据
        SI.ui.sliderW.setValue(SI.curW)
        SI.ui.sliderH.setValue(SI.curH)

        # 取消屏蔽
        SI.ui.sBoxResizeW.blockSignals(False)
        SI.ui.sBoxResizeH.blockSignals(False)
        SI.ui.sliderW.blockSignals(False)
        SI.ui.sliderH.blockSignals(False)

    '''
    这个函数是W滑动条滑动的事件触发函数
    判断内容包括
     1.是否固定缩放比  SI.ui.cboxFixedRatio.isChecked()
       固定则要同时移动另一个滑动条


    会更改图片下端、自定义缩放比筐的尺寸
    '''

    def SliderChangeW(self):
        SI.curW = SI.ui.sliderW.value()
        # print(SI.curW/SI.oriW)
        # 原方案  换算比例
        # SI.processingImgQueue = self.resizeShowImg(SI.cvImg,0,0,fx=SI.curW/SI.oriW)
        # SI.curH = SI.processingImgQueue.shape[0]
        # SI.ui.sliderH.setValue(SI.curH)

        self.ChangeSizeAndResize("w")

        SI.ShowBGRPic(SI.processingImgQueue[0], SI.ui.labelImgViewpot)
        print("debug4")
        # 更改图片信息尺寸
        self.showImgInfoRefresh()

    def SliderChangeH(self):
        SI.curH = SI.ui.sliderH.value()
        self.ChangeSizeAndResize("h")
        SI.ShowBGRPic(SI.processingImgQueue[0], SI.ui.labelImgViewpot)
        print("debug3")
        # 更改图片信息尺寸
        self.showImgInfoRefresh()

    '''
    这个函数是W滑动条的Trigger
    判断内容包括
        1.是否固定缩放比  SI.ui.cboxFixedRatio.isChecked()
          固定则要设置另一个单位和
        2.单位是像素还是比例，按要求调节显示的单位
    '''

    def CustomizeSizeW(self):
        SI.curW = SI.ui.sBoxResizeW.value()
        self.ChangeSizeAndResize("w")
        SI.ShowBGRPic(SI.processingImgQueue[0], SI.ui.labelImgViewpot)
        print(SI.curW, SI.curH)
        print("Debug")
        # 更改图片信息尺寸
        self.showImgInfoRefresh()

    def CustomizeSizeH(self):
        SI.curH = SI.ui.sBoxResizeH.value()
        self.ChangeSizeAndResize("h")
        SI.ShowBGRPic(SI.processingImgQueue[0], SI.ui.labelImgViewpot)
        print("debug2")
        # 更改图片信息尺寸
        self.showImgInfoRefresh()
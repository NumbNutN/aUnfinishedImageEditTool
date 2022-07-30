from lib.share import SI
import cv2
import numpy as np
from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *

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
            grayImg = cv2.cvtColor(SI.processingImgQueue[0],cv2.COLOR_BGR2GRAY)
            sobelx = cv2.Sobel(grayImg, -1, 1, 0, ksize=3)
            sobely = cv2.Sobel(grayImg, -1, 0, 1, ksize=3)
            self.tempSobelImg = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
            self.tempFlipImg = self.FlipImg(self.tempSobelImg)
            self.PositiveAndNegativeChange()
            #SI.processingImgQueue[0] = self.tempSobelImg
            #SI.ShowGrayPic(SI.processingImgQueue[0], SI.ui.labelShowImg)
        else:
            SI.processingImgQueue[0] = SI.processingImgQueue[1]
            SI.ShowPic(SI.processingImgQueue[0], SI.ui.labelShowImg)
        SI.PrintSimpleImgInfo(SI.processingImgQueue[0], SI.ui.labelShowImgInfo)

        print(SI.processingImgQueue[0].shape)

        # cv2.imshow("window", SI.processingImgQueue[0])
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # SI.ShowGrayPic(SI.processingImgQueue[0], SI.ui.labelShowImg)

    def AdjustStrength(self):
        if (SI.ui.radioButtonNagetive.isChecked()):
            #SI.processingImgQueue[0] = cv2.inRange(self.tempFlipImg,255 - SI.ui.sliderMarginAdjustStrength.value(),256)
            SI.processingImgQueue[0] = cv2.inRange(self.tempSobelImg,0, SI.ui.sliderMarginAdjustStrength.value())

        else:
            SI.processingImgQueue[0] = cv2.inRange(self.tempSobelImg, 255 - SI.ui.sliderMarginAdjustStrength.value(), 255)

        SI.ShowPic(SI.processingImgQueue[0], SI.ui.labelShowImg)
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
                SI.processingImgQueue[0] = self.tempSobelImg
                print("positive")
            else:
                SI.processingImgQueue[0] = self.tempFlipImg
                SI.print_img_txt(SI.processingImgQueue[0])
                print("negative")
            SI.ShowGrayPic(SI.processingImgQueue[0], SI.ui.labelShowImg)



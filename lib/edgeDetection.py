from lib.share import SI
import cv2
import numpy as np
from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *

class EdgeDetection:

    tempEdgeImg = None
    tempFlipImg = None

    def __init__(self):
        #边缘检测勾选框和单选区的事件处理函数的绑定
        SI.mainWindow.cBoxCvtMargin.stateChanged.connect(self.FindEdge)
        #SI.mainWindow.bGroupMarginBackground.buttonClicked.connect(self.RowAndFilmChange)
        SI.mainWindow.bGroupMarginBackground.buttonClicked.connect(self.FindEdge)
        SI.mainWindow.bGroupEdgeMethod.buttonClicked.connect(self.FindEdge)

        #默认原片模式
        SI.mainWindow.rbtnRow.setChecked(True)
        #默认采用canny检测
        SI.mainWindow.rBtnCanny.setChecked(True)

        # 设置宽度滑块最大/小值
        SI.mainWindow.sliderMarginAdjustStrength.setMinimum(0)
        SI.mainWindow.sliderMarginAdjustStrength.setMaximum(255)

        # 设置步长
        SI.mainWindow.sliderMarginAdjustStrength.setSingleStep(1)

        # 设置当前值
        SI.mainWindow.sliderMarginAdjustStrength.setValue(127)
        SI.mainWindow.labelEdgeStrength.setText(str(SI.mainWindow.sliderMarginAdjustStrength.value()))

        # 设置刻度的位置，刻度在下方
        SI.mainWindow.sliderMarginAdjustStrength.setTickPosition(QSlider.TicksBelow)

        # 设置刻度的间隔
        SI.mainWindow.sliderMarginAdjustStrength.setTickInterval(int(1 / 5 * 255))

        # 设置控件的信号处理函数
        SI.mainWindow.sliderMarginAdjustStrength.valueChanged.connect(self.AdjustThreshold)




    def FindEdge(self):
        #判断边缘检测checkBox是否选中
        if (SI.mainWindow.cBoxCvtMargin.isChecked()):
            #判断是否为sobel算子并生成正反两种灰度图存储在内存
            if (SI.mainWindow.rBtnSobel.isChecked()):
                #通道数不唯一则sobel卷积前转化成灰度图
                if(SI.returnChannelNum(SI.processingImgQueue[1])!=1):
                    grayImg = cv2.cvtColor(SI.processingImgQueue[1],cv2.COLOR_BGR2GRAY)
                else:
                    grayImg = SI.processingImgQueue[1]
                sobelx = cv2.Sobel(grayImg, -1, 1, 0, ksize=3)
                sobely = cv2.Sobel(grayImg, -1, 0, 1, ksize=3)
                self.tempEdgeImg = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
                self.tempFlipImg = self.FlipImg(self.tempEdgeImg)

            self.RowAndFilmChange()
        else:
            SI.processingImgQueue[0] = SI.processingImgQueue[1]
            SI.ShowBGRPic(SI.processingImgQueue[0], SI.mainWindow.labelImgViewpot)

        SI.PrintSimpleImgInfo(SI.processingImgQueue[0], SI.mainWindow.labelShowImgInfo)


    def AdjustThreshold(self):
        if (SI.mainWindow.cBoxCvtMargin.isChecked()):
            #判断图像为原片
            if (SI.mainWindow.rbtnRow.isChecked()):
                #判断图像采用canny算法
                if (SI.mainWindow.rBtnCanny.isChecked()):
                    SI.processingImgQueue[0] = cv2.Canny(SI.processingImgQueue[1],0,SI.mainWindow.sliderMarginAdjustStrength.value())
                #采用sobel算子
                else:
                    SI.processingImgQueue[0] = cv2.inRange(self.tempEdgeImg,
                                                           255 - SI.mainWindow.sliderMarginAdjustStrength.value(), 255)
            #判断图像为底片
            else:
                # 判断图像采用canny算法
                if (SI.mainWindow.rBtnCanny.isChecked()):
                    SI.processingImgQueue[0] = cv2.Canny(SI.processingImgQueue[1], 0,SI.mainWindow.sliderMarginAdjustStrength.value())
                    SI.processingImgQueue[0] = self.FlipImg(SI.processingImgQueue[0])
                #判断图像采用sobel算子
                else:
                    SI.processingImgQueue[0] = cv2.inRange(self.tempEdgeImg, 0,
                                                           SI.mainWindow.sliderMarginAdjustStrength.value())

            SI.ShowBGRPic(SI.processingImgQueue[0], SI.mainWindow.labelImgViewpot)
            SI.mainWindow.labelEdgeStrength.setText(str(SI.mainWindow.sliderMarginAdjustStrength.value()))


    def RowAndFilmChange(self):
        #判断边缘检测checkBox是否选中
        #解决的问题：canny选择底片不会自动转成底片
        if(SI.mainWindow.cBoxCvtMargin.isChecked()):

            #判断是否为sobel算子
            if (SI.mainWindow.rBtnSobel.isChecked()):
                if(SI.mainWindow.rbtnRow.isChecked()):
                    SI.processingImgQueue[0] = self.tempEdgeImg
                    print("row")
                else:
                    SI.processingImgQueue[0] = self.tempFlipImg
                    print("film")

            else:
                SI.processingImgQueue[0] = cv2.Canny(SI.processingImgQueue[1], 0,SI.mainWindow.sliderMarginAdjustStrength.value())
                if (SI.mainWindow.rbtnFilm.isChecked()):
                    SI.processingImgQueue[0] = self.FlipImg(SI.processingImgQueue[0])

            SI.ShowGrayPic(SI.processingImgQueue[0], SI.mainWindow.labelImgViewpot)


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



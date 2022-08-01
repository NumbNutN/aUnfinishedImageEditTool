from lib.share import SI
import cv2
import numpy as np
from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *

class Transparent:

    SLIDERLIGHTANDDARK = 100
    SLIDERCOLOR = 101

    SLIDERHCOLOR = 104
    SLIDERLCOLOR = 105

    GREATER = 108
    LESS = 109

    def __init__(self):

        # 设置深浅色
        SI.ui.cBoxLight.setChecked(True)

        # 设置宽度滑块最大/小值
        SI.ui.sliderLight.setMinimum(0)
        SI.ui.sliderLight.setMaximum(255)
        SI.ui.sliderDark.setMinimum(0)
        SI.ui.sliderDark.setMaximum(255)

        SI.ui.sliderRHigh.setMinimum(0)
        SI.ui.sliderRHigh.setMaximum(255)
        SI.ui.sliderGHigh.setMinimum(0)
        SI.ui.sliderGHigh.setMaximum(255)
        SI.ui.sliderBHigh.setMinimum(0)
        SI.ui.sliderBHigh.setMaximum(255)

        SI.ui.sliderRLow.setMinimum(0)
        SI.ui.sliderRLow.setMaximum(255)
        SI.ui.sliderGLow.setMinimum(0)
        SI.ui.sliderGLow.setMaximum(255)
        SI.ui.sliderBLow.setMinimum(0)
        SI.ui.sliderBLow.setMaximum(255)

        # 设置步长
        SI.ui.sliderDark.setSingleStep(1)
        SI.ui.sliderLight.setSingleStep(1)

        SI.ui.sliderRHigh.setSingleStep(1)
        SI.ui.sliderGHigh.setSingleStep(1)
        SI.ui.sliderBHigh.setSingleStep(1)

        SI.ui.sliderRLow.setSingleStep(1)
        SI.ui.sliderGLow.setSingleStep(1)
        SI.ui.sliderBLow.setSingleStep(1)

        # 设置当前值
        SI.ui.sliderDark.setValue(255)
        SI.ui.sliderLight.setValue(255)

        SI.ui.sliderRHigh.setValue(255)
        SI.ui.sliderGHigh.setValue(255)
        SI.ui.sliderBHigh.setValue(255)

        SI.ui.sliderRLow.setValue(0)
        SI.ui.sliderGLow.setValue(0)
        SI.ui.sliderBLow.setValue(0)

        #SI.ui.labelEdgeStrength.setText(str(SI.ui.sliderDarkAndLight.value()))

        # 设置刻度的位置，刻度在下方
        SI.ui.sliderLight.setTickPosition(QSlider.TicksBelow)
        SI.ui.sliderDark.setTickPosition(QSlider.TicksBelow)

        # 设置刻度的间隔
        SI.ui.sliderDark.setTickInterval(int(1 / 5 * 255))
        SI.ui.sliderLight.setTickInterval(int(1 / 5 * 255))

        # 设置控件的信号处理函数
        SI.ui.sliderDark.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERLIGHTANDDARK))
        SI.ui.sliderLight.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERLIGHTANDDARK))



        SI.ui.sliderRHigh.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))
        SI.ui.sliderGHigh.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))
        SI.ui.sliderBHigh.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))

        SI.ui.sliderRLow.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))
        SI.ui.sliderGLow.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))
        SI.ui.sliderBLow.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))

        #显示滑动条改变后的值和样式
        SI.ui.sliderLight.valueChanged.connect(
            lambda: self.showSliderValue(SI.ui.labelLightValue, SI.ui.sliderLight,self.SLIDERLIGHTANDDARK,SI.ui.labelLightSample))
        SI.ui.sliderDark.valueChanged.connect(
            lambda: self.showSliderValue(SI.ui.labelDarkValue, SI.ui.sliderDark,self.SLIDERLIGHTANDDARK,SI.ui.labelDarkSample))

        SI.ui.sliderRHigh.valueChanged.connect(
            lambda: self.showSliderValue(SI.ui.labelRHighValue, SI.ui.sliderRHigh,self.SLIDERHCOLOR,SI.ui.labelCHighSample))
        SI.ui.sliderGHigh.valueChanged.connect(
            lambda: self.showSliderValue(SI.ui.labelGHighValue, SI.ui.sliderGHigh,self.SLIDERHCOLOR,SI.ui.labelCHighSample))
        SI.ui.sliderBHigh.valueChanged.connect(
            lambda: self.showSliderValue(SI.ui.labelBHighValue, SI.ui.sliderBHigh,self.SLIDERHCOLOR,SI.ui.labelCHighSample))
        SI.ui.sliderRLow.valueChanged.connect(
            lambda: self.showSliderValue(SI.ui.labelRLowValue, SI.ui.sliderRLow,self.SLIDERLCOLOR,SI.ui.labelCLowSample))
        SI.ui.sliderGLow.valueChanged.connect(
            lambda: self.showSliderValue(SI.ui.labelGLowValue, SI.ui.sliderGLow,self.SLIDERLCOLOR,SI.ui.labelCLowSample))
        SI.ui.sliderBLow.valueChanged.connect(
            lambda: self.showSliderValue(SI.ui.labelBLowValue, SI.ui.sliderBLow,self.SLIDERLCOLOR,SI.ui.labelCLowSample))

        #显示滑动条数值
        SI.ui.labelLightValue.setText(str(SI.ui.sliderLight.value()))
        SI.ui.labelDarkValue.setText(str(SI.ui.sliderDark.value()))
        SI.ui.labelRHighValue.setText(str(SI.ui.sliderRHigh.value()))
        SI.ui.labelGHighValue.setText(str(SI.ui.sliderGHigh.value()))
        SI.ui.labelBHighValue.setText(str(SI.ui.sliderBHigh.value()))
        SI.ui.labelRLowValue.setText(str(SI.ui.sliderRLow.value()))
        SI.ui.labelGLowValue.setText(str(SI.ui.sliderGLow.value()))
        SI.ui.labelBLowValue.setText(str(SI.ui.sliderBLow.value()))
    
    def changeToBGRA(self,cvImg,rThrHigh,gThrHigh,bThrHigh,rThrLow,gThrLow,bThrLow):
        newImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2BGRA)
        width, height, channel = newImg.shape
        for i in range(width):
            for j in range(height):
                b, g, r, a = newImg[i][j]
                # 把白色像素改成透明色
                if (r >=rThrHigh and g >= gThrHigh and b >= bThrHigh) or (r <=rThrLow and g<=gThrLow and b<=bThrLow):
                    newImg[i][j][3] = 0

        return newImg

    def AdjustTransparent(self,sliderType):
        if (sliderType == self.SLIDERLIGHTANDDARK):
            if(SI.ui.cBoxLight.isChecked()):
                up = SI.ui.sliderLight.value()
            else:
                up = 255
            if (SI.ui.cBoxDark.isChecked()):
                down = SI.ui.sliderDark.value()
            else:
                down = 0
            SI.processingImgQueue[0] = self.changeToBGRA(SI.processingImgQueue[1], up,up,up,down,down,down)
            print("Light: "+"Greater than"+str(up)+" Less than"+str(down))
            # SI.processingImgQueue[0] = self.changeToBGRA(SI.processingImgQueue[1], up, up, up, 255, 255, 255)
            # SI.processingImgQueue[0] = self.changeToBGRA(SI.processingImgQueue[1], 0,0,0,down,down,down)

        elif (sliderType == self.SLIDERCOLOR):
            if(SI.ui.cBoxColorHigh.isChecked()):
                rTH = SI.ui.sliderRHigh.value()
                gTH = SI.ui.sliderGHigh.value()
                bTH = SI.ui.sliderGHigh.value()
            else:
                rTH = gTH = bTH = 255
            if(SI.ui.cBoxColorLow.isChecked()):
                rTL = SI.ui.sliderRLow.value()
                gTL = SI.ui.sliderGLow.value()
                bTL = SI.ui.sliderGLow.value()
            else:
                rTL = gTL = bTL = 0
            SI.processingImgQueue[0] = self.changeToBGRA(SI.processingImgQueue[1],rTH,gTH,bTH,rTL,gTL,bTL)

        SI.ShowBGRAPic(SI.processingImgQueue[0], SI.ui.labelImgViewpot)
        SI.PrintSimpleImgInfo(SI.processingImgQueue[0],SI.ui.labelImgViewpot)
        print("setTransparent")

    def showSliderValue(self,label,slider,sliderType,clabel,crgblabel=None):
        val = slider.value()
        label.setText(str(val))
        if(sliderType == self.SLIDERLIGHTANDDARK):
            for i in range(SI.cSamW):
                for j in range(SI.cSamH):
                    SI.colorSample[i][j]=(val,val,val)
            SI.ShowBGRPic(SI.colorSample.astype(np.uint8), clabel)

        elif(sliderType==self.SLIDERHCOLOR):
            for i in range(SI.cSamW):
                for j in range(SI.cSamH):
                    SI.colorSample[i][j]=(SI.ui.sliderBHigh.value(),SI.ui.sliderGHigh.value(),SI.ui.sliderRHigh.value())
            SI.ShowBGRPic(SI.colorSample.astype(np.uint8), clabel)

        else:
            for i in range(SI.cSamW):
                for j in range(SI.cSamH):
                    SI.colorSample[i][j]=(SI.ui.sliderBLow.value(),SI.ui.sliderGLow.value(),SI.ui.sliderRLow.value())
            SI.ShowBGRPic(SI.colorSample.astype(np.uint8), clabel)




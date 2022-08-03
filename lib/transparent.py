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
        SI.mainWindow.cBoxLight.setChecked(True)

        # 设置宽度滑块最大/小值
        SI.mainWindow.sliderLight.setMinimum(0)
        SI.mainWindow.sliderLight.setMaximum(255)
        SI.mainWindow.sliderDark.setMinimum(0)
        SI.mainWindow.sliderDark.setMaximum(255)

        SI.mainWindow.sliderRHigh.setMinimum(0)
        SI.mainWindow.sliderRHigh.setMaximum(255)
        SI.mainWindow.sliderGHigh.setMinimum(0)
        SI.mainWindow.sliderGHigh.setMaximum(255)
        SI.mainWindow.sliderBHigh.setMinimum(0)
        SI.mainWindow.sliderBHigh.setMaximum(255)

        SI.mainWindow.sliderRLow.setMinimum(0)
        SI.mainWindow.sliderRLow.setMaximum(255)
        SI.mainWindow.sliderGLow.setMinimum(0)
        SI.mainWindow.sliderGLow.setMaximum(255)
        SI.mainWindow.sliderBLow.setMinimum(0)
        SI.mainWindow.sliderBLow.setMaximum(255)

        # 设置步长
        SI.mainWindow.sliderDark.setSingleStep(1)
        SI.mainWindow.sliderLight.setSingleStep(1)

        SI.mainWindow.sliderRHigh.setSingleStep(1)
        SI.mainWindow.sliderGHigh.setSingleStep(1)
        SI.mainWindow.sliderBHigh.setSingleStep(1)

        SI.mainWindow.sliderRLow.setSingleStep(1)
        SI.mainWindow.sliderGLow.setSingleStep(1)
        SI.mainWindow.sliderBLow.setSingleStep(1)

        # 设置当前值
        SI.mainWindow.sliderDark.setValue(255)
        SI.mainWindow.sliderLight.setValue(255)

        SI.mainWindow.sliderRHigh.setValue(255)
        SI.mainWindow.sliderGHigh.setValue(255)
        SI.mainWindow.sliderBHigh.setValue(255)

        SI.mainWindow.sliderRLow.setValue(0)
        SI.mainWindow.sliderGLow.setValue(0)
        SI.mainWindow.sliderBLow.setValue(0)

        #SI.mainWindow.labelEdgeStrength.setText(str(SI.mainWindow.sliderDarkAndLight.value()))

        # 设置刻度的位置，刻度在下方
        SI.mainWindow.sliderLight.setTickPosition(QSlider.TicksBelow)
        SI.mainWindow.sliderDark.setTickPosition(QSlider.TicksBelow)

        # 设置刻度的间隔
        SI.mainWindow.sliderDark.setTickInterval(int(1 / 5 * 255))
        SI.mainWindow.sliderLight.setTickInterval(int(1 / 5 * 255))

        # 设置控件的信号处理函数
        SI.mainWindow.sliderDark.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERLIGHTANDDARK))
        SI.mainWindow.sliderLight.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERLIGHTANDDARK))



        SI.mainWindow.sliderRHigh.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))
        SI.mainWindow.sliderGHigh.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))
        SI.mainWindow.sliderBHigh.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))

        SI.mainWindow.sliderRLow.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))
        SI.mainWindow.sliderGLow.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))
        SI.mainWindow.sliderBLow.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERCOLOR))

        #显示滑动条改变后的值和样式
        SI.mainWindow.sliderLight.valueChanged.connect(
            lambda: self.showSliderValue(SI.mainWindow.labelLightValue, SI.mainWindow.sliderLight,self.SLIDERLIGHTANDDARK,SI.mainWindow.labelLightSample))
        SI.mainWindow.sliderDark.valueChanged.connect(
            lambda: self.showSliderValue(SI.mainWindow.labelDarkValue, SI.mainWindow.sliderDark,self.SLIDERLIGHTANDDARK,SI.mainWindow.labelDarkSample))

        SI.mainWindow.sliderRHigh.valueChanged.connect(
            lambda: self.showSliderValue(SI.mainWindow.labelRHighValue, SI.mainWindow.sliderRHigh,self.SLIDERHCOLOR,SI.mainWindow.labelCHighSample))
        SI.mainWindow.sliderGHigh.valueChanged.connect(
            lambda: self.showSliderValue(SI.mainWindow.labelGHighValue, SI.mainWindow.sliderGHigh,self.SLIDERHCOLOR,SI.mainWindow.labelCHighSample))
        SI.mainWindow.sliderBHigh.valueChanged.connect(
            lambda: self.showSliderValue(SI.mainWindow.labelBHighValue, SI.mainWindow.sliderBHigh,self.SLIDERHCOLOR,SI.mainWindow.labelCHighSample))
        SI.mainWindow.sliderRLow.valueChanged.connect(
            lambda: self.showSliderValue(SI.mainWindow.labelRLowValue, SI.mainWindow.sliderRLow,self.SLIDERLCOLOR,SI.mainWindow.labelCLowSample))
        SI.mainWindow.sliderGLow.valueChanged.connect(
            lambda: self.showSliderValue(SI.mainWindow.labelGLowValue, SI.mainWindow.sliderGLow,self.SLIDERLCOLOR,SI.mainWindow.labelCLowSample))
        SI.mainWindow.sliderBLow.valueChanged.connect(
            lambda: self.showSliderValue(SI.mainWindow.labelBLowValue, SI.mainWindow.sliderBLow,self.SLIDERLCOLOR,SI.mainWindow.labelCLowSample))

        #显示滑动条数值
        SI.mainWindow.labelLightValue.setText(str(SI.mainWindow.sliderLight.value()))
        SI.mainWindow.labelDarkValue.setText(str(SI.mainWindow.sliderDark.value()))
        SI.mainWindow.labelRHighValue.setText(str(SI.mainWindow.sliderRHigh.value()))
        SI.mainWindow.labelGHighValue.setText(str(SI.mainWindow.sliderGHigh.value()))
        SI.mainWindow.labelBHighValue.setText(str(SI.mainWindow.sliderBHigh.value()))
        SI.mainWindow.labelRLowValue.setText(str(SI.mainWindow.sliderRLow.value()))
        SI.mainWindow.labelGLowValue.setText(str(SI.mainWindow.sliderGLow.value()))
        SI.mainWindow.labelBLowValue.setText(str(SI.mainWindow.sliderBLow.value()))
    
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
            if(SI.mainWindow.cBoxLight.isChecked()):
                up = SI.mainWindow.sliderLight.value()
            else:
                up = 255
            if (SI.mainWindow.cBoxDark.isChecked()):
                down = SI.mainWindow.sliderDark.value()
            else:
                down = 0
            SI.processingImgQueue[0] = self.changeToBGRA(SI.processingImgQueue[1], up,up,up,down,down,down)
            print("Light: "+"Greater than"+str(up)+" Less than"+str(down))
            # SI.processingImgQueue[0] = self.changeToBGRA(SI.processingImgQueue[1], up, up, up, 255, 255, 255)
            # SI.processingImgQueue[0] = self.changeToBGRA(SI.processingImgQueue[1], 0,0,0,down,down,down)

        elif (sliderType == self.SLIDERCOLOR):
            if(SI.mainWindow.cBoxColorHigh.isChecked()):
                rTH = SI.mainWindow.sliderRHigh.value()
                gTH = SI.mainWindow.sliderGHigh.value()
                bTH = SI.mainWindow.sliderGHigh.value()
            else:
                rTH = gTH = bTH = 255
            if(SI.mainWindow.cBoxColorLow.isChecked()):
                rTL = SI.mainWindow.sliderRLow.value()
                gTL = SI.mainWindow.sliderGLow.value()
                bTL = SI.mainWindow.sliderGLow.value()
            else:
                rTL = gTL = bTL = 0
            SI.processingImgQueue[0] = self.changeToBGRA(SI.processingImgQueue[1],rTH,gTH,bTH,rTL,gTL,bTL)

        SI.ShowBGRAPic(SI.processingImgQueue[0], SI.mainWindow.labelImgViewpot)
        SI.PrintSimpleImgInfo(SI.processingImgQueue[0],SI.mainWindow.labelImgViewpot)
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
                    SI.colorSample[i][j]=(SI.mainWindow.sliderBHigh.value(),SI.mainWindow.sliderGHigh.value(),SI.mainWindow.sliderRHigh.value())
            SI.ShowBGRPic(SI.colorSample.astype(np.uint8), clabel)

        else:
            for i in range(SI.cSamW):
                for j in range(SI.cSamH):
                    SI.colorSample[i][j]=(SI.mainWindow.sliderBLow.value(),SI.mainWindow.sliderGLow.value(),SI.mainWindow.sliderRLow.value())
            SI.ShowBGRPic(SI.colorSample.astype(np.uint8), clabel)




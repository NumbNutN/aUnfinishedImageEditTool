from lib.share import SI
import cv2
import numpy as np
from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *

class Transparent:

    SLIDERLIGHTANDDARK = 100
    SLIDERCOLOR = 101

    GREATER = 108
    LESS = 109

    def __init__(self):

        # 设置深浅色
        SI.ui.cBoxLight.setChecked(True)

        # 设置宽度滑块最大/小值
        SI.ui.sliderDarkAndLight.setMinimum(0)
        SI.ui.sliderDarkAndLight.setMaximum(255)

        # 设置步长
        SI.ui.sliderDarkAndLight.setSingleStep(1)

        # 设置当前值
        SI.ui.sliderDarkAndLight.setValue(255)
        #SI.ui.labelEdgeStrength.setText(str(SI.ui.sliderDarkAndLight.value()))

        # 设置刻度的位置，刻度在下方
        SI.ui.sliderDarkAndLight.setTickPosition(QSlider.TicksBelow)

        # 设置刻度的间隔
        SI.ui.sliderDarkAndLight.setTickInterval(int(1 / 5 * 255))

        # 设置控件的信号处理函数
        SI.ui.sliderDarkAndLight.sliderReleased.connect(lambda: self.AdjustTransparent(self.SLIDERLIGHTANDDARK))
        SI.ui.sliderDarkAndLight.valueChanged.connect(lambda: self.showDarkAndLightValue(SI.ui.labelDarkAndLightValue,SI.ui.sliderDarkAndLight))

        #显示滑动条数值
        SI.ui.labelDarkAndLightValue.setText(str(SI.ui.sliderDarkAndLight.value()))

    
    
    def changeToBGRA(self,cvImg,gl,rThrHigh,gThrHigh,bThrHigh,rThrLow,gThrLow,bThrLow):
            newImg = cv2.cvtColor(cvImg, cv2.COLOR_BGR2BGRA)
            width, height, channel = newImg.shape

            if (gl == self.GREATER):
                for i in range(width):
                    for j in range(height):
                        b, g, r, a = newImg[i][j]
                        # 把白色像素改成透明色
                        if r >=rThrHigh and g >= gThrHigh and b >= bThrHigh:
                            newImg[i][j][3] = 0

            elif (gl == self.LESS):
                for i in range(width):
                    for j in range(height):
                        b, g, r, a = newImg[i][j]
                        # 把白色像素改成透明色
                        if r <=rThrHigh and g <= rThrHigh and b <= rThrHigh:
                            newImg[i][j][3] = 0
            return newImg

    def AdjustTransparent(self,sliderType):
        if (sliderType == self.SLIDERLIGHTANDDARK):
            if(SI.ui.cBoxLight.isChecked()):
                up = SI.ui.sliderDarkAndLight.value()
                SI.showCvImg[0] = self.changeToBGRA(SI.showCvImg[1],self.GREATER,up,up,up)
            if (SI.ui.cBoxDark.isChecked()):
                down = SI.ui.sliderDarkAndLight.value()
                SI.showCvImg[0] = self.changeToBGRA(SI.showCvImg[1], self.LESS,down,down,down)

        elif (sliderType == self.SLIDERCOLOR):
            if(SI.ui.cBoxColorHigh.isChecked()):
                rT = SI.ui.sliderRHigh.value()
                gT = SI.ui.sliderGHigh.value()
                bT = SI.ui.sliderGHigh.value()
                SI.showCvImg[0] = self.changeToBGRA(SI.showCvImg[1], self.GREATER,0,0)
            if(SI.ui.cBoxColorLow.isChecked()):
                pass



        SI.ShowBGRAPic(SI.showCvImg[0], SI.ui.labelShowImg)
        SI.PrintSimpleImgInfo(SI.showCvImg[0],SI.ui.labelShowImg)

    def showDarkAndLightValue(self,label,slider):
        label.setText(str(slider.value()))

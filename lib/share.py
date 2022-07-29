from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from PySide2.QtGui import QPixmap ,QImage, QIcon
import cv2
import numpy as np

class SI:

    cvImg = None
    showCvImg = []
    oriCvW = 0
    oriCvH = 0
    showCvW = None
    showCvH = None
    historyFilePath = []
    historyProcessing = []
    imgChannel = 0

    RESIZE = 100
    GRAYSCALE = 101
    DRAWEDGE = 102
    cSamW = 40
    cSamH = 40
    colorSample = np.zeros((cSamW,cSamH,3))
    colorrgbSample = np.zeros((cSamW,cSamH,3))



    def __init__(self):
        self.cvImg = None
        self.showCvImg = []
        self.oriCvW = 0
        self.oriCvH = 0
        self.showCvW = None
        self.showCvH = None

        self.historyFilePath = []

    def createSampleImg(self):
        img = np.zeros((3,3,3))


    def InitImg(self):
        self.cvImg = cv2.imread("./InitImg.png")
        self.showCvImg.insert(0,self.cvImg)
        self.showCvImg.insert(0, self.cvImg)
        self.oriCvW = self.showCvW = self.cvImg.shape[1]
        self.oriCvH = self.showCvH = self.cvImg.shape[0]


    def ShowPic(cvImg, label):
        cvImg = cv2.cvtColor(cvImg,cv2.COLOR_BGR2RGB)
        #print(type(cvImg))
        showImg = QImage(cvImg.data, cvImg.shape[1], cvImg.shape[0],cvImg.shape[1]*3, QImage.Format_RGB888)

        #   5.在PYQT5显示，需要转化为QPixmap格式
        label.setPixmap(QPixmap.fromImage(showImg))

    def ShowGrayPic(cvImg, label):
        #print(cvImg.shape)
        showImg = QImage(cvImg.data, cvImg.shape[1], cvImg.shape[0], cvImg.shape[1], QImage.Format_Grayscale8)
        label.setPixmap(QPixmap.fromImage(showImg))

    def ShowBGRAPic(cvImg,label):
        showImg = cv2.cvtColor(cvImg,cv2.COLOR_BGR2RGBA)
        showImg = QImage(cvImg.data, cvImg.shape[1], cvImg.shape[0], cvImg.shape[1]*4,QImage.Format_ARGB32)
        label.setPixmap(QPixmap.fromImage(showImg))
        print("Show RGBA Image")

    def ShowResizePic(npImg,w,h,label):
        showImg = cv2.resize(npImg,w,h)
        qImg = QImage(showImg, SI.cSamW, SI.cSamH, SI.cSamW*8, QImage.Format_RGB888)
        label.setPixmap(QPixmap.fromImage(qImg))

    def showIcon(npImg,container):
        img = QImage(npImg, SI.cSamW, SI.cSamH, SI.cSamW * 8, QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        container.setIcon(QIcon(pix))


    def PrintSimpleImgInfo(cvImg , label):
        try:
            SI.imgChannel = cvImg.shape[2]
        except IndexError:
            SI.imgChannel = 1
        SI.ui.labelShowImgInfo.setText("Size:%dx%d Channel:%d" % (SI.showCvW, SI.showCvH,SI.imgChannel))
    #测试工具
    def print_img_txt(img):
        i = 0
        j = 0
        k = 0
        file = open("img.txt", 'w')
        print(img.shape)
        try:
            channel = img.shape[2]
        except IndexError:
            channel = 1
        while i < img.shape[0]:
            while j < img.shape[1]:
                file.write(str(img[i][j]))
                j += 1
            file.write('\n')
            j = 0
            i += 1
        file.close()

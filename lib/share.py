from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from PySide2.QtGui import QPixmap ,QImage, QIcon, QMouseEvent
import cv2
import numpy as np

class SI:
    cvImg = None
    processingImgQueue = []
    historyFilePath = []
    oriW = 0
    oriH = 0
    curW = None
    curH = None
    imgChannel = 0

    RESIZE = 100
    GRAYSCALE = 101
    DRAWEDGE = 102
    cSamW = 40
    cSamH = 40

    colorSample = np.zeros((cSamW,cSamH,3))
    colorRGBSample = np.zeros((cSamW,cSamH,3))

    def __init__(self):
        self.cvImg = None
        self.processingImgQueue = []
        self.oriW = 0
        self.oriH = 0
        self.curW = None
        self.curH = None
        self.historyFilePath = []

    @classmethod
    def InitImg(cls):
        cls.cvImg = cv2.imread("./InitImg.png")
        cls.processingImgQueue.insert(0,cls.cvImg)
        cls.processingImgQueue.insert(0, cls.cvImg)
        cls.oriW = cls.curW = cls.cvImg.shape[1]
        cls.oriH = cls.curH = cls.cvImg.shape[0]

    @staticmethod
    def ShowBGRPic(cvImg, label):
        cvImg = cv2.cvtColor(cvImg,cv2.COLOR_BGR2RGB)
        showImg = QImage(cvImg.data, cvImg.shape[1], cvImg.shape[0],cvImg.shape[1]*3, QImage.Format_RGB888)
        #在PYQT5显示，需要转化为QPixmap格式
        label.setPixmap(QPixmap.fromImage(showImg))

    @staticmethod
    def ShowGrayPic(cvImg, label):
        showImg = QImage(cvImg.data, cvImg.shape[1], cvImg.shape[0], cvImg.shape[1], QImage.Format_Grayscale8)
        label.setPixmap(QPixmap.fromImage(showImg))

    @staticmethod
    def ShowBGRAPic(cvImg,label):
        showImg = cv2.cvtColor(cvImg,cv2.COLOR_BGR2RGBA)
        showImg = QImage(cvImg.data, cvImg.shape[1], cvImg.shape[0], cvImg.shape[1]*4,QImage.Format_ARGB32)
        label.setPixmap(QPixmap.fromImage(showImg))
        print("Show RGBA Image")

    @staticmethod
    def PrintSimpleImgInfo(cvImg , label):
        SI.imgChannel = SI.returnChannelNum(SI.processingImgQueue[0])
        SI.ui.labelShowImgInfo.setText("Size:%dx%d Channel:%d" % (SI.curW, SI.curH,SI.imgChannel))

    @staticmethod
    def returnChannelNum(cvImg):
        try:
            imgChannel = cvImg.shape[2]
        except IndexError:
            imgChannel = 1
        return imgChannel

    @staticmethod
    def returnImgType(cvImg):
        if(cvImg.dtype == "uint8"):
            channelNum = SI.returnChannelNum(cvImg)
            if(channelNum == 4):
                return "ABGR32"
            elif(channelNum == 3):
                return "BGR888"
            elif(channelNum == 1):
                return "GrayScale"

    @staticmethod
    def returnColorDepth(cvImg):
        if(cvImg.dtype == "uint8"):
            channelNum = SI.returnChannelNum(cvImg)
            return channelNum*8

    #测试工具
    @staticmethod
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

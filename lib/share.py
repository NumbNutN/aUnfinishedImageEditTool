from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from PySide2.QtGui import QPixmap ,QImage
import cv2

class SI:
    def __init__(self):
        self.cvImg = None
        self.showCvImg = None
        self.oriCvW = 0
        self.oriCvH = 0
        self.showCvW = None
        self.showCvH = None

        self.historyFilePath = []

    def InitImg(self):
        self.cvImg = self.showCvImg = cv2.imread("./InitImg.png")
        self.oriCvW = self.showCvW = self.cvImg.shape[1]
        self.oriCvH = self.showCvH = self.cvImg.shape[0]


    def ShowPic(cvImg, label):
        showImg = QImage(cvImg.data, cvImg.shape[1], cvImg.shape[0],cvImg.shape[1]*3, QImage.Format_RGB888)
        #   5.在PYQT5显示，需要转化为QPixmap格式
        label.setPixmap(QPixmap.fromImage(showImg))
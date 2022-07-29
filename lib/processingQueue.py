from lib.share import SI
import cv2
import numpy as np
from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider, QListWidgetItem, QAbstractScrollArea
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from lib.ui_ProcessingQueue import Ui_ProcessingQueue

class ProcessingQueue:

    previewImgLabel = []
    EmptyNotice = None

    def __init__(self):
        qfile_processingQueue_stats = QFile("./ProcessingQueue.ui")
        qfile_processingQueue_stats.open(QFile.ReadOnly)
        qfile_processingQueue_stats.close()
        SI.processingQueueUI = QUiLoader().load(qfile_processingQueue_stats)

        #SI.ui.actionViewProcessingQueue.triggered.connect(self.LoadProcessingImg)
        SI.processingQueueUI.btnBack.clicked.connect(self.quitProcessingQueue)

    def LoadProcessingImg(self):
        SI.processingQueueUI.show()

        if not SI.showCvImg:
            self.EmptyNotice = QLabel(SI.processingQueueUI)
            SI.processingQueueUI.vLayoutProcessingQueue.addWidget(self.EmptyNotice)
            self.EmptyNotice.setText("当前操作队列中没有保存的操作")

        for img in SI.showCvImg:
            widget = QLabel(SI.processingQueueUI)
            self.previewImgLabel.append(widget)
            SI.processingQueueUI.vLayoutProcessingQueue.addWidget(widget)
            SI.ShowPic(cv2.resize(img,(200,int(200/img.shape[1]*img.shape[0]))),widget)

        #Qicon方案废案
        #把addChildWidget改成addWidget就好了？？？
        #SI.processingQueueUI.vLayoutProcessingQueue.addWidget(widget)
        #widget = QListWidgetItem()
        #SI.processingQueueUI.listPreviewImg.addItem(widget)
        #SI.showIcon(img,self.previewImg[-1])

        #抽象滚动页面 不会用
        #QAbstractScrollArea(SI.processingQueueUI.vLayoutProcessingQueue)

    def quitProcessingQueue(self):
        if self.EmptyNotice:
            self.EmptyNotice.deleteLater()

        for label in self.previewImg:
            label.deleteLater()
        SI.processingQueueUI.hide()



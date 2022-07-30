from lib.share import SI
import cv2
import numpy as np
#from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider, QListWidgetItem, QAbstractScrollArea
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from lib.ui_ProcessingQueue import Ui_ProcessingQueue


class ExitQLable(QLabel):
    def __init__(self,label):
        self.label = label
        super().__init__()

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == Qt.LeftButton:
            print(ProcessingQueue.previewImgLabel)
            for index in range(len(ProcessingQueue.previewImgLabel)):
                print(ProcessingQueue.previewImgLabel[index] == self)
                print("self:" + str(self))
                print("List:"+str(ProcessingQueue.previewImgLabel[index]))

                if(ProcessingQueue.previewImgLabel[index] == self):
                    SI.ShowPic(SI.processingImgQueue[index],self.label)
                    print(index)
                    break
        print("click previous precessing img")

    def enterEvent(self, QMouseEvent):  ##鼠标停留
        self.setToolTip("关闭")  ##停留气泡



class ProcessingQueue(QWidget,Ui_ProcessingQueue):

    previewImgLabel = []
    EmptyNotice = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        SI.ui.actionViewProcessingQueue.triggered.connect(self.LoadProcessingImg)
        self.btnBack.clicked.connect(self.quitProcessingQueue)


    def closeEvent(self, event):
        self.quitProcessingQueue()


    def LoadProcessingImg(self):
        '''
        这个函数加载一个新的pyside2 widget页面
        将SI.processingImgQueue列表里面的图片按先后顺序展示在该页面上
        函数会创建和SI.processingImgQueue长度等量的label来展示图片（最多10个）
        创建label的函数QLabel被继承重写其单击触发事件来实现选择图片的功能
        :return: None
        '''
        self.show()

        if not SI.processingImgQueue:
            self.EmptyNotice = QLabel(self)
            self.vLayoutProcessingQueue.addWidget(self.EmptyNotice)
            self.EmptyNotice.setText("当前操作队列中没有保存的操作")

        for img in SI.processingImgQueue:
            #重写的方法
            widget = ExitQLable(self.labelPreviewImg)

            self.previewImgLabel.append(widget)
            self.vLayoutProcessingQueue.addWidget(widget)
            SI.ShowPic(cv2.resize(img,(200,int(200/img.shape[1]*img.shape[0]))),widget)
        print(self.previewImgLabel)

        #Qicon方案废案
        #把addChildWidget改成addWidget就好了？？？
        #self.vLayoutProcessingQueue.addWidget(widget)
        #widget = QListWidgetItem()
        #self.listPreviewImg.addItem(widget)
        #SI.showIcon(img,self.previewImg[-1])

        #抽象滚动页面 不会用
        #QAbstractScrollArea(self.vLayoutProcessingQueue)

    def quitProcessingQueue(self):
        if self.EmptyNotice:
            self.EmptyNotice.deleteLater()
        self.EmptyNotice = None

        #最后保留的方案，每次打开该页面都重新动态加载一遍ui的py文件来彻底丢弃僵尸控件，就是不知道它们还在不在内存里
        self.setupUi(self)
        SI.ui.actionViewProcessingQueue.triggered.connect(self.LoadProcessingImg)
        self.btnBack.clicked.connect(self.quitProcessingQueue)

        #对控件的清除回收总是会遇到某种错误，页面上已经不显示deletelater()处理的控件，但鼠标左键触发事件的触发主体依然是被删除的控件导致报错

        # for label in self.previewImgLabel:
        #     self.vLayoutProcessingQueue.removeWidget(label)
        #     label.clear()
        #     label.deleteLater()
        # self.labelPreviewImg.setText("大图在这里")
        # self.previewImgLabel = []
        #self.hide()



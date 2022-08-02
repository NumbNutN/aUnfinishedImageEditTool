import numpy as np
from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from PySide2.QtGui import QPixmap ,QImage
import cv2
from lib.share import SI
from lib.resize import Resize
from lib.transparent import Transparent
from lib.processingQueue import ProcessingQueue
from lib.edgeDetection import EdgeDetection
from lib.fileManage import FIleMenu






class TabWidget:
    def __init__(self):
        SI.ui.tabWidgetFunction.currentChanged.connect(self.TabChange)

    def TabChange(self):
        print(SI.ui.tabWidgetFunction.currentIndex())
        if not(np.array_equal(SI.processingImgQueue[0],SI.processingImgQueue[1])):
            SI.processingImgQueue.insert(0,SI.processingImgQueue[0])
        print("Image Edit Stack: "+str(len(SI.processingImgQueue)))
        SI.ShowBGRPic(SI.processingImgQueue[0],SI.ui.labelImgViewpot)
        SI.advancedinfo.InfoRefresh()


class GrayScale:
    def __init__(self):
        SI.ui.cboxCvtToGrayScale.stateChanged.connect(self.TranToGrayScal)

    def TranToGrayScal(self):
        if (SI.ui.cboxCvtToGrayScale.isChecked()):
            SI.processingImgQueue[0] = cv2.cvtColor(SI.processingImgQueue[1],cv2.COLOR_BGR2GRAY)
            SI.ShowGrayPic(SI.processingImgQueue[0],SI.ui.labelImgViewpot)
            print("ConvertToGrayScale")
        else:
            SI.processingImgQueue[0] = SI.processingImgQueue[1]
            SI.ShowBGRPic(SI.processingImgQueue[0], SI.ui.labelImgViewpot)
            print("ReturnToColor")
        SI.PrintSimpleImgInfo(SI.processingImgQueue[0], SI.ui.labelShowImgInfo)


class AdvancedInfo:
    def __init__(self):
        pass

    def InfoRefresh(self):
        SI.ui.textBrowser.setText(
        "当前图像属性：\n"\
        "图片尺寸: %dx%d\t"\
        "通道数: %d\n"\
        "图片类型: %s\t"\
        "位深度: %d\n"\
        "----------------------\n"\
        "状态：\n"\
        "图片处理历史队列数: %d\n"
             % (SI.curW, SI.curH,SI.imgChannel,SI.returnImgType(SI.processingImgQueue[0]),SI.returnColorDepth(SI.processingImgQueue[0]),len(SI.processingImgQueue)))

app = QApplication([])

qfile_stats = QFile("main.ui")
qfile_stats.open(QFile.ReadOnly)
qfile_stats.close()
SI.ui = QUiLoader().load(qfile_stats)
SI.InitImg()
SI.ShowBGRPic(SI.processingImgQueue[0],SI.ui.labelImgViewpot)


SI.fileMenu = FIleMenu()
SI.resize = Resize()
SI.tabwidget = TabWidget()
SI.advancedinfo = AdvancedInfo()
SI.grayscale = GrayScale()
SI.edgedetection = EdgeDetection()
SI.transparent = Transparent()
SI.processingqueue = ProcessingQueue()

SI.ui.show()
app.exec_()
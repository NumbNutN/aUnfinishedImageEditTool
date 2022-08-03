import numpy as np
#from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtWidgets import *
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
from ui.ui_MainWindow import Ui_MainWindow


class TabWidget:
    '''
    这个类负责实现用户在各个tab之间切换的时候历史图像处理队列的改变逻辑

    大致的功能预期：
    当用户切换tab页面时图像处理队列会更新，生成一个当前队头(head)的深拷贝插入队列，作为SI.processingQueue[0]，（新队头）
    需要考虑以下情况：
    - 1.假如用户上一次切换tab没有进行任何图像处理，切换tab更新队列会导致队列记录了重复的图像信息，浪费队列存量，且更可能覆盖有效的历史操作
        这种情况切换前SI.processingQueue[0]和SI.processingQueue[1]的值是相等的
        TabChange()函数在每一次tab切换事件触发时判断这种情况，此时队列将不会更新
    '''
    def __init__(self):
        '''
        为主窗口tab控件切换事件添加槽函数
        '''
        SI.mainWindow.tabWidgetFunction.currentChanged.connect(self.TabChange)

    def TabChange(self):
        print(SI.mainWindow.tabWidgetFunction.currentIndex())
        if not(np.array_equal(SI.processingImgQueue[0],SI.processingImgQueue[1])):
            SI.processingImgQueue.insert(0,SI.processingImgQueue[0])
        print("Image Edit Stack: "+str(len(SI.processingImgQueue)))
        SI.ShowBGRPic(SI.processingImgQueue[0],SI.mainWindow.labelImgViewpot)
        SI.advancedinfo.InfoRefresh()


class GrayScale:
    '''
    这个类负责实现把当前显示图片转化为灰度图的tab控件
    '''
    def __init__(self):
        SI.mainWindow.cboxCvtToGrayScale.stateChanged.connect(self.TranToGrayScal)

    def TranToGrayScal(self):
        if (SI.mainWindow.cboxCvtToGrayScale.isChecked()):
            SI.processingImgQueue[0] = cv2.cvtColor(SI.processingImgQueue[1],cv2.COLOR_BGR2GRAY)
            SI.ShowGrayPic(SI.processingImgQueue[0],SI.mainWindow.labelImgViewpot)
            print("ConvertToGrayScale")
        else:
            SI.processingImgQueue[0] = SI.processingImgQueue[1]
            SI.ShowBGRPic(SI.processingImgQueue[0], SI.mainWindow.labelImgViewpot)
            print("ReturnToColor")
        SI.PrintSimpleImgInfo(SI.processingImgQueue[0], SI.mainWindow.labelShowImgInfo)


class AdvancedInfo:
    '''
    这个方法类负责打印当前图片各项属性的tab控件的实现
    '''
    def __init__(self):
        pass

    def InfoRefresh(self):
        SI.mainWindow.textBrowser.setText(
        "当前图像属性：\n"\
        "图片尺寸: %dx%d\t"\
        "通道数: %d\n"\
        "图片类型: %s\t"\
        "位深度: %d\n"\
        "----------------------\n"\
        "状态：\n"\
        "图片处理历史队列数: %d\n"
             % (SI.curW, SI.curH,SI.imgChannel,SI.returnImgType(SI.processingImgQueue[0]),SI.returnColorDepth(SI.processingImgQueue[0]),len(SI.processingImgQueue)))


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

'''
 这是之前读取.ui文件的代码实现
 这里的弊端是ui页面里所有的可视化控件在代码中都是隐式的
 python编译器将无法探测到任何一个控件也无法给出有效的代码自动补全方案
'''

# qfile_stats = QFile("main.ui")
# qfile_stats.open(QFile.ReadOnly)
# qfile_stats.close()
# SI.mainWindow = QUiLoader().load(qfile_stats)

app = QApplication([])
SI.mainWindow = MainWindow()
SI.mainWindow.show()
SI.InitImg()
SI.ShowBGRPic(SI.processingImgQueue[0],SI.mainWindow.labelImgViewpot)

#初始化文件管理菜单
SI.fileMenu = FIleMenu()
#初始化tab控件切换功能
SI.tabwidget = TabWidget()
#初始化图像尺寸调整功能
SI.resize = Resize()
#初始化高级信息展示功能
SI.advancedinfo = AdvancedInfo()
#初始化灰度图转化功能
SI.grayscale = GrayScale()
#初始化边缘检测功能
SI.edgedetection = EdgeDetection()
#初始化透明度转化功能
SI.transparent = Transparent()
'''
初始化历史图像回退功能
这个功能没有实现好！！！
'''
SI.processingqueue = ProcessingQueue()

#展示pyside2主窗口
SI.mainWindow.show()
#直到窗口退出，循环执行
app.exec_()
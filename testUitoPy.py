from lib.share import SI
import cv2
import numpy as np
from PySide2.QtWidgets import QApplication ,QMessageBox ,QTableWidgetItem ,QFileDialog ,QLabel ,QSlider
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *

qfile_processingQueue_stats = QFile("./ProcessingQueue.ui")
qfile_processingQueue_stats.open(QFile.ReadOnly)
qfile_processingQueue_stats.close()
UI = QUiLoader().load(qfile_processingQueue_stats)
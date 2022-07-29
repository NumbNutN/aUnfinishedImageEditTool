# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProcessingQueueJcvQtG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ProcessingQueue(object):
    def setupUi(self, ProcessingQueue):
        if not ProcessingQueue.objectName():
            ProcessingQueue.setObjectName(u"ProcessingQueue")
        ProcessingQueue.resize(509, 423)
        self.horizontalLayout = QHBoxLayout(ProcessingQueue)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vLayoutProcessingQueue = QVBoxLayout()
        self.vLayoutProcessingQueue.setObjectName(u"vLayoutProcessingQueue")
        self.label = QLabel(ProcessingQueue)
        self.label.setObjectName(u"label")

        self.vLayoutProcessingQueue.addWidget(self.label)


        self.horizontalLayout.addLayout(self.vLayoutProcessingQueue)

        self.line = QFrame(ProcessingQueue)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelPreviewImg = QLabel(ProcessingQueue)
        self.labelPreviewImg.setObjectName(u"labelPreviewImg")

        self.verticalLayout_2.addWidget(self.labelPreviewImg)

        self.labelPreviewInfo = QLabel(ProcessingQueue)
        self.labelPreviewInfo.setObjectName(u"labelPreviewInfo")

        self.verticalLayout_2.addWidget(self.labelPreviewInfo)

        self.btnBack = QPushButton(ProcessingQueue)
        self.btnBack.setObjectName(u"btnBack")

        self.verticalLayout_2.addWidget(self.btnBack)

        self.verticalLayout_2.setStretch(0, 9)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(ProcessingQueue)

        QMetaObject.connectSlotsByName(ProcessingQueue)
    # setupUi

    def retranslateUi(self, ProcessingQueue):
        ProcessingQueue.setWindowTitle(QCoreApplication.translate("ProcessingQueue", u"ProcessingQueue", None))
        self.label.setText(QCoreApplication.translate("ProcessingQueue", u"\u64cd\u4f5c\u961f\u5217", None))
        self.labelPreviewImg.setText(QCoreApplication.translate("ProcessingQueue", u"\u5927\u56fe\u5728\u8fd9\u91cc", None))
        self.labelPreviewInfo.setText(QCoreApplication.translate("ProcessingQueue", u"\u4fe1\u606f\u5728\u8fd9\u91cc", None))
        self.btnBack.setText(QCoreApplication.translate("ProcessingQueue", u"\u56de\u9000", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HistoryFilelBEcQd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_historyFile(object):
    def setupUi(self, historyFile):
        if not historyFile.objectName():
            historyFile.setObjectName(u"historyFile")
        historyFile.resize(600, 400)
        self.horizontalLayout = QHBoxLayout(historyFile)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listHistoryFile = QListWidget(historyFile)
        self.listHistoryFile.setObjectName(u"listHistoryFile")

        self.horizontalLayout.addWidget(self.listHistoryFile)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelHistoryPreview = QLabel(historyFile)
        self.labelHistoryPreview.setObjectName(u"labelHistoryPreview")

        self.verticalLayout.addWidget(self.labelHistoryPreview)

        self.labelPreviewInfo = QLabel(historyFile)
        self.labelPreviewInfo.setObjectName(u"labelPreviewInfo")

        self.verticalLayout.addWidget(self.labelPreviewInfo)

        self.btnVerifyHistoryFile = QPushButton(historyFile)
        self.btnVerifyHistoryFile.setObjectName(u"btnVerifyHistoryFile")

        self.verticalLayout.addWidget(self.btnVerifyHistoryFile)

        self.verticalLayout.setStretch(0, 9)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)

        self.retranslateUi(historyFile)

        QMetaObject.connectSlotsByName(historyFile)
    # setupUi

    def retranslateUi(self, historyFile):
        historyFile.setWindowTitle(QCoreApplication.translate("historyFile", u"HistoryFiles", None))
        self.labelHistoryPreview.setText(QCoreApplication.translate("historyFile", u"\u56fe\u7247\u5728\u8fd9\u91cc", None))
        self.labelPreviewInfo.setText(QCoreApplication.translate("historyFile", u"\u4fe1\u606f\u5728\u8fd9\u91cc", None))
        self.btnVerifyHistoryFile.setText(QCoreApplication.translate("historyFile", u"\u6253\u5f00", None))
    # retranslateUi


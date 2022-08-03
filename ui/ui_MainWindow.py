# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowQmVJXi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(616, 449)
        self.fileOpenAction = QAction(MainWindow)
        self.fileOpenAction.setObjectName(u"fileOpenAction")
        self.saveAsAction = QAction(MainWindow)
        self.saveAsAction.setObjectName(u"saveAsAction")
        self.recentFileAction = QAction(MainWindow)
        self.recentFileAction.setObjectName(u"recentFileAction")
        self.actionBack = QAction(MainWindow)
        self.actionBack.setObjectName(u"actionBack")
        self.convertToGrayScaleAction = QAction(MainWindow)
        self.convertToGrayScaleAction.setObjectName(u"convertToGrayScaleAction")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.cleanHistoryAction = QAction(MainWindow)
        self.cleanHistoryAction.setObjectName(u"cleanHistoryAction")
        self.actionViewProcessingQueue = QAction(MainWindow)
        self.actionViewProcessingQueue.setObjectName(u"actionViewProcessingQueue")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidgetFunction = QTabWidget(self.centralwidget)
        self.tabWidgetFunction.setObjectName(u"tabWidgetFunction")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidgetFunction.sizePolicy().hasHeightForWidth())
        self.tabWidgetFunction.setSizePolicy(sizePolicy)
        self.tabGrayscale = QWidget()
        self.tabGrayscale.setObjectName(u"tabGrayscale")
        self.verticalLayout_10 = QVBoxLayout(self.tabGrayscale)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.cboxCvtToGrayScale = QCheckBox(self.tabGrayscale)
        self.cboxCvtToGrayScale.setObjectName(u"cboxCvtToGrayScale")

        self.verticalLayout_6.addWidget(self.cboxCvtToGrayScale)


        self.verticalLayout_10.addLayout(self.verticalLayout_6)

        self.tabWidgetFunction.addTab(self.tabGrayscale, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_17 = QVBoxLayout(self.tab_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.cBoxCvtMargin = QCheckBox(self.tab_2)
        self.cBoxCvtMargin.setObjectName(u"cBoxCvtMargin")

        self.verticalLayout_16.addWidget(self.cBoxCvtMargin)

        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.rBtnSobel = QRadioButton(self.groupBox_2)
        self.bGroupEdgeMethod = QButtonGroup(MainWindow)
        self.bGroupEdgeMethod.setObjectName(u"bGroupEdgeMethod")
        self.bGroupEdgeMethod.addButton(self.rBtnSobel)
        self.rBtnSobel.setObjectName(u"rBtnSobel")

        self.verticalLayout_11.addWidget(self.rBtnSobel)

        self.rBtnCanny = QRadioButton(self.groupBox_2)
        self.bGroupEdgeMethod.addButton(self.rBtnCanny)
        self.rBtnCanny.setObjectName(u"rBtnCanny")

        self.verticalLayout_11.addWidget(self.rBtnCanny)


        self.verticalLayout_16.addWidget(self.groupBox_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_16)

        self.line_2 = QFrame(self.tab_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_2)

        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.rbtnRow = QRadioButton(self.groupBox)
        self.bGroupMarginBackground = QButtonGroup(MainWindow)
        self.bGroupMarginBackground.setObjectName(u"bGroupMarginBackground")
        self.bGroupMarginBackground.addButton(self.rbtnRow)
        self.rbtnRow.setObjectName(u"rbtnRow")

        self.verticalLayout_7.addWidget(self.rbtnRow)

        self.rbtnFilm = QRadioButton(self.groupBox)
        self.bGroupMarginBackground.addButton(self.rbtnFilm)
        self.rbtnFilm.setObjectName(u"rbtnFilm")

        self.verticalLayout_7.addWidget(self.rbtnFilm)


        self.horizontalLayout_8.addWidget(self.groupBox)

        self.horizontalLayout_8.setStretch(0, 9)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 2)

        self.verticalLayout_17.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.sliderMarginAdjustStrength = QSlider(self.tab_2)
        self.sliderMarginAdjustStrength.setObjectName(u"sliderMarginAdjustStrength")
        self.sliderMarginAdjustStrength.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.sliderMarginAdjustStrength)

        self.labelEdgeStrength = QLabel(self.tab_2)
        self.labelEdgeStrength.setObjectName(u"labelEdgeStrength")

        self.horizontalLayout_9.addWidget(self.labelEdgeStrength)


        self.verticalLayout_17.addLayout(self.horizontalLayout_9)

        self.tabWidgetFunction.addTab(self.tab_2, "")
        self.tabResize = QWidget()
        self.tabResize.setObjectName(u"tabResize")
        self.horizontalLayout = QHBoxLayout(self.tabResize)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.tabResize)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.label_7 = QLabel(self.tabResize)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)


        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sliderW = QSlider(self.tabResize)
        self.sliderW.setObjectName(u"sliderW")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sliderW.sizePolicy().hasHeightForWidth())
        self.sliderW.setSizePolicy(sizePolicy1)
        self.sliderW.setOrientation(Qt.Horizontal)

        self.verticalLayout_13.addWidget(self.sliderW)

        self.labelSliderWInfo = QLabel(self.tabResize)
        self.labelSliderWInfo.setObjectName(u"labelSliderWInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelSliderWInfo.sizePolicy().hasHeightForWidth())
        self.labelSliderWInfo.setSizePolicy(sizePolicy2)

        self.verticalLayout_13.addWidget(self.labelSliderWInfo)

        self.sliderH = QSlider(self.tabResize)
        self.sliderH.setObjectName(u"sliderH")
        sizePolicy1.setHeightForWidth(self.sliderH.sizePolicy().hasHeightForWidth())
        self.sliderH.setSizePolicy(sizePolicy1)
        self.sliderH.setOrientation(Qt.Horizontal)

        self.verticalLayout_13.addWidget(self.sliderH)

        self.labelSliderHInfo = QLabel(self.tabResize)
        self.labelSliderHInfo.setObjectName(u"labelSliderHInfo")
        sizePolicy2.setHeightForWidth(self.labelSliderHInfo.sizePolicy().hasHeightForWidth())
        self.labelSliderHInfo.setSizePolicy(sizePolicy2)

        self.verticalLayout_13.addWidget(self.labelSliderHInfo)

        self.verticalLayout_13.setStretch(1, 1)
        self.verticalLayout_13.setStretch(3, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_13)

        self.groupFixedRatio = QGroupBox(self.tabResize)
        self.groupFixedRatio.setObjectName(u"groupFixedRatio")
        self.horizontalLayout_7 = QHBoxLayout(self.groupFixedRatio)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.cboxFixedRatio = QCheckBox(self.groupFixedRatio)
        self.cboxFixedRatio.setObjectName(u"cboxFixedRatio")

        self.horizontalLayout_7.addWidget(self.cboxFixedRatio)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.rbtnResizePixel = QRadioButton(self.groupFixedRatio)
        self.bGroupRatioOrNot = QButtonGroup(MainWindow)
        self.bGroupRatioOrNot.setObjectName(u"bGroupRatioOrNot")
        self.bGroupRatioOrNot.addButton(self.rbtnResizePixel)
        self.rbtnResizePixel.setObjectName(u"rbtnResizePixel")

        self.verticalLayout_14.addWidget(self.rbtnResizePixel)

        self.rbtnResizePresentage = QRadioButton(self.groupFixedRatio)
        self.bGroupRatioOrNot.addButton(self.rbtnResizePresentage)
        self.rbtnResizePresentage.setObjectName(u"rbtnResizePresentage")

        self.verticalLayout_14.addWidget(self.rbtnResizePresentage)


        self.horizontalLayout_7.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label = QLabel(self.groupFixedRatio)
        self.label.setObjectName(u"label")

        self.verticalLayout_15.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sBoxResizeW = QSpinBox(self.groupFixedRatio)
        self.sBoxResizeW.setObjectName(u"sBoxResizeW")

        self.horizontalLayout_2.addWidget(self.sBoxResizeW)

        self.labelResizeWUnit = QLabel(self.groupFixedRatio)
        self.labelResizeWUnit.setObjectName(u"labelResizeWUnit")

        self.horizontalLayout_2.addWidget(self.labelResizeWUnit)


        self.verticalLayout_15.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sBoxResizeH = QSpinBox(self.groupFixedRatio)
        self.sBoxResizeH.setObjectName(u"sBoxResizeH")

        self.horizontalLayout_6.addWidget(self.sBoxResizeH)

        self.labelResizeHUnit = QLabel(self.groupFixedRatio)
        self.labelResizeHUnit.setObjectName(u"labelResizeHUnit")

        self.horizontalLayout_6.addWidget(self.labelResizeHUnit)


        self.verticalLayout_15.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_15)

        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 3)

        self.horizontalLayout.addWidget(self.groupFixedRatio)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.tabWidgetFunction.addTab(self.tabResize, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_16 = QHBoxLayout(self.tab)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_19.addWidget(self.label_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.cBoxLight = QCheckBox(self.tab)
        self.cBoxLight.setObjectName(u"cBoxLight")

        self.horizontalLayout_5.addWidget(self.cBoxLight)

        self.labelLightSample = QLabel(self.tab)
        self.labelLightSample.setObjectName(u"labelLightSample")
        self.labelLightSample.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.labelLightSample)

        self.sliderLight = QSlider(self.tab)
        self.sliderLight.setObjectName(u"sliderLight")
        self.sliderLight.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.sliderLight)

        self.labelLightValue = QLabel(self.tab)
        self.labelLightValue.setObjectName(u"labelLightValue")

        self.horizontalLayout_5.addWidget(self.labelLightValue)


        self.verticalLayout_19.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.cBoxDark = QCheckBox(self.tab)
        self.cBoxDark.setObjectName(u"cBoxDark")

        self.horizontalLayout_3.addWidget(self.cBoxDark)

        self.labelDarkSample = QLabel(self.tab)
        self.labelDarkSample.setObjectName(u"labelDarkSample")
        self.labelDarkSample.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.labelDarkSample)

        self.sliderDark = QSlider(self.tab)
        self.sliderDark.setObjectName(u"sliderDark")
        self.sliderDark.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.sliderDark)

        self.labelDarkValue = QLabel(self.tab)
        self.labelDarkValue.setObjectName(u"labelDarkValue")

        self.horizontalLayout_3.addWidget(self.labelDarkValue)


        self.verticalLayout_19.addLayout(self.horizontalLayout_3)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_19.addWidget(self.label_9)


        self.horizontalLayout_16.addLayout(self.verticalLayout_19)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_18.addWidget(self.label_2)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)


        self.horizontalLayout_15.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cBoxColorHigh = QCheckBox(self.tab)
        self.cBoxColorHigh.setObjectName(u"cBoxColorHigh")

        self.verticalLayout.addWidget(self.cBoxColorHigh)

        self.labelCHighSample = QLabel(self.tab)
        self.labelCHighSample.setObjectName(u"labelCHighSample")
        self.labelCHighSample.setMinimumSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.labelCHighSample)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 5)

        self.horizontalLayout_15.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelRHighSample = QLabel(self.tab)
        self.labelRHighSample.setObjectName(u"labelRHighSample")
        self.labelRHighSample.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.labelRHighSample)

        self.sliderRHigh = QSlider(self.tab)
        self.sliderRHigh.setObjectName(u"sliderRHigh")
        self.sliderRHigh.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.sliderRHigh)

        self.labelRHighValue = QLabel(self.tab)
        self.labelRHighValue.setObjectName(u"labelRHighValue")

        self.horizontalLayout_4.addWidget(self.labelRHighValue)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.labelGHighSample = QLabel(self.tab)
        self.labelGHighSample.setObjectName(u"labelGHighSample")
        self.labelGHighSample.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_10.addWidget(self.labelGHighSample)

        self.sliderGHigh = QSlider(self.tab)
        self.sliderGHigh.setObjectName(u"sliderGHigh")
        self.sliderGHigh.setOrientation(Qt.Horizontal)

        self.horizontalLayout_10.addWidget(self.sliderGHigh)

        self.labelGHighValue = QLabel(self.tab)
        self.labelGHighValue.setObjectName(u"labelGHighValue")

        self.horizontalLayout_10.addWidget(self.labelGHighValue)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.labelBHighSample = QLabel(self.tab)
        self.labelBHighSample.setObjectName(u"labelBHighSample")
        self.labelBHighSample.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.labelBHighSample)

        self.sliderBHigh = QSlider(self.tab)
        self.sliderBHigh.setObjectName(u"sliderBHigh")
        self.sliderBHigh.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.sliderBHigh)

        self.labelBHighValue = QLabel(self.tab)
        self.labelBHighValue.setObjectName(u"labelBHighValue")

        self.horizontalLayout_11.addWidget(self.labelBHighValue)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_15.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cBoxColorLow = QCheckBox(self.tab)
        self.cBoxColorLow.setObjectName(u"cBoxColorLow")

        self.verticalLayout_3.addWidget(self.cBoxColorLow)

        self.labelCLowSample = QLabel(self.tab)
        self.labelCLowSample.setObjectName(u"labelCLowSample")
        self.labelCLowSample.setMinimumSize(QSize(50, 50))

        self.verticalLayout_3.addWidget(self.labelCLowSample)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 5)

        self.horizontalLayout_15.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.labelRLowSample = QLabel(self.tab)
        self.labelRLowSample.setObjectName(u"labelRLowSample")
        self.labelRLowSample.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.labelRLowSample)

        self.sliderRLow = QSlider(self.tab)
        self.sliderRLow.setObjectName(u"sliderRLow")
        self.sliderRLow.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.sliderRLow)

        self.labelRLowValue = QLabel(self.tab)
        self.labelRLowValue.setObjectName(u"labelRLowValue")

        self.horizontalLayout_12.addWidget(self.labelRLowValue)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.labelGLowSample = QLabel(self.tab)
        self.labelGLowSample.setObjectName(u"labelGLowSample")
        self.labelGLowSample.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_13.addWidget(self.labelGLowSample)

        self.sliderGLow = QSlider(self.tab)
        self.sliderGLow.setObjectName(u"sliderGLow")
        self.sliderGLow.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.sliderGLow)

        self.labelGLowValue = QLabel(self.tab)
        self.labelGLowValue.setObjectName(u"labelGLowValue")

        self.horizontalLayout_13.addWidget(self.labelGLowValue)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.labelBLowSample = QLabel(self.tab)
        self.labelBLowSample.setObjectName(u"labelBLowSample")
        self.labelBLowSample.setMinimumSize(QSize(25, 25))

        self.horizontalLayout_14.addWidget(self.labelBLowSample)

        self.sliderBLow = QSlider(self.tab)
        self.sliderBLow.setObjectName(u"sliderBLow")
        self.sliderBLow.setOrientation(Qt.Horizontal)

        self.horizontalLayout_14.addWidget(self.sliderBLow)

        self.labelBLowValue = QLabel(self.tab)
        self.labelBLowValue.setObjectName(u"labelBLowValue")

        self.horizontalLayout_14.addWidget(self.labelBLowValue)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_15.addLayout(self.verticalLayout_5)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 2)
        self.horizontalLayout_15.setStretch(2, 5)
        self.horizontalLayout_15.setStretch(3, 2)
        self.horizontalLayout_15.setStretch(4, 5)

        self.verticalLayout_18.addLayout(self.horizontalLayout_15)

        self.verticalLayout_18.setStretch(0, 1)
        self.verticalLayout_18.setStretch(1, 9)

        self.horizontalLayout_16.addLayout(self.verticalLayout_18)

        self.horizontalLayout_16.setStretch(0, 10)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(2, 20)
        self.tabWidgetFunction.addTab(self.tab, "")
        self.tabImgInfo = QWidget()
        self.tabImgInfo.setObjectName(u"tabImgInfo")
        self.verticalLayout_20 = QVBoxLayout(self.tabImgInfo)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.textBrowser = QTextBrowser(self.tabImgInfo)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_20.addWidget(self.textBrowser)

        self.tabWidgetFunction.addTab(self.tabImgInfo, "")

        self.verticalLayout_9.addWidget(self.tabWidgetFunction)

        self.labelImgViewpot = QLabel(self.centralwidget)
        self.labelImgViewpot.setObjectName(u"labelImgViewpot")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelImgViewpot.sizePolicy().hasHeightForWidth())
        self.labelImgViewpot.setSizePolicy(sizePolicy3)
        self.labelImgViewpot.setMaximumSize(QSize(1920, 1080))

        self.verticalLayout_9.addWidget(self.labelImgViewpot)

        self.labelShowImgInfo = QLabel(self.centralwidget)
        self.labelShowImgInfo.setObjectName(u"labelShowImgInfo")

        self.verticalLayout_9.addWidget(self.labelShowImgInfo)

        self.saveImg = QPushButton(self.centralwidget)
        self.saveImg.setObjectName(u"saveImg")

        self.verticalLayout_9.addWidget(self.saveImg)

        self.verticalLayout_9.setStretch(1, 5)
        self.verticalLayout_9.setStretch(2, 1)
        self.verticalLayout_9.setStretch(3, 1)

        self.verticalLayout_12.addLayout(self.verticalLayout_9)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 616, 22))
        self.fileSetting = QMenu(self.menubar)
        self.fileSetting.setObjectName(u"fileSetting")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar)

        self.menubar.addAction(self.fileSetting.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.fileSetting.addAction(self.fileOpenAction)
        self.fileSetting.addAction(self.saveAsAction)
        self.fileSetting.addAction(self.recentFileAction)
        self.fileSetting.addAction(self.cleanHistoryAction)
        self.menu_2.addAction(self.actionBack)
        self.menu_2.addAction(self.actionViewProcessingQueue)
        self.toolBar.addAction(self.convertToGrayScaleAction)
        self.toolBar.addAction(self.action_4)
        self.toolBar.addAction(self.action_5)
        self.toolBar.addAction(self.action_6)

        self.retranslateUi(MainWindow)

        self.tabWidgetFunction.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fileOpenAction.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.saveAsAction.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.recentFileAction.setText(QCoreApplication.translate("MainWindow", u"\u6700\u8fd1\u6253\u5f00", None))
        self.actionBack.setText(QCoreApplication.translate("MainWindow", u"\u56de\u9000\u4e0a\u4e00\u6b65", None))
        self.convertToGrayScaleAction.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u6761", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u523b\u5f55\u65f6\u95f4\u8f74", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u77e9\u5f62", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u8272", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"\u6587\u672c", None))
        self.cleanHistoryAction.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u5386\u53f2\u6253\u5f00\u8bb0\u5f55", None))
        self.actionViewProcessingQueue.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u9605\u64cd\u4f5c\u961f\u5217", None))
        self.cboxCvtToGrayScale.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5316\u4e3a\u7070\u5ea6\u56fe", None))
        self.tabWidgetFunction.setTabText(self.tabWidgetFunction.indexOf(self.tabGrayscale), QCoreApplication.translate("MainWindow", u"\u7070\u5ea6", None))
        self.cBoxCvtMargin.setText(QCoreApplication.translate("MainWindow", u"\u52fe\u753b\u8fb9\u7f18", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
        self.rBtnSobel.setText(QCoreApplication.translate("MainWindow", u"Sobel\u7b97\u5b50\u5377\u79ef", None))
        self.rBtnCanny.setText(QCoreApplication.translate("MainWindow", u"Canny\u7b97\u6cd5", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
        self.rbtnRow.setText(QCoreApplication.translate("MainWindow", u"\u539f\u7247", None))
        self.rbtnFilm.setText(QCoreApplication.translate("MainWindow", u"\u5e95\u7247", None))
        self.labelEdgeStrength.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidgetFunction.setTabText(self.tabWidgetFunction.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u63cf\u8fb9", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5bbd Width", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u9ad8 Height", None))
        self.labelSliderWInfo.setText(QCoreApplication.translate("MainWindow", u"w", None))
        self.labelSliderHInfo.setText(QCoreApplication.translate("MainWindow", u"h", None))
        self.groupFixedRatio.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
        self.cboxFixedRatio.setText(QCoreApplication.translate("MainWindow", u"\u56fa\u5b9a\u7f29\u653e\u6bd4", None))
        self.rbtnResizePixel.setText(QCoreApplication.translate("MainWindow", u"\u50cf\u7d20", None))
        self.rbtnResizePresentage.setText(QCoreApplication.translate("MainWindow", u"\u767e\u5206\u6bd4", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49", None))
        self.labelResizeWUnit.setText(QCoreApplication.translate("MainWindow", u"Pixel", None))
        self.labelResizeHUnit.setText(QCoreApplication.translate("MainWindow", u"Pixel", None))
        self.tabWidgetFunction.setTabText(self.tabWidgetFunction.indexOf(self.tabResize), QCoreApplication.translate("MainWindow", u"\u8c03\u6574\u5c3a\u5bf8", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5c06\u50cf\u7d20\u503c\u5728\u4ee5\u4e0b\u57df\u4e2d\u8bbe\u4e3a\u900f\u660e\u8272", None))
        self.cBoxLight.setText(QCoreApplication.translate("MainWindow", u"\u4eae>", None))
        self.labelLightSample.setText(QCoreApplication.translate("MainWindow", u"\u989c\u8272", None))
        self.labelLightValue.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.cBoxDark.setText(QCoreApplication.translate("MainWindow", u"\u6697>", None))
        self.labelDarkSample.setText(QCoreApplication.translate("MainWindow", u"\u989c\u8272", None))
        self.labelDarkValue.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7801\u8bbe\u8ba1\u80fd\u529b\u6709\u9650\uff0c\u8bf7\u7528\u62d6\u52a8\u66ff\u4ee3\u8df3\u52a8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u7ea7", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.cBoxColorHigh.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u4e8e", None))
        self.labelCHighSample.setText(QCoreApplication.translate("MainWindow", u"\u989c\u8272", None))
        self.labelRHighSample.setText("")
        self.labelRHighValue.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.labelGHighSample.setText("")
        self.labelGHighValue.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.labelBHighSample.setText("")
        self.labelBHighValue.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.cBoxColorLow.setText(QCoreApplication.translate("MainWindow", u"\u4f4e\u4e8e", None))
        self.labelCLowSample.setText(QCoreApplication.translate("MainWindow", u"\u989c\u8272", None))
        self.labelRLowSample.setText("")
        self.labelRLowValue.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.labelGLowSample.setText("")
        self.labelGLowValue.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.labelBLowSample.setText("")
        self.labelBLowValue.setText(QCoreApplication.translate("MainWindow", u"value", None))
        self.tabWidgetFunction.setTabText(self.tabWidgetFunction.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u900f\u660e\u8272", None))
        self.tabWidgetFunction.setTabText(self.tabWidgetFunction.indexOf(self.tabImgInfo), QCoreApplication.translate("MainWindow", u"\u4fe1\u606f", None))
        self.labelImgViewpot.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u663e\u793a\u5728\u8fd9\u91cc", None))
        self.labelShowImgInfo.setText(QCoreApplication.translate("MainWindow", u"Size:   ", None))
        self.saveImg.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.fileSetting.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


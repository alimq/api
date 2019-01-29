# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1490, 689)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftSpace = QtWidgets.QWidget(self.centralwidget)
        self.leftSpace.setObjectName("leftSpace")
        self.horizontalLayout.addWidget(self.leftSpace)
        self.sidebar = QtWidgets.QWidget(self.centralwidget)
        self.sidebar.setMinimumSize(QtCore.QSize(250, 0))
        self.sidebar.setMaximumSize(QtCore.QSize(250, 16777215))
        self.sidebar.setAutoFillBackground(True)
        self.sidebar.setObjectName("sidebar")
        self.clearButton = QtWidgets.QPushButton(self.sidebar)
        self.clearButton.setGeometry(QtCore.QRect(20, 30, 91, 41))
        self.clearButton.setObjectName("clearButton")
        self.brushSizeSlider = QtWidgets.QSlider(self.sidebar)
        self.brushSizeSlider.setGeometry(QtCore.QRect(20, 120, 160, 22))
        self.brushSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brushSizeSlider.setObjectName("brushSizeSlider")
        self.brushSizeLabel = QtWidgets.QLabel(self.sidebar)
        self.brushSizeLabel.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.brushSizeLabel.setObjectName("brushSizeLabel")
        self.brushColorLabel = QtWidgets.QLabel(self.sidebar)
        self.brushColorLabel.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.brushColorLabel.setObjectName("brushColorLabel")
        self.brushColorButton = QtWidgets.QPushButton(self.sidebar)
        self.brushColorButton.setGeometry(QtCore.QRect(20, 190, 91, 41))
        self.brushColorButton.setObjectName("brushColorButton")
        self.horizontalLayout.addWidget(self.sidebar, 0, QtCore.Qt.AlignLeft)
        self.canvas = Canvas(self.centralwidget)
        self.canvas.setMinimumSize(QtCore.QSize(600, 600))
        self.canvas.setMaximumSize(QtCore.QSize(600, 600))
        self.canvas.setBaseSize(QtCore.QSize(600, 600))
        self.canvas.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.canvas.setAutoFillBackground(True)
        self.canvas.setStyleSheet("canvas{background-color: rgb(70, 70, 50);}")
        self.canvas.setObjectName("canvas")
        self.horizontalLayout.addWidget(self.canvas, 0, QtCore.Qt.AlignLeft)
        self.rightSpace = QtWidgets.QWidget(self.centralwidget)
        self.rightSpace.setObjectName("rightSpace")
        self.horizontalLayout.addWidget(self.rightSpace)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.toolBar.addAction(self.actionSaveAs)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clearButton.setText(_translate("MainWindow", "Clear canvas"))
        self.brushSizeLabel.setText(_translate("MainWindow", "Current brush size:"))
        self.brushColorLabel.setText(_translate("MainWindow", "Current brush color:"))
        self.brushColorButton.setText(_translate("MainWindow", "Choose"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As.."))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))

from canvas import Canvas

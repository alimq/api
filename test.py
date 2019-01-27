# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(912, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sidebar = QtWidgets.QWidget(self.centralwidget)
        self.sidebar.setMinimumSize(QtCore.QSize(388, 0))
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
        self.brushColorDial = QtWidgets.QDial(self.sidebar)
        self.brushColorDial.setGeometry(QtCore.QRect(20, 180, 50, 64))
        self.brushColorDial.setObjectName("brushColorDial")
        self.brushColorLabel = QtWidgets.QLabel(self.sidebar)
        self.brushColorLabel.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.brushColorLabel.setObjectName("brushColorLabel")
        self.horizontalLayout.addWidget(self.sidebar)
        self.canvas = Canvas(self.centralwidget)
        self.canvas.setMinimumSize(QtCore.QSize(500, 500))
        self.canvas.setMaximumSize(QtCore.QSize(5000, 5000))
        self.canvas.setBaseSize(QtCore.QSize(500, 500))
        self.canvas.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.canvas.setAutoFillBackground(True)
        self.canvas.setStyleSheet("canvas{background-color: rgb(70, 70, 50);}")
        self.canvas.setObjectName("canvas")
        self.horizontalLayout.addWidget(self.canvas)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clearButton.setText(_translate("MainWindow", "Clear canvas"))
        self.brushSizeLabel.setText(_translate("MainWindow", "Current brush size:"))
        self.brushColorLabel.setText(_translate("MainWindow", "Current brush color:"))

from project import Canvas

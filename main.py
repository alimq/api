# -*- coding: utf-8 -*-
import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui import Ui_MainWindow
from os.path import expanduser


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.penSizeSlider.setMinimum(1)
        self.penSizeSlider.setMaximum(24)
        self.penSizeSlider.setTickInterval(1)
        self.penSizeSlider.valueChanged.connect(self.changePenSize)
        
        self.penColorButton.clicked.connect(self.changePenColor)
        self.clearButton.clicked.connect(self.clearCanvas)
        self.actionSaveAs.triggered.connect(self.saveAs)
        self.actionOpenFile.triggered.connect(self.openFile)
        self.penHardSoft.clicked.connect(self.changeHardSoft)
        self.penEraserButton.clicked.connect(self.changePenEraser)
        
        self.eraserSizeSlider.setMinimum(2)
        self.eraserSizeSlider.setMaximum(48)
        self.eraserSizeSlider.setTickInterval(2)
        self.eraserSizeSlider.valueChanged.connect(self.changeEraserSize)        
        
        
    def changePenSize(self):
        self.canvas.pen.setWidth(self.penSizeSlider.value())
        newLabel = 'Current pen size(' + str(self.penSizeSlider.value()) + '):'
        self.penSizeLabel.setText(newLabel)
        
    def changePenColor(self):
        color = QColorDialog().getColor()
        self.canvas.pen.setColor(color)
        
    def clearCanvas(self):
        self.canvas.painter.fillRect(0, 0, 600, 600, Qt.white)
        self.canvas.setPixmap(self.canvas.currentPixmap)
        
    def saveAs(self):
        saveAs_file = QFileDialog.getSaveFileName(None, 'Save File:', 'untitled.png', 'Images (*.png *.bmp *.jpg)')
        saveAs_ok = self.canvas.currentPixmap.save(saveAs_file[0])
        print('save', saveAs_ok)
        
    def openFile(self):
        openFile_file = QFileDialog.getOpenFileName(None, 'Open File:', '', 'Images (*.png *.bmp *.jpg)')
        openFile_ok = self.canvas.currentPixmap.load(openFile_file[0])
        self.canvas.setPixmap(self.canvas.currentPixmap)
        self.canvas.update()
        print('open', openFile_ok)
        
    def changeHardSoft(self):
        if self.penHardSoft.text() == 'Hard':
            self.canvas.pen.setCapStyle(Qt.RoundCap)
            self.canvas.pen.setJoinStyle(Qt.RoundJoin)
            self.penHardSoft.setText('Soft')
        elif self.penHardSoft.text() == 'Soft':
            self.canvas.pen.setCapStyle(Qt.SquareCap)
            self.canvas.pen.setJoinStyle(Qt.BevelJoin)
            self.penHardSoft.setText('Hard')
            
    def changePenEraser(self):
        if self.penEraserButton.text() == 'Pen':
            self.canvas.currentPen = self.canvas.eraser
            self.penEraserButton.setText('Eraser')
        elif self.penEraserButton.text() == 'Eraser':
            self.canvas.currentPen = self.canvas.pen
            self.penEraserButton.setText('Pen')
            
    def changeEraserSize(self):
        self.canvas.eraser.setWidth(self.eraserSizeSlider.value())
        newLabel = 'Current eraser size(' + str(self.eraserSizeSlider.value()) + '):'
        self.eraserSizeLabel.setText(newLabel)        
        

if __name__ == '__main__':
    application = QApplication(sys.argv)
    example = App()
    example.show()
    sys.exit(application.exec_())
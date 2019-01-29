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
        self.brushSizeSlider.setMinimum(1)
        self.brushSizeSlider.setMaximum(24)
        self.brushSizeSlider.setTickInterval(1)
        self.brushSizeSlider.valueChanged.connect(self.changeBrushSize)
        self.brushColorButton.clicked.connect(self.changeBrushColor)
        self.clearButton.clicked.connect(self.clearCanvas)
        self.actionSaveAs.triggered.connect(self.saveAs)
        self.actionOpenFile.triggered.connect(self.openFile)
        self.brushHardSoft.clicked.connect(self.changeHardSoft)
        
    def changeBrushSize(self):
        self.canvas.pen.setWidth(self.brushSizeSlider.value())
        
    def changeBrushColor(self):
        color = QColorDialog().getColor()
        self.canvas.pen.setColor(color)
        
    def clearCanvas(self):
        self.canvas.painter.fillRect(0, 0, 600, 600, Qt.white)
        self.canvas.setPixmap(self.canvas.myPixmap)
        
    def saveAs(self):
        saveAs_file = QFileDialog.getSaveFileName(None, 'Save File:', 'untitled.png', 'Images (*.png *.bmp *.jpg)')
        saveAs_ok = self.canvas.myPixmap.save(saveAs_file[0])
        print('save', saveAs_ok)
        
    def openFile(self):
        openFile_file = QFileDialog.getOpenFileName(None, 'Open File:', '', 'Images (*.png *.bmp *.jpg)')
        openFile_ok = self.canvas.myPixmap.load(openFile_file[0])
        self.canvas.setPixmap(self.canvas.myPixmap)
        self.canvas.update()
        print('open', openFile_ok)
        
    def changeHardSoft(self):
        if self.brushHardSoft.text() == 'Hard':
            self.canvas.pen.setCapStyle(Qt.RoundCap)
            self.canvas.pen.setJoinStyle(Qt.RoundJoin)
            self.brushHardSoft.setText('Soft')
        elif self.brushHardSoft.text() == 'Soft':
            self.canvas.pen.setCapStyle(Qt.SquareCap)
            self.canvas.pen.setJoinStyle(Qt.BevelJoin)
            self.brushHardSoft.setText('Hard')
        

if __name__ == '__main__':
    application = QApplication(sys.argv)
    example = App()
    example.show()
    sys.exit(application.exec_())
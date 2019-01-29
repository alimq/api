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
        print(saveAs_ok)
        

if __name__ == '__main__':
    application = QApplication(sys.argv)
    example = App()
    example.show()
    sys.exit(application.exec_())
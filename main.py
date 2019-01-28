# -*- coding: utf-8 -*-
import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.brushSizeSlider.valueChanged.connect(self.changeBrushSize)
        
    def changeBrushSize(self):
        self.canvas.pen.setWidth(self.brushSizeSlider.value())
        print(self.canvas.pen.width)

if __name__ == '__main__':
    application = QApplication(sys.argv)
    example = App()
    example.show()
    sys.exit(application.exec_())
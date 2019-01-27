# -*- coding: utf-8 -*-
import sys
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from test import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setCursor(QCursor(Qt.CrossCursor))
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(p)        
        self.path = QPainterPath()
        
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin()
        painter.drawPath(self.path)
        painter.end()
        
    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        update()
        
    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())
        update()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Paint App')
        
        
application = QApplication(sys.argv)
example = App()
example.show()
sys.exit(application.exec_())

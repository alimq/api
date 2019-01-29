from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Canvas(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(p)
        self.myPixmap = QPixmap(600, 600)
        self.painter = QPainter(self.myPixmap)
        self.pen = QPen(Qt.black)
        self.painter.setPen(self.pen)
        self.painter.fillRect(0, 0, 600, 600, Qt.white)
        self.setPixmap(self.myPixmap)
        self.last = None    

    def mouseMoveEvent(self, event):
        if self.last:
            self.painter.setPen(self.pen)
            self.painter.drawLine(self.last, event.pos())
            
            self.last = event.pos()
            self.setPixmap(self.myPixmap)
            self.update()

    def mousePressEvent(self, event):
        self.last = event.pos()
        
    def mouseReleaseEvent(self, event):
        self.last = None


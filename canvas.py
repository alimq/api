from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Canvas(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        self.currentPixmap = QPixmap(600, 600)
        self.painter = QPainter(self.currentPixmap)
        self.painter.fillRect(0, 0, 600, 600, Qt.white)
        self.setPixmap(self.currentPixmap)
        self.pen = QPen()
        self.last = None   
        
        self.eraser = QPen()
        self.eraser.setColor(Qt.white)
        self.eraser.setJoinStyle(Qt.RoundJoin)
        self.eraser.setCapStyle(Qt.RoundCap)
        
        self.currentPen = self.pen

    def mouseMoveEvent(self, event):
        if self.last:
            self.painter.setPen(self.currentPen)
            self.painter.drawLine(self.last, event.pos())
            
            self.last = event.pos()
            self.setPixmap(self.currentPixmap)
            self.update()

    def mousePressEvent(self, event):
        self.last = event.pos()
        
    def mouseReleaseEvent(self, event):
        self.last = None
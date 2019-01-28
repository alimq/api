from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Canvas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(p)        
        self.path = QPainterPath()
        self.pen = QPen()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.pen)
        painter.drawPath(self.path)
        painter.end()

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        self.update()

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())
        self.update()


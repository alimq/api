# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class PaintApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Paint App')
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    paint = PaintApp()
    paint.showMaximized()
    sys.exit(app.exec())
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
        self.setWindowTitle('YandexLyceum Paint Project')
        self.penSizeSlider.setMinimum(1)
        self.penSizeSlider.setMaximum(24)
        self.penSizeSlider.setTickInterval(1)
        self.penSizeSlider.valueChanged.connect(self.changePenSize)
        
        self.currentFile = None
        
        self.penColorButton.clicked.connect(self.changePenColor)
        self.clearButton.clicked.connect(self.clearCanvas)
        self.actionSaveAs.triggered.connect(self.saveAs)
        self.penHardSoft.clicked.connect(self.changeHardSoft)
        self.penEraserButton.clicked.connect(self.changePenEraser)
        
        self.eraserSizeSlider.setMinimum(2)
        self.eraserSizeSlider.setMaximum(48)
        self.eraserSizeSlider.setTickInterval(2)
        self.eraserSizeSlider.valueChanged.connect(self.changeEraserSize)     
        
        self.penTypeCombo.currentTextChanged.connect(self.changePenType)
        self.actionSave.triggered.connect(self.saveFile)
        
        
    def changePenSize(self):
        self.canvas.pen.setWidth(self.penSizeSlider.value())
        newLabel = 'Current pen size(' + str(self.penSizeSlider.value()) + '):'
        self.penSizeLabel.setText(newLabel)
        
    def changePenColor(self):
        color = QColorDialog().getColor()
        self.canvas.pen.setColor(color)
        self.canvas.brush.setColor(color)
        
    def clearCanvas(self):
        self.canvas.painter.fillRect(0, 0, 600, 600, Qt.white)
        self.canvas.setPixmap(self.canvas.currentPixmap)
        
    def saveAs(self):
        saveAs_file = QFileDialog.getSaveFileName(None, 'Save File:', 'yandexlyceum.png', 'Images (*.png *.bmp *.jpg)')
        saveAs_ok = self.canvas.currentPixmap.save(saveAs_file[0])
        if saveAs_ok:
            self.currentFile = saveAs_file[0]
            print('Successfully saved into', self.currentFile)
        else:
            print('Fail!')
        
    def saveFile(self):
        if self.currentFile:
            saveAs_ok = self.canvas.currentPixmap.save(self.currentFile)
            if saveAs_ok:
                print('Successfully saved', self.currentFile)
            else:
                print('Fail!')
        else:
            self.saveAs()
        
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
        
    def changePenType(self):
        val = self.penTypeCombo.currentText()
        if val == 'Default':
            self.canvas.brush.setStyle(Qt.SolidPattern)
        elif val == 'Dense 1':
            self.canvas.brush.setStyle(Qt.Dense1Pattern)
        elif val == 'Dense 2':
            self.canvas.brush.setStyle(Qt.Dense2Pattern)
        elif val == 'Dense 3':
            self.canvas.brush.setStyle(Qt.Dense3Pattern)
        elif val == 'Dense 4':
            self.canvas.brush.setStyle(Qt.Dense4Pattern)
        elif val == 'Dense 5':
            self.canvas.brush.setStyle(Qt.Dense5Pattern)
        elif val == 'Dense 6':
            self.canvas.brush.setStyle(Qt.Dense6Pattern)
        elif val == 'Dense 7':
            self.canvas.brush.setStyle(Qt.Dense7Pattern)       
        elif val == 'Horizontal':
            self.canvas.brush.setStyle(Qt.HorPattern)
        elif val == 'Vertical':
            self.canvas.brush.setStyle(Qt.VerPattern)
        elif val == 'Cross':
            self.canvas.brush.setStyle(Qt.CrossPattern)
        elif val == 'BDiagonal':
            self.canvas.brush.setStyle(Qt.BDiagPattern)
        elif val == 'FDiagonal':
            self.canvas.brush.setStyle(Qt.FDiagPattern)         
        elif val == 'DiagonalCross':
            self.canvas.brush.setStyle(Qt.DiagCrossPattern)    
        

if __name__ == '__main__':
    application = QApplication(sys.argv)
    example = App()
    example.show()
    sys.exit(application.exec_())
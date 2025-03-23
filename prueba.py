from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QHBoxLayout, QSplitter, QLineEdit, QFrame
import sys
from PyQt5 import QtGui, QtCore
#import PySide6 Qti

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title= "Mi titulo"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        hbox = QHBoxLayout()
        left = QFrame()
        left.setStyleSheet("background-color: yellow;border: 2px solid black;") 

        #left.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        left.setStyleSheet("background-color: red;border: 2px solid black;") 
        
        #bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter()

        lineedit = QLineEdit()
        lineedit.setText("LINE EDIT")


        splitter1.addWidget(left)
        splitter1.addWidget(lineedit)
        splitter1.setSizes([300,300])

        splitter2 = QSplitter()
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        

        hbox.addWidget(splitter2)

        self.setLayout(hbox)
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
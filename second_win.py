from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from inst import *

app = QApplication([])
window = QWidget()

class TestWin(QWidget):
    def __init__(self):
        super.__init__()
        self.setappear()
        self.initUI()
        self.connects()
        self.show()
        
    def setappear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_widht, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
        pass
    
    def connects(self):
        pass
    
    def show(self):
        pass

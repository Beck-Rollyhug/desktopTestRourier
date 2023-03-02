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
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        txt1 = QLabel(txt_fio)
        txt2 = QLabel('')
        txt3 = QLabel('txt_')
        txt4 = QLabel('txt_')
        txt5 = QLabel('txt_')
        txt6 = QLabel('(txt_')
        self.button1 = QPushButton('txt_b_')
        self.button2 = QPushButton('(txt_b_')
        self.button3 = QPushButton('txt_b_')
        self.btn_next = QPushButton('txt_b_')
        pole1 = QLineEdit('txt_l_')
        pole2 = QLineEdit('txt_l_')
        pole3 = QLineEdit('txt_l_')
        pole4 = QLineEdit('txt_l_)')
        pole5 = QLineEdit('txt_l_')
        
        self.r_line.addWidget(txt6)
        
        self.l_line.addWidget(txt1)
        self.l_line.addWidget(txt2)
        self.l_line.addWidget(txt3)
        self.l_line.addWidget(txt4)
        self.l_line.addWidget(txt5)
        self.l_line.addWidget(self.button1)
        self.l_line.addWidget(self.button2)
        self.l_line.addWidget(self.button3)
        self.l_line.addWidget(pole1)
        self.l_line.addWidget(pole2)
        self.l_line.addWidget(pole3)
        self.l_line.addWidget(pole4)
        self.l_line.addWidget(pole5)
        
        self.h_line.addLayout(r_line)
        self.h_line.addLayout(l_line)
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
    
    def show(self):
        pass

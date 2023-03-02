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
        self.txt_name = QLabel(txt_name)
        self.txt_age = QLabel(txt_age)
        self.txt_test1 = QLabel(txt_test1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_test3 = QLabel(txt_test3)
        self.txt_timer = QLabel(txt_timer)
        self.button_starttest1 = QPushButton(txt_starttest1)
        self.button_starttest2 = QPushButton(txt_starttest2)
        self.button_starttest3 = QPushButton(txt_starttest3)
        self.btn_next = QPushButton(txt_sendresults)
        self.hintname = QLineEdit(txt_hintname)
        self.hintage = QLineEdit(txt_hintage)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)
        
        self.r_line.addWidget(self.txt_timer)
        
        self.l_line.addWidget(self.txt_name)
        self.l_line.addWidget(self.hintname)
        self.l_line.addWidget(self.txt_age)
        self.l_line.addWidget(self.hintage)
        self.l_line.addWidget(self.txt_test1)
        self.l_line.addWidget(self.button_starttest1)
        self.l_line.addWidget(self.hinttest1)
        self.l_line.addWidget(self.txt_test2)
        self.l_line.addWidget(self.button_starttest2)
        self.l_line.addWidget(self.txt_test3)
        self.l_line.addWidget(self.button_starttest3)
        self.l_line.addWidget(self.hinttest2)
        self.l_line.addWidget(self.hinttest3)
        self.l_line.addWidget(self.btn_next, aligment = QtAlignCenter)
        
        self.h_line.addLayout(r_line)
        self.h_line.addLayout(l_line)
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
    
    def show(self):
        pass

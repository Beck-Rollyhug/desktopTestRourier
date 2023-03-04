from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
from final_win import *
from rupe import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setappear()
        self.initUI()
        self.connects()
        self.show()
        
    def setappear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
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
        
        self.r_line.addWidget(self.txt_timer, alignment = Qt.AlignRight)
        
        self.l_line.addWidget(self.txt_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hintname, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hintage, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_starttest1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_starttest2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.txt_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.button_starttest3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        
    def next_click(self):
        self.hide()
        self.fw = FinalWin(experement(int(self.hintage.text()), int(self.hinttest1.text()), int(self.hinttest2.text()), int(self.hinttest2.text())))
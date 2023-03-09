from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def results(self):
        self.answer = (4*(int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3) - 200)/10)
        if int(self.exp.age) >= 15:
            if int(self.answer) >= 15:
                return txt_res1
            elif int(self.answer) < 15 and int(self.answer) >= 11:
                return txt_res2
            elif int(self.answer) < 11 and int(self.answer) >= 6:
                return txt_res3
            elif int(self.answer) < 6 and int(self.answer) >= 0.5:
                return txt_res4
            else:
                return txt_res5
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.answer))
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.work_text, alignment = Qt.AlignCenter)
        self.v_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.setLayout(self.v_line)


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *

class FinalWin(QWidget):
    def __init__(self, res, txt_res):
        super().__init__()
        self.res = res
        self.txt_res = txt_res

        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.line = QVBoxLayout()
        self.res_txt = QLabel(self.res + ' ' + self.txt_res)
        self.line.addWidget(self.res_txt, alignment = Qt.AlignCenter)
        self.setLayout(self.line)


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from  inst import *

app = QApplication([])
main_win = QWidget()

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.unitUI()
        self.show()
    def set_apper(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def unitUI(self):
        pass
    def show():
        pass


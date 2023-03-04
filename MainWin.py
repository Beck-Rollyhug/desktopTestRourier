from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from inst import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
       
        # создаём и настраиваем графические элементы:
        self.set_appear()

        # устанавливает связи между элементами
        self.initUI()

        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.connects()

        # старт:
        self.show()

    def set_appear(self):
        txt_title = '111'
        win_x = 0
        win_y = 0
        win_width = 600
        win_height = 400

        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        pass
    def connects(self):
        pass
    def show(self):
        pass

app = QApplication([])
mw = MainWin()
app.exec_()

from PyQt5.QtCore import Qt
from PyQT5.QtCore import 
from inst import*

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTtle(txt_title)
        self.main.show()
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        pass
    def connects(self):
        pass
    def show(self):
        pass


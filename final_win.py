from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.v_line = QVBoxLayout()
        self.victory_win = QLabel()
        self.victory_win.setText('надпись')
        self.v_line.addWidget(victory_win, alignment = Qt.AlignCenter) 
    

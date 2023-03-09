from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import *
from second_win import *


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_txt = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button_next = QPushButton(txt_next)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_txt, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout.addWidget(self.button_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)
    def next_win(self):
        self.hide()
        self.tw = TestWin()
    def connects(self):
        self.button_next.clicked.connect(self.next_win)

app = QApplication([])
main_win = MainWin()
app.exec_()

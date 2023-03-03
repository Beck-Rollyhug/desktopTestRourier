from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from inst import *
from second_win import *

#TODO: Написать функцию initUI
#TODO: Написать функцию connects
#TODO: Написать функцию show
#TODO: Проверить файл MainWIn на работоспособность(Первый экран должен открываться при запуске)

txt_title = "Здоровье"
win_width, win_height = 1000, 600
win_x, win_y = 200, 200
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def next_win(self):
        self.hide()
        self.tw = TestWin()
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
    def connects(self):
        self.button_next.clicked.connect(self.next_win)

app = QApplication([])
main_win = MainWin()
app.exec_()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

app = QApplication([])
main_win = QWidget()

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.unitUI()
        self.show()
    def set_apper(self):
        pass
    def unitUI(self):
        pass

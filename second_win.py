from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from instr import *
from final_win import *

win_x, win_y = 200, 100
win_width, win_height = 1000, 600

time = QTime(0, 0, 0)

# Файл Артёма и Виталия
class Experiment():
    def __init__(self, age, t1, t2, t3):
        self.age = age
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setappear()
        self.initUI()
        self.connects()
        self.show()
        
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.hintage.text(), self.hinttest1.text(), self.hinttest2.text(), self.hinttest3.text())
        self.fw = FinalWin(self.exp)

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
        self.text_timer = QLabel(txt_timer)
        self.button_starttest1 = QPushButton(txt_starttest1)
        self.button_starttest2 = QPushButton(txt_starttest2)
        self.button_starttest3 = QPushButton(txt_starttest3)
        self.btn_next = QPushButton(txt_sendresults)
        self.hintname = QLineEdit(txt_hintname)
        self.hintage = QLineEdit(txt_hintage)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)
        
        self.l_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.r_line.addWidget(self.txt_name, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.hintname, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.txt_age, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.hintage, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.txt_test1, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.button_starttest1, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.hinttest1, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.txt_test2, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.button_starttest2, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.txt_test3, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.button_starttest3, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.hinttest2, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.hinttest3, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        
        self.h_line.addLayout(self.r_line)
        self.h_line.addLayout(self.l_line)
        self.setLayout(self.h_line)
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.button_starttest1.clicked.connect(self.timer_first)
        self.button_starttest2.clicked.connect(self.timer_second)
        self.button_starttest3.clicked.connect(self.timer_final)
        

    def timer_first(self):
        #1 ТАЙМЕР
        global time
        time = QTime(0, 0, 15)
        self.timer_first = QTimer()
        self.timer_first.timeout.connect(self.timer1Event)
        self.timer_first.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer_first.stop()



    def timer_second(self):
        #ВТОРОЙ ТАЙМЕР
        global time
        time = QTime(0, 0, 30)
        self.timer_second = QTimer()
        self.timer_second.timeout.connect(self.timer2Event)
        self.timer_second.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer_second.stop()
    


    def timer_final(self):
        #ТРЕТИЙ ТАЙМЕР
        global time
        time = QTime(0, 1, 0)
        self.timer_third = QTimer()
        self.timer_third.timeout.connect(self.timer3Event)
        self.timer_third.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0, 255, 0)")
            if time.toString("hh:mm:ss") == "00:00:00":
                self.timer_third.stop()
        else:
            self.text_timer.setStyleSheet("color: rgb(0, 0, 0)")

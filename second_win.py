from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import *

from instr import *
from final_win import *

# Файл Артёма и Виталия

time = QTime(0, 0, 0)

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setappear()
        self.initUI()
        self.connects()
        self.show()
        
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
        self.txt_timer = QLabel(txt_timer)
        self.button_starttest1 = QPushButton(txt_starttest1)
        self.button_starttest2 = QPushButton(txt_starttest2)
        self.button_starttest3 = QPushButton(txt_starttest3)
        self.btn_next = QPushButton(txt_sendresults)
        self.hintname = QLineEdit(txt_hintname)
        self.hintage = QLineEdit(txt_hintage)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)
        
        self.r_line.addWidget(self.txt_timer)
        
        self.l_line.addWidget(self.txt_name)
        self.l_line.addWidget(self.hintname)
        self.l_line.addWidget(self.txt_age)
        self.l_line.addWidget(self.hintage)
        self.l_line.addWidget(self.txt_test1)
        self.l_line.addWidget(self.button_starttest1)
        self.l_line.addWidget(self.hinttest1)
        self.l_line.addWidget(self.txt_test2)
        self.l_line.addWidget(self.button_starttest2)
        self.l_line.addWidget(self.txt_test3)
        self.l_line.addWidget(self.button_starttest3)
        self.l_line.addWidget(self.hinttest2)
        self.l_line.addWidget(self.hinttest3)
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        
        self.h_line.addLayout(self.r_line)
        self.h_line.addLayout(self.l_line)
        self.setLayout(self.h_line)
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        # self.button_starttest1.clicked.connect(self.timer)
        self.button_starttest2.clicked.connect(self.timer2)
        self.button_starttest1.clicked.connect(self.timer1)
        self.button_starttest3.clicked.connect(self.timer3)
        
        # self.button_starttest3.clicked.connect(self.timer)
        
    def next_click(self):
        self.hide()
        self.a = self.hinttest1.text()
        self.b = self.hinttest2.text()
        self.c = self.hinttest3.text()
        self.age = self.hintage.text()
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.age)
        self.fw = FinalWin(self.age,self.a,self.b,self.c)
    def timer1(self):
        global time
        self.timer = QTimer()
        time = QTime(0, 0, 30)
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer2(self):
        global time
        self.timer = QTimer()
        time = QTime(0, 0, 30)
        self.timer.timeout.connect(self.timer2Event)      
        self.timer.start(1500)
    def timer3(self):
        global time
        self.timer = QTimer()
        time = QTime(0, 1, 0)
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString('hh:mm:ss'))
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.txt_timer.setText(time.toString('hh:mm:ss')[6:8]) 
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def timer3Event(self):
        global time
        time = time.addSecs(-1) 
        self.txt_timer.setText(time.toString('hh:mm:ss'))
        if int(time.toString('hh:mm:ss')[6:8]) <= 15 or int(time.toString('hh:mm:ss')[6:8]) >= 45:
                self.txt_timer.setStyleSheet('color: rgb(0,255,0)')
        else:
            self.txt_timer.setStyleSheet('color: rgb(0,0,0)')
        
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    



    # def timer(self):
    #     t = timer_event_1()
    #     while int(t.split()[0]) > 0:
    #         self.txt_timer.setText(t)
    #         t = timer_event_1()


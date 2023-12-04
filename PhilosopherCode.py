from PyQt6 import QtCore
import time
import sys
from PyQt6 import QtWidgets,QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtCore import pyqtSignal
from NewUI import Ui_MainWindow
import threading

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        num_philosophers = 5
        self.forks = [Fork(i) for i in range(num_philosophers)]
        self.thread = {}
        
        self.uic.Button0.setEnabled(False)
        self.uic.Button1.setEnabled(False)
        self.uic.Button2.setEnabled(False)
        self.uic.Button3.setEnabled(False)
        self.uic.Button4.setEnabled(False)
        
        self.Button0_event = threading.Event()
        self.Button1_event = threading.Event()
        self.Button2_event = threading.Event()
        self.Button3_event = threading.Event()
        self.Button4_event = threading.Event()
        
        self.uic.Button0.clicked.connect(self.on_Button0_clicked)
        self.uic.Button1.clicked.connect(self.on_Button1_clicked)
        self.uic.Button2.clicked.connect(self.on_Button2_clicked)
        self.uic.Button3.clicked.connect(self.on_Button3_clicked)
        self.uic.Button4.clicked.connect(self.on_Button4_clicked)
        
        self.uic.Start_button.clicked.connect(self.start)
        #self.uic.Button0.clicked.connect(lambda: self.philosopher_0_status()) # vao ham chuyen trang thai
        #self.uic.Button1.clicked.connect(self.philosopher_2_status)
        
    def start(self):
        num_philosophers = 5
        forks = [Fork(i) for i in range(num_philosophers)]
        self.philosopher_0(forks[0],forks[1])
        self.philosopher_1(forks[1],forks[2])
        self.philosopher_2(forks[2],forks[3])
        self.philosopher_3(forks[3],forks[4])
        self.philosopher_4(forks[4],forks[0])
        
        self.uic.Button0.setEnabled(True)
        self.uic.Button1.setEnabled(True)
        self.uic.Button2.setEnabled(True)
        self.uic.Button3.setEnabled(True)
        self.uic.Button4.setEnabled(True)
        
    def on_Button0_clicked(self):
        self.Button0_event.set()
    def on_Button1_clicked(self):
        self.Button1_event.set()
    def on_Button2_clicked(self):
        self.Button2_event.set()
    def on_Button3_clicked(self):
        self.Button3_event.set()
    def on_Button4_clicked(self):
        self.Button4_event.set()
    
    def change_status(self, status):
        status=status
        i=self.sender().id
        if i==0: 
            button=self.uic.Button0
        elif i==1:
            button=self.uic.Button1
        elif i==2:
            button=self.uic.Button2
        elif i==3:
            button=self.uic.Button3
        else:
            button=self.uic.Button4
        
        if status=="Thinking":
            button.setEnabled(True)
            button.setStyleSheet("background-color: green")
            button.setText("Thinking")
        elif status=="Waiting":
            button.setStyleSheet("background-color: yellow")
            button.setText("Waiting")
            button.setEnabled(False)
        else:
            button.setEnabled(True)
            button.setStyleSheet("background-color: red")
            button.setText("Eating")
            
            
    def philosopher_0(self,fork0,fork1):
        self.thread[0] = Philosopher(id=0, left_fork=fork0, right_fork=fork1,button_event=self.Button0_event)
        self.thread[0].start()
        self.thread[0].pick_up_left_fork_signal.connect(self.pick_up_id_0_left)
        self.thread[0].pick_up_right_fork_signal.connect(self.pick_up_id_0_right)
        self.thread[0].put_down_left_fork_signal.connect(self.put_down_id_0_left)
        self.thread[0].put_down_right_fork_signal.connect(self.put_down_id_0_right)
        self.thread[0].change_status_signal.connect(self.change_status)
        
    def pick_up_id_0_left(self):
        self.uic.fork0.move(300, 80)
    def pick_up_id_0_right(self):
        self.uic.fork1.move(380, 90)
    def put_down_id_0_left(self):
        self.uic.fork0.move(230, 90)
    def put_down_id_0_right(self):
        self.uic.fork1.move(360, 170)
            
    def philosopher_1(self,fork1,fork2):
        self.thread[1] = Philosopher(id=1,left_fork=fork1, right_fork=fork2,button_event=self.Button1_event)
        self.thread[1].start()
        self.thread[1].pick_up_left_fork_signal.connect(self.pick_up_id_1_left)
        self.thread[1].pick_up_right_fork_signal.connect(self.pick_up_id_1_right)
        self.thread[1].put_down_left_fork_signal.connect(self.put_down_id_1_left)
        self.thread[1].put_down_right_fork_signal.connect(self.put_down_id_1_right)
        self.thread[1].change_status_signal.connect(self.change_status)
    def pick_up_id_1_left(self):
        self.uic.fork1.move(410, 220)
    def pick_up_id_1_right(self):
        self.uic.fork2.move(390, 300)
    def put_down_id_1_left(self):
        self.uic.fork1.move(360, 170)
    def put_down_id_1_right(self):
        self.uic.fork2.move(320, 300)

    
    def philosopher_2(self,fork2,fork3):
        self.thread[2] = Philosopher(id=2,left_fork=fork2, right_fork=fork3,button_event=self.Button2_event)
        self.thread[2].start()
        self.thread[2].pick_up_left_fork_signal.connect(self.pick_up_id_2_left)
        self.thread[2].pick_up_right_fork_signal.connect(self.pick_up_id_2_right)
        self.thread[2].put_down_left_fork_signal.connect(self.put_down_id_2_left)
        self.thread[2].put_down_right_fork_signal.connect(self.put_down_id_2_right)
        self.thread[2].change_status_signal.connect(self.change_status)
        #self.thread[2].pick_up_signal.connect(self.my_function)
        #self.uic.Button2.setEnabled(False)
    def pick_up_id_2_left(self):
        self.uic.fork2.move(300, 370)
    def pick_up_id_2_right(self):
        self.uic.fork3.move(210, 370)
    def put_down_id_2_left(self):
        self.uic.fork2.move(320, 310)
    def put_down_id_2_right(self):
        self.uic.fork3.move(170, 310)
    
    def philosopher_3(self,fork3,fork4):
        self.thread[3] = Philosopher(id=3,left_fork=fork3, right_fork=fork4,button_event=self.Button3_event)
        self.thread[3].start()
        self.thread[3].pick_up_left_fork_signal.connect(self.pick_up_id_3_left)
        self.thread[3].pick_up_right_fork_signal.connect(self.pick_up_id_3_right)
        self.thread[3].put_down_left_fork_signal.connect(self.put_down_id_3_left)
        self.thread[3].put_down_right_fork_signal.connect(self.put_down_id_3_right)
        self.thread[3].change_status_signal.connect(self.change_status)

    def pick_up_id_3_left(self):
        self.uic.fork3.move(110, 290)
    def pick_up_id_3_right(self):
        self.uic.fork4.move(80, 240)
    def put_down_id_3_left(self):
        self.uic.fork3.move(170, 310)
    def put_down_id_3_right(self):
        self.uic.fork4.move(120, 190)
    
    def philosopher_4(self,fork4,fork0):
        self.thread[4] = Philosopher(id=4,left_fork=fork4, right_fork=fork0,button_event=self.Button4_event)
        self.thread[4].start()
        self.thread[4].pick_up_left_fork_signal.connect(self.pick_up_id_4_left)
        self.thread[4].pick_up_right_fork_signal.connect(self.pick_up_id_4_right)
        self.thread[4].put_down_left_fork_signal.connect(self.put_down_id_4_left)
        self.thread[4].put_down_right_fork_signal.connect(self.put_down_id_4_right)
        self.thread[4].change_status_signal.connect(self.change_status)

    def pick_up_id_4_left(self):
        self.uic.fork4.move(110, 120)
    def pick_up_id_4_right(self):
        self.uic.fork0.move(150, 60)
    def put_down_id_4_left(self):
        self.uic.fork4.move(120, 190)
    def put_down_id_4_right(self):
        self.uic.fork0.move(230, 90)
    

# Fork class using QThread
class Fork(QtCore.QObject):
    def __init__(self, fork_id):
        super().__init__()
        self.fork_id = fork_id
        self.lock = QtCore.QMutex()

    def pick_up(self):
        self.lock.lock()
        
    def put_down(self):
        self.lock.unlock()

# Philosopher class using QThread
class Philosopher(QtCore.QThread): #Thread class
    change_status_signal = pyqtSignal(str)
    pick_up_left_fork_signal = pyqtSignal(int)
    pick_up_right_fork_signal = pyqtSignal(int)
    put_down_left_fork_signal = pyqtSignal(int)
    put_down_right_fork_signal = pyqtSignal(int)
    
    def __init__(self, id, left_fork, right_fork, button_event):
        super().__init__()
        self.id = id
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.button_event = button_event

    def run(self):
        while True:
            self.status = "Thinking"
            self.change_status_signal.emit(self.status)
            print(f"Philosopher {self.id} is thinking.")
            self.button_event.wait()  # Wait for the button signal
            self.button_event.clear()
            self.status = "Waiting"  
            self.change_status_signal.emit(self.status)
            
            print(f"Philosopher {self.id} try to picked up left fork {self.left_fork.fork_id}.")
            self.left_fork.pick_up()
            self.pick_up_left_fork_signal.emit(self.left_fork)
            print(f"Philosopher {self.id} picked up left fork {self.left_fork.fork_id}.")
            
            print(f"Philosopher {self.id} try to picked up right fork {self.right_fork.fork_id}.")
            self.right_fork.pick_up()
            self.pick_up_right_fork_signal.emit(self.right_fork)
            print(f"Philosopher {self.id} picked up right fork {self.right_fork.fork_id} and is eating.")
            
            self.status = "Eating"
            self.change_status_signal.emit(self.status)
            self.button_event.wait()  # Wait for the button signal
            self.button_event.clear()
            
            self.right_fork.put_down()
            self.put_down_right_fork_signal.emit(self.right_fork)
            print(f"Philosopher {self.id} put down right fork {self.right_fork.fork_id}.")
            self.left_fork.put_down()
            self.put_down_left_fork_signal.emit(self.left_fork)
            print(f"Philosopher {self.id} put down left fork {self.left_fork.fork_id}.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

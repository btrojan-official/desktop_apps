from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QLCDNumber, QMainWindow
from PySide6.QtGui import  QAction
from PySide6.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Calendar Widget")
        self.setGeometry(400, 400, 800, 600)
        
        layout = QVBoxLayout()

        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(8)
        layout.addWidget(self.lcd)
        
        self.label_data = QLabel(self)
        layout.addWidget(self.label_data)
        
        self.timer = QTimer()
        # self.timer.timeout.connect(self.show_date)
        # self.timer.start(1000)
        
        # self.setLayout(layout)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
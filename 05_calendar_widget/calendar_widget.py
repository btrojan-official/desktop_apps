from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QCalendarWidget, QMainWindow
from PySide6.QtGui import  QAction
from PySide6.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Calendar Widget")
        self.setGeometry(400, 400, 800, 600)
        
        layout = QVBoxLayout()
        
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        layout.addWidget(self.calendar)
        
        self.label = QLabel(self)
        layout.addWidget(self.label)
        
        
        locale = QLocale.system()
        self.calendar.setFirstDayOfWeek(locale.firstDayOfWeek())
        
    def show_date(self):
        selected_date = self.calendar.selectedDate()
        
        locale = QLocale.system()
        day_name = locale.dayName(selected_date.dayOfWeek())
        month_name = locale.monthName(selected_date.month())
        
        formatted_date = f"{day_name}, {selected_date.day()} {month_name} {selected_date.year()}"
        
        self.label.setText(f"Wybrana data: {formatted_date}")
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
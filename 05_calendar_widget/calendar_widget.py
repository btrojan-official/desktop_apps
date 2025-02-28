from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget, QMainWindow
from PySide6.QtGui import  QAction
from PySide6.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Calendar Widget")
        self.resize(400, 300)
        
        self.layout = QVBoxLayout()
        
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.layout.addWidget(self.calendar)
        
        self.label = QLabel("Wybrana data: ")
        self.layout.addWidget(self.label)
        
        self.locale = QLocale.system()
        
        self.calendar.setFirstDayOfWeek(self.locale.firstDayOfWeek())
        
    def show_date(self):
        selected_date = self.calendar.selectedDate()
        
        day_name = self.locale.dayName(selected_date.dayOfWeek())
        month_name = self.locale.monthName(selected_date.month())
        
        formatted_date = f"{day_name}, {selected_date.day()} {month_name} {selected_date.year()}"
        
        self.label.setText(f"Wybrana data: {formatted_date}")
            
            
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QLCDNumber, QMainWindow, QWidget
from PySide6.QtCore import QTimer, QTime, QDate, QLocale, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Calendar Widget")
        self.setGeometry(100, 100, 400, 200)  # Adjusted for better UI
        
        # Main widget and layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        
        # LCD Time Display
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(8)
        self.lcd.setStyleSheet("border: 2px solid #00ff00; background: black; color: lime; font-size: 36px;")
        layout.addWidget(self.lcd)
        
        # Label for Date
        self.label_data = QLabel(self)
        self.label_data.setAlignment(Qt.AlignCenter)  # Centering text
        layout.addWidget(self.label_data)
        
        # Timer to update clock
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Refresh every second
        
        self.update_time()
        
        # Apply layout to the main window
        self.setCentralWidget(central_widget)
        
        # General Styling
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: white;
                font-family: 'Courier New', Courier, monospace;
            }
            QLabel {
                font-size: 18px;
                margin-top: 10px;
            }
        """)
        
    def update_time(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        
        self.lcd.display(current_time.toString("HH:mm:ss"))
        
        locale = QLocale.system()
        full_date = locale.toString(current_date, "dddd, dd MMMM yyyy")
        self.label_data.setText(f"Wybrana data: {full_date}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import QSize, Qt

from mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Excel Desktop Editor")
        self.setGeometry(200, 200, 500, 500)
        
        self.ui_python = Ui_MainWindow()
        self.ui_python.setupUi(self)
        
        # button = QPushButton("Press Button!")
        # button.clicked.connect(self.button_click)
        
        # button_2 = QPushButton("Press Button!")
        # button_2.clicked.connect(self.button_click)
        
        # widget = QWidget()
        # layout = QVBoxLayout()
        
        # self.setCentralWidget(widget)
        # widget.setLayout(layout)
        
        # layout.addWidget(button)
        # layout.addWidget(button_2)
        
    def button_click(self):
        print("Kliknięto w przycisk")
        

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
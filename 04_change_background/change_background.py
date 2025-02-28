from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Change Background")
        self.resize(800, 600)
        self.create_menu()
        
    def create_menu(self):
        self.menu = self.menuBar()
        self.menu.addAction("Background color")
        
        change_color_action = QAction("Select Color", self)
        change_color_action.triggered.connect(self.change_color)
        self.menu.addAction(change_color_action)
        
    def change_color(self):
        color = QColorDialog.getColor()
        
        if color.isValid():
            self.setStyleSheet(f"background-color: {color.name()};")
            
            
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
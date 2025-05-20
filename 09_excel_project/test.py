from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        action = QAction("Example Action", self)  # 'self' is QMainWindow, valid QObject
        self.menuBar().addAction(action)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
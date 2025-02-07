import json

from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QTableWidget, QLabel
from PySide6.QtGui import QStandardItemModel, QStandardItem
    
from layout import Ui_Dialog
    
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.setWindowTitle("ToDo List :)")
        
        self.model = QStandardItemModel()
        self.ui.listView.setModel(self.model)
        
        self.ui.pushButton_6.clicked.connect(self.add_item)
        
    def add_item(self):
        title = self.ui.lineEdit.text()
        status = self.ui.comboBox.currentText()
        date = self.ui.dateTimeEdit.dateTime()
        date_string = date.toString(self.ui.dateTimeEdit.displayFormat())
        
        task_text = title + " || " + status + " || Due: " + date_string
        
        item = QStandardItem(task_text)
        
        self.model.appendRow(item)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
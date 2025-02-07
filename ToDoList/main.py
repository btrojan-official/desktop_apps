import json

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor
from PySide6.QtCore import Qt
    
from layout import Ui_Dialog
from Task import Task
    
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.setWindowTitle("ToDo List :)")
        
        self.list_data = [] 
        
        self.model = QStandardItemModel()
        self.ui.listView.setModel(self.model)
        
        self.ui.pushButton_6.clicked.connect(self.add_item)
        self.ui.pushButton_2.clicked.connect(self.remove_item)
        
    def add_item(self):
        title = self.ui.lineEdit.text()
        status = self.ui.comboBox.currentText()
        date = self.ui.dateTimeEdit.dateTime().toPython()
        
        new_task = Task(title, status, date)
        self.list_data.append(new_task)
        
        self.display_list()
        
    def remove_item(self):
        clicked_id = self.ui.listView.currentIndex().row()
        if clicked_id == -1:
            print("No item is selected!")
            return
        self.list_data.remove(self.list_data[clicked_id])
        
        self.display_list()
        
    def edit_item(self):
        clicked_id = self.ui.listView.currentIndex().row()
        if clicked_id == -1:
            print("No item is selected!")
            return
        
        # tutaj dodaj display dla nowego boxa z selectem pomiędzy statusami dostępnymi
        
        self.display_list()
        
    def display_list(self):
        self.model.clear()
        for task in self.list_data:
            item = QStandardItem()
            item.setText(str(task))
            if task.is_past_due():
                item.setData(QColor("red"), Qt.ForegroundRole)
            self.model.appendRow(item)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
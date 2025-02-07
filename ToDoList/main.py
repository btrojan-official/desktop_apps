import json
from datetime import datetime

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor
from PySide6.QtCore import Qt
    
from utils.layout import Ui_Dialog
from utils.Task import Task
from utils.ComboBoxDialog import ComboBoxDialog
    
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
        self.ui.pushButton.clicked.connect(self.edit_item)
        self.ui.pushButton_5.clicked.connect(self.save_list_data)
        self.ui.pushButton_7.clicked.connect(self.load_list_data)
        
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
        
        dialog = ComboBoxDialog()
        if dialog.exec() == QDialog.Accepted:
            selected_value = dialog.get_selected_value()
            self.list_data[clicked_id].status = selected_value
        else:
            print("Dialog was canceled.")
        
        self.display_list()
        
    def display_list(self):
        self.model.clear()
        for task in self.list_data:
            item = QStandardItem()
            item.setText(str(task))
            if task.is_past_due():
                item.setData(QColor("red"), Qt.ForegroundRole)
            self.model.appendRow(item)
            
    def save_list_data(self):
        tasks_dict = [task.to_dict() for task in self.list_data]

        with open('backup.json', 'w') as file:
            json.dump(tasks_dict, file, indent=4)
            
        print("App data was saved to file: backup.json")
        
    def load_list_data(self):
        with open("backup.json", "r") as f:
            data = json.load(f)

        self.list_data = [Task(**item) for item in data]
        
        self.display_list()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
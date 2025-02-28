import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QHBoxLayout, QDialogButtonBox

class ComboBoxDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Select status for task')

        layout = QVBoxLayout()

        label = QLabel('Please select an option:')
        layout.addWidget(label)

        self.comboBox = QComboBox()
        self.comboBox.addItems(['To do', 'Done']) 
        layout.addWidget(self.comboBox)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def get_selected_value(self):
        return self.comboBox.currentText()


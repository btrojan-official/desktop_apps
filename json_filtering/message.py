import json

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy, \
    QTableWidget, QTableWidgetItem, QLabel

sizes = ['Wszystkie', '2XL', 'XL', 'L', 'M', 'S', 'XS']

def load_data():
    with open('person.json', 'r', encoding='utf-8') as file:
        return json.load(file)

persons = load_data()

avg_salary = sum([float(person['salary'].replace('€', '').replace(',', '.')) for person in persons]) / len(persons)
avg_salary = round(avg_salary, 2)

class MainWindow(QWidget):
    def __init__(self):
        self.current_size = 'Wszystkie'

        super().__init__()
        self.setWindowTitle('Filtering data')
        self.resize(800, 600)

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        self.size__btns = []

        self.radioLayout = QHBoxLayout()
        mainLayout.addLayout(self.radioLayout)
        for size in sizes:
            radio = QPushButton(size)
            radio.setStyleSheet(f'background-color: {"#0a59ca" if size == self.current_size else "#0e6efd"}; color: #fff; border-radius: 5px; padding: 5px 10px;')
            radio.clicked.connect(lambda checked, s=size: self.set_current_size(s))
            self.radioLayout.addWidget(radio)
            self.size__btns.append(radio)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.radioLayout.addItem(spacer)

        self.maxAndMinSalaryLayout = QHBoxLayout()
        mainLayout.addLayout(self.maxAndMinSalaryLayout)

        max_salary_btn = QPushButton('Maksymalne wynagrodzenie')
        max_salary_btn.setStyleSheet('background-color: #1c8454; color: #fff; border-radius: 5px; padding: 5px 10px;')
        max_salary_btn.clicked.connect(self.max_salary)

        min_salary_btn = QPushButton('Minimalne wynagrodzenie')
        min_salary_btn.setStyleSheet('background-color: #1c8454; color: #fff; border-radius: 5px; padding: 5px 10px;')
        min_salary_btn.clicked.connect(self.min_salary)

        self.maxAndMinSalaryLayout.addWidget(max_salary_btn)
        self.maxAndMinSalaryLayout.addWidget(min_salary_btn)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.maxAndMinSalaryLayout.addItem(spacer)

        avg_salary_formatted = str(avg_salary)[:1] + "," + str(avg_salary)[1:]
        avg_salary_label = QLabel(f'Średnie wynagrodzenie: €{avg_salary_formatted}')
        avg_salary_label.setStyleSheet('font-size: 20px; color: #dc3848')
        mainLayout.addWidget(avg_salary_label)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setRowCount(len(persons))
        self.table.setHorizontalHeaderLabels(['ID', 'Imię', 'Nazwisko', 'Email', 'Płeć', 'Wynagrodzenie', 'Rozmiar koszulki'])

        for row, person in enumerate(persons):
            for col, data in enumerate(person.values()):
                self.table.setItem(row, col, QTableWidgetItem(str(data)))

        mainLayout.addWidget(self.table)

    def max_salary(self):
        max_salary_person = max(persons, key=lambda person: float(person['salary'].replace('€', '').replace(',', '.')))
        max_salary = round(float(max_salary_person['salary'].replace('€', '').replace(',', '.')), 2)
        self.update_table([max_salary_person])

    def min_salary(self):
        min_salary_person = min(persons, key=lambda person: float(person['salary'].replace('€', '').replace(',', '.')))
        min_salary = round(float(min_salary_person['salary'].replace('€', '').replace(',', '.')), 2)
        self.update_table([min_salary_person])

    def update_table(self, data):
        self.table.setRowCount(0)
        for row, person in enumerate(data):
            self.table.insertRow(self.table.rowCount())
            for col, value in enumerate(person.values()):
                self.table.setItem(self.table.rowCount() - 1, col, QTableWidgetItem(str(value)))

    def filter_data(self):
        self.table.setRowCount(0)
        for row, person in enumerate(persons):
            if self.current_size == 'Wszystkie' or person['size'] == self.current_size:
                self.table.insertRow(self.table.rowCount())
                for col, data in enumerate(person.values()):
                    self.table.setItem(self.table.rowCount() - 1, col, QTableWidgetItem(str(data)))

    def set_current_size(self, size):
        self.current_size = size
        for radio in self.size__btns:
            radio.setStyleSheet(f'background-color: {"#0a59ca" if radio.text() == self.current_size else "#0e6efd"}; color: #fff; border-radius: 5px; padding: 5px 10px;')

        self.filter_data()

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
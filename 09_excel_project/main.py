import sys
import pandas as pd
from PySide6.QtWidgets import (QMainWindow, QApplication, QFileDialog, QMessageBox, QInputDialog)
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QAction
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mainwindow_ui import Ui_MainWindow

class PandasModel(QAbstractTableModel):
    def __init__(self, df: pd.DataFrame):
        super().__init__()
        self._df = df.copy()
        self._original_df = df.copy()
        self._undo_stack = []

    def rowCount(self, parent=QModelIndex()):
        return self._df.shape[0]

    def columnCount(self, parent=QModelIndex()):
        return self._df.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid() and role in (Qt.DisplayRole, Qt.EditRole):
            return str(self._df.iat[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._df.columns[section]
            else:
                return str(self._df.index[section])
        return None

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            row, col = index.row(), index.column()
            old_value = self._df.iat[row, col]
            self._undo_stack.append((row, col, old_value))
            self._df.iat[row, col] = value
            self.dataChanged.emit(index, index, [Qt.DisplayRole])
            return True
        return False

    def undo(self):
        if self._undo_stack:
            row, col, value = self._undo_stack.pop()
            self._df.iat[row, col] = value
            index = self.index(row, col)
            self.dataChanged.emit(index, index, [Qt.DisplayRole])

    def get_dataframe(self):
        return self._df

    def set_dataframe(self, df):
        self.beginResetModel()
        self._df = df.copy()
        self._undo_stack.clear()
        self.endResetModel()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_python = Ui_MainWindow()
        self.ui_python.setupUi(self)

        self.file_path = None
        self.excel_data = {}
        self.model = None

        self.action_open = QAction("Open Excel File", self)   
        self.ui_python.menu_open.addAction(self.action_open)
        self.action_open.triggered.connect(self.open_file)
    
        self.action_save_as = QAction("Save As", self)     
        self.ui_python.menuSave_as.addAction(self.action_save_as)
        self.action_save_as.triggered.connect(self.save_as)
        
        self.ui_python.filter_button.clicked.connect(self.apply_filter)
        self.ui_python.chart_button.clicked.connect(self.generate_chart)
        self.ui_python.undo_button.clicked.connect(self.undo_change)
        self.ui_python.sheet_combobox.currentIndexChanged.connect(self.load_sheet)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Excel File', '', 'Excel Files (*.xlsx *.xls)')
        if not file_path:
            return

        try:
            self.file_path = file_path
            xls = pd.ExcelFile(file_path)
            self.excel_data = {sheet: xls.parse(sheet) for sheet in xls.sheet_names}
            self.ui_python.sheet_combobox.clear()
            self.ui_python.sheet_combobox.addItems(xls.sheet_names)
            self.load_sheet()
        except Exception as e:
            QMessageBox.critical(self, 'Error', f"Failed to load file: {e}")

    def load_sheet(self):
        sheet = self.ui_python.sheet_combobox.currentText()
        if not sheet:
            return
        df = self.excel_data[sheet]
        self.model = PandasModel(df)
        self.ui_python.sheet_tableview.setModel(self.model)
        self.update_status()

    def update_status(self):
        sheet = self.ui_python.sheet_combobox.currentText()
        rows = len(self.model.get_dataframe())
        self.ui_python.path_label.setText(f"Path: {self.file_path}")
        self.ui_python.records_label.setText(f"Records: {rows}")

    def apply_filter(self):
        if not self.model:
            return

        df = self.model.get_dataframe()
        column, ok = QInputDialog.getItem(self, "Select column", "Column:", df.columns.tolist(), editable=False)
        if not ok:
            return

        value, ok = QInputDialog.getText(self, "Enter filter value", f"Show rows where {column} ==")
        if ok:
            try:
                filtered_df = df[df[column].astype(str) == value]
                self.model.set_dataframe(filtered_df)
                self.update_status()
            except Exception as e:
                QMessageBox.warning(self, 'Filter Error', f"Could not apply filter: {e}")

    def save_as(self):
        if not self.model:
            return
        path, _ = QFileDialog.getSaveFileName(self, 'Save Excel File', '', 'Excel Files (*.xlsx)')
        if not path:
            return
        try:
            df = self.model.get_dataframe()
            df.to_excel(path, index=False)
            QMessageBox.information(self, "Success", f"File saved to: {path}")
        except Exception as e:
            QMessageBox.critical(self, "Save Error", str(e))

    def undo_change(self):
        if self.model:
            self.model.undo()

    def generate_chart(self):
        if not self.model:
            return

        df = self.model.get_dataframe()
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        if len(numeric_cols) < 1:
            QMessageBox.warning(self, "Chart", "No numeric columns available to plot.")
            return

        column, ok = QInputDialog.getItem(self, "Select column", "Plot by:", numeric_cols, editable=False)
        if ok:
            df[column].value_counts().plot(kind='bar')
            plt.title(f"Value counts of {column}")
            plt.xlabel(column)
            plt.ylabel("Count")
            plt.tight_layout()
            plt.show()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
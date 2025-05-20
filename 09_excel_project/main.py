import sys
import pandas as pd
from PySide6.QtWidgets import (QMainWindow, QApplication, QFileDialog, QMessageBox, QInputDialog)
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QAction
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mainwindow_ui import Ui_MainWindow

from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton

class FilterDialog(QDialog):
    def __init__(self, columns):
        super().__init__()
        self.setWindowTitle("Apply Filter")
        self.setMinimumWidth(300)
        layout = QVBoxLayout()

        # Column selector
        col_layout = QHBoxLayout()
        col_layout.addWidget(QLabel("Column:"))
        self.column_selector = QComboBox()
        self.column_selector.addItems(columns)
        col_layout.addWidget(self.column_selector)
        layout.addLayout(col_layout)

        # Condition inputs
        self.greater_input = QLineEdit()
        self.less_input = QLineEdit()
        self.equal_input = QLineEdit()

        layout.addWidget(QLabel("Greater than:"))
        layout.addWidget(self.greater_input)

        layout.addWidget(QLabel("Less than:"))
        layout.addWidget(self.less_input)

        layout.addWidget(QLabel("Equal to:"))
        layout.addWidget(self.equal_input)

        # Buttons
        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("Apply")
        self.cancel_button = QPushButton("Cancel")
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_filter_data(self):
        return (
            self.column_selector.currentText(),
            self.greater_input.text().strip(),
            self.less_input.text().strip(),
            self.equal_input.text().strip()
        )


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
            column_name = self._df.columns[col]
            old_value = self._df.iat[row, col]
            self._undo_stack.append((row, col, old_value))
            try:
                dtype = self._df[column_name].dtype
                if pd.api.types.is_numeric_dtype(dtype):
                    cast_value = pd.to_numeric(value)
                elif pd.api.types.is_datetime64_any_dtype(dtype):
                    cast_value = pd.to_datetime(value)
                else:
                    cast_value = value  # keep as string or object
            except Exception:
                cast_value = value  # fallback on error

            self._df.iat[row, col] = cast_value
            self.dataChanged.emit(index, index, [Qt.DisplayRole])
            main_window_ref = QApplication.instance().property("main_window_ref")
            if main_window_ref:
                sheet = main_window_ref.ui_python.sheet_combobox.currentText()
                main_window_ref.excel_data[sheet] = self._df.copy()
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
        self.filtered = False

        self.action_open = QAction("Open", self)   
        self.ui_python.menu_file.addAction(self.action_open)
        self.action_open.triggered.connect(self.open_file)
    
        self.action_save_as = QAction("Save", self)     
        self.ui_python.menu_file.addAction(self.action_save_as)
        self.action_save_as.triggered.connect(self.save)
    
        self.action_save_as = QAction("Save As", self)     
        self.ui_python.menu_file.addAction(self.action_save_as)
        self.action_save_as.triggered.connect(self.save_as)
        
        self.action_save_as = QAction("Help", self)     
        self.ui_python.menu_file.addAction(self.action_save_as)
        self.action_save_as.triggered.connect(self.show_help)
        
        self.ui_python.filter_button.clicked.connect(self.apply_filter)
        self.ui_python.chart_button.clicked.connect(self.generate_chart)
        self.ui_python.undo_button.clicked.connect(self.undo_change)
        self.ui_python.sheet_combobox.currentIndexChanged.connect(self.load_sheet)
        
        QApplication.instance().setProperty("main_window_ref", self)

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

    def save(self):
        if not self.model or not self.file_path:
            return
        try:
            sheet = self.ui_python.sheet_combobox.currentText()
            self.excel_data[sheet] = self.model.get_dataframe()
            with pd.ExcelWriter(self.file_path, engine='openpyxl') as writer:
                for name, df in self.excel_data.items():
                    df.to_excel(writer, sheet_name=name, index=False)
            QMessageBox.information(self, "Saved", f"File saved to: {self.file_path}")
        except Exception as e:
            QMessageBox.critical(self, "Save Error", str(e))

    def save_as(self):
        if not self.model:
            return
        path, _ = QFileDialog.getSaveFileName(self, 'Save Excel File', '', 'Excel Files (*.xlsx)')
        if not path:
            return
        try:
            sheet = self.ui_python.sheet_combobox.currentText()
            self.excel_data[sheet] = self.model.get_dataframe()
            with pd.ExcelWriter(path, engine='openpyxl') as writer:
                for name, df in self.excel_data.items():
                    df.to_excel(writer, sheet_name=name, index=False)
            QMessageBox.information(self, "Success", f"File saved to: {path}")
        except Exception as e:
            QMessageBox.critical(self, "Save Error", str(e))


    def show_help(self):
        help_text = (
            "Functionality Guide:\n\n"
            "Open: Load an Excel file with multiple sheets.\n"
            "Sheet Selector: Choose a sheet to view and edit.\n"
            "Editable Table: Double-click a cell to edit its content.\n"
            "Undo: Reverts the last change made to a cell.\n"
            "Filter: Choose a column and a value to filter displayed rows.\n"
            "Chart: Select a numeric column to plot a bar chart of value counts.\n"
            "Save: Save current changes back to the originally loaded file.\n"
            "Save As: Save the data to a new Excel file.\n"
        )
        QMessageBox.information(self, "Help", help_text)

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
        rows = self.model.rowCount() * self.model.columnCount()
        self.ui_python.path_label.setText(f"Path: {self.file_path}")
        self.ui_python.records_label.setText(f"Records: {rows}")

    def apply_filter(self):
        if not self.model:
            return
        
        self.filtered = True

        df = self.model.get_dataframe()
        dialog = FilterDialog(df.columns.tolist())
        if dialog.exec() != QDialog.Accepted:
            return

        column, gt, lt, eq = dialog.get_filter_data()
        series = df[column]
        filtered_df = df.copy()

        if gt:
            try:
                filtered_df = filtered_df[series.astype(float) > float(gt)]
            except:
                filtered_df = filtered_df[series > gt]

        if lt:
            try:
                filtered_df = filtered_df[series.astype(float) < float(lt)]
            except:
                filtered_df = filtered_df[series < lt]

        if eq:
            filtered_df = filtered_df[series.astype(str) == eq]

        self.model.set_dataframe(filtered_df)
        self.update_status()

    def undo_change(self):
        if not self.model:
            return
        if self.filtered: 
            self.filtered = False
            original_df = self.excel_data[self.ui_python.sheet_combobox.currentText()]
            self.model.set_dataframe(original_df)
            self.update_status()
        else:
            self.model.undo()


    def generate_chart(self):
        if not self.model:
            return

        # Get the latest data from the model
        df = self.model.get_dataframe()
        df = df.copy()  # Avoid modifying in-place during plotting

        if df.empty:
            QMessageBox.warning(self, "Chart", "DataFrame is empty.")
            return

        columns = df.columns.tolist()
        x_column, ok1 = QInputDialog.getItem(self, "Select X-axis", "X-axis column:", columns, editable=False)
        if not ok1:
            return

        y_column, ok2 = QInputDialog.getItem(self, "Select Y-axis", "Y-axis column:", columns, editable=False)
        if not ok2:
            return

        if x_column == y_column:
            QMessageBox.warning(self, "Chart", "X and Y columns must be different.")
            return

        x_data = df[x_column]
        y_data = df[y_column]

        try:
            if pd.api.types.is_numeric_dtype(x_data) and pd.api.types.is_numeric_dtype(y_data):
                plt.plot(x_data, y_data, marker='o', linestyle='-')
                plt.title(f"{y_column} vs {x_column}")
                plt.xlabel(x_column)
                plt.ylabel(y_column)
            elif not pd.api.types.is_numeric_dtype(x_data) and pd.api.types.is_numeric_dtype(y_data):
                grouped = df.groupby(x_column)[y_column].sum()
                grouped.plot(kind='bar')
                plt.title(f"{y_column} by {x_column}")
                plt.xlabel(x_column)
                plt.ylabel(f"Sum of {y_column}")
            else:
                x_type = str(x_data.dtype)
                y_type = str(y_data.dtype)
                QMessageBox.warning(
                    self,
                    "Chart",
                    f"Unsupported column types for chart.\n"
                    f"X column type: {x_type}\n"
                    f"Y column type: {y_type}"
                )
                return

            plt.tight_layout()
            plt.show()

        except Exception as e:
            QMessageBox.critical(self, "Chart Error", f"Failed to generate chart:\n{str(e)}")



app = QApplication([])
window = MainWindow()
window.show()
app.exec()
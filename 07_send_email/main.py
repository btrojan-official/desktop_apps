import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from SendLetter_ui import Ui_Dialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  
        self.ui.setupUi(self)
        
        pixmap = QPixmap("images/pocztowka.png")
        self.ui.imageLabel.setPixmap(pixmap)
        self.ui.priceLabel.setText("Cena: 1 zł")

        self.ui.submitButton.clicked.connect(lambda: self.on_submit())
        self.ui.checkPriceButton.clicked.connect(lambda: self.on_check_price())
        
    def on_submit(self):
        post_number = self.ui.postNumberLineEdit.text()

        if len(post_number) < 5 or len(post_number) > 5:
            self.show_message("Error", "Nieprawidłowa liczba cyfr w kodzie pocztowym")
        if not post_number.isdigit():
            self.show_message("Error", "Kod pocztowy powinien się składać z samych cyfr")
        else:
            self.show_message("Valid", "Dane przesyłki zostały wprowadzone")

    def on_check_price(self):
        if self.ui.postcartRadio.isChecked():
            self.ui.imageLabel.setPixmap(QPixmap("images/pocztowka.png"))
            self.ui.priceLabel.setText("Cena: 1 zł")
        elif self.ui.letterRadio.isChecked():
            self.ui.imageLabel.setPixmap(QPixmap("images/list.png"))
            self.ui.priceLabel.setText("Cena: 1,5 zł")
        elif self.ui.packageRadio.isChecked():
            self.ui.imageLabel.setPixmap(QPixmap("images/paczka.png"))
            self.ui.priceLabel.setText("Cena: 10 zł")
    
    def show_message(self, title, message):

        msg = QMessageBox(self)
        if title == "Valid":
            msg.setIcon(QMessageBox.Information)
        else:
            msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)

        msg.exec()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
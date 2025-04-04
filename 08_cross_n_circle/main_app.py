import sys

from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        ui_file = QFile('layout.ui')
        if not ui_file.open(QIODevice.ReadOnly):
            print(f'Cannot open file: {ui_file.errorString()}')
            return

        loader = QUiLoader()
        self.ui = loader.load(ui_file)
        ui_file.close()

        if not self.ui:
            print(loader.errorString())
            return

        self.ui.show()

        self.setGeometry(self.ui.geometry())
        self.setWindowTitle(self.ui.windowTitle())

        self.isGameRunning = False
        self.player = None

        self.label = self.ui.label
        self.inputX = self.ui.inputX
        self.inputO = self.ui.inputO

        self.btn1x1 = self.ui.btn1x1
        self.btn1x2 = self.ui.btn1x2
        self.btn1x3 = self.ui.btn1x3
        self.btn2x1 = self.ui.btn2x1
        self.btn2x2 = self.ui.btn2x2
        self.btn2x3 = self.ui.btn2x3
        self.btn3x1 = self.ui.btn3x1
        self.btn3x2 = self.ui.btn3x2
        self.btn3x3 = self.ui.btn3x3

        self.btnNewGame = self.ui.btnNewGame

        self.btnNewGame.clicked.connect(self.new_game)

        self.btn1x1.clicked.connect(lambda: self.handleBtns(1, 1))
        self.btn1x2.clicked.connect(lambda: self.handleBtns(1, 2))
        self.btn1x3.clicked.connect(lambda: self.handleBtns(1, 3))
        self.btn2x1.clicked.connect(lambda: self.handleBtns(2, 1))
        self.btn2x2.clicked.connect(lambda: self.handleBtns(2, 2))
        self.btn2x3.clicked.connect(lambda: self.handleBtns(2, 3))
        self.btn3x1.clicked.connect(lambda: self.handleBtns(3, 1))
        self.btn3x2.clicked.connect(lambda: self.handleBtns(3, 2))
        self.btn3x3.clicked.connect(lambda: self.handleBtns(3, 3))

        self.btns = [
            [self.btn1x1, self.btn1x2, self.btn1x3],
            [self.btn2x1, self.btn2x2, self.btn2x3],
            [self.btn3x1, self.btn3x2, self.btn3x3]
        ]

    def new_game(self):
        if self.inputX.text() == '' or self.inputO.text() == '':
            self.label.setText('No player names were provided')
            return

        self.isGameRunning = True

        self.playerX = self.inputX.text()
        self.playerO = self.inputO.text()

        self.player = self.playerX

        for row in self.btns:
            for btn in row:
                btn.setText('')

        self.label.setText(f'{self.playerX} turn')

    def getBtn(self, x, y):
        return self.btns[x - 1][y - 1]

    def handleBtns(self, x, y):
        if not self.isGameRunning:
            return

        btn = self.getBtn(x, y)

        if btn.text() != '':
            return

        btn.setText('X' if self.player == self.playerX else 'O')

        if self.check_winner():
            self.label.setText(f'{self.player} wins')
            self.isGameRunning = False
            return

        if self.check_draw():
            self.label.setText('Draw')
            self.isGameRunning = False
            return

        self.player = self.playerO if self.player == self.playerX else self.playerX

        self.label.setText(f'{self.player} turn')

    def check_winner(self):
        for i in range(3):
            if self.btns[i][0].text() == self.btns[i][1].text() == self.btns[i][2].text() != '':
                return True
            if self.btns[0][i].text() == self.btns[1][i].text() == self.btns[2][i].text() != '':
                return True

        if self.btns[0][0].text() == self.btns[1][1].text() == self.btns[2][2].text() != '':
            return True
        if self.btns[0][2].text() == self.btns[1][1].text() == self.btns[2][0].text() != '':
            return True

        return False

    def check_draw(self):
        for row in self.btns:
            for btn in row:
                if btn.text() == '':
                    return False

        return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
# pip install PyQt5
# pip install pyinstaller

import sys
from random import choices
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('form.ui', self)

        self.btnReset.clicked.connect(self.reset)
        self.btnGenerate.clicked.connect(self.generate)

        self.__inputText = self.textEdit
        self.__countPass = self.count_pass
        self.__countSymbol = self.count_symbol

        self.__checkBoxSpecialSymbols = self.specialCharacters
        self.__checkBoxLetters = self.letters
        self.__checkBoxNumbers = self.numbers

    def generate(self):
        SpecialSymbols = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        Numbers = "1234567890"

        password = ""

        if self.__checkBoxSpecialSymbols.isChecked():  # проверка checkbox (TRUE/FALSE)
            password += SpecialSymbols
        if self.__checkBoxLetters.isChecked():  # проверка checkbox (TRUE/FALSE)
            password += Letters
        if self.__checkBoxNumbers.isChecked():  # проверка checkbox (TRUE/FALSE)
            password += Numbers

        if len(password) == 0:
            self.__inputText.setText(
                "Неправильные настройки генерации!")  # установка текста
            return

        countSymbol = self.__countSymbol.value()  # получения числа
        countPass = self.__countPass.value()  # получения числа

        inputText = self.__inputText.toPlainText()  # текст содержимого

        if len(inputText):
            self.__inputText.setText("")  # установка текста

        for i in range(countPass):
            symbol = "".join(choices(password, k=countSymbol))
            self.__inputText.insertPlainText(f"{symbol}\n")  # Добавляет текст

    def reset(self):
        inputText = self.__inputText.toPlainText()
        if len(inputText):
            self.__inputText.setText("")  # установка текста


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

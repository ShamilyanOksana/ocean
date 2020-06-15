from ui.admin import Ui_MainWindow
from PyQt5 import QtWidgets
import sys


class AdminWin(QtWidgets.QMainWindow):
    def __init__(self, house):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.house = house

        self.ui.btn_add.clicked.connect()

    def add_house(self):



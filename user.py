
from ui.user import Ui_MainWindow
from PyQt5 import QtWidgets
import sys


class UserWin(QtWidgets.QMainWindow):
    def __init__(self, house):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.house = house




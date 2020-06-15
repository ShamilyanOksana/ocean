from ui.user import Ui_MainWindow
from PyQt5 import QtWidgets
import sys


class UserWin(QtWidgets.QMainWindow):
    def __init__(self, house, user):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.house = house

        self.user = self.ui.label_user.setText(user)

        #Что-то поменяла




import house
from ui.auth import Ui_MainWindow
import admin
import user
from PyQt5 import QtWidgets
import sys


class MyWin(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.house = house.House()
        self.nextwin = None
        self.adminwin = None
        self.admin = None
        try:
            self.is_admin()
        except Exception:
            pass
        try:
            self.set_accounts()
        except Exception:
            pass
        try:
            self.ui.btn_auth.clicked.connect(self.login)
        except Exception:
            pass

    def set_accounts(self):
        accounts = self.house.get_accounts()
        for i in accounts:
            self.ui.address.addItem(i)

    def is_admin(self):
        self.admin = self.house.get_admin()

    def login(self):
        user_address = self.ui.address.currentText()
        self.house.auth(user_address)
        self.nextwin = user.UserWin(self.house)
        self.nextwin.show()
        if user_address == self.admin:
            self.adminwin = admin.AdminWin(self.house)
            self.adminwin.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())









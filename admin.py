from ui.admin import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import house


class AdminWin(QtWidgets.QMainWindow):
    # def __init__(self, house):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.house = house.House()
        self.set_accounts()
        self.ui.btn_add.clicked.connect(self.add_house)

    def set_accounts(self):
        accounts = self.house.get_accounts()
        for i in accounts:
            self.ui.owner.addItem(i)

    def add_house(self):

        owner = self.ui.owner.currentText()
        address = self.ui.address.text()
        square = self.ui.square.text()
        time = self.ui.time.text()

        self.house.reg_home(owner, address, square, time)

        self.ui.address.clear()
        self.ui.square.clear()
        self.ui.time.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = AdminWin()
    myapp.show()
    sys.exit(app.exec())


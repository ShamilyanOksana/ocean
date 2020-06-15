from ui.user import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import house
import web3
# import sale


class UserWin(QtWidgets.QMainWindow):


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.house = house.House()
        self.user = self.house.user_address
        balance = self.house.w3.eth.getBalance(self.user)
        self.ui.label_user.setText(self.user)
        self.ui.label_balance.setText(str(balance//(10**18)))
        self.T_all_houses()
        self.T_my_houses()
        self.T_my_sales()
        self.T_all_sales()
    #     self.ui.btn_sale.clicked.connect(self.sale)
	#
    def sale(self):
        pass
    #     self.s = sale.SaleWin()
    #     self.s.show()

    def stop_sale(self, sale_ID):
        pass

    def T_all_houses(self):
        result = []
        amount = self.house.get_homes_amount()
        for i in range(amount):
            h = self.house.get_home(i)
            if h[4] == 0:
                r = ['Нет']
            else:
                r = ['Да']
            result.append([i] + h[0:4] + r)

        self.ui.table_register.clear()
        self.ui.table_register.setHorizontalHeaderLabels(
            ['ID', 'Собственник', 'Адрес', 'Общая площадь', 'Срок эксплуатации', 'Продается'])
        self.ui.table_register.setRowCount(len(result))
        self.ui.table_register.setColumnCount(6)
        for i in range(len(result)):
            for j in range(6):
                self.ui.table_register.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))

    def T_my_houses(self):
        result = []
        amount = self.house.get_homes_amount()
        for i in range(amount):
            h = self.house.get_home(i)
            if (h[0] == self.user):
                r = [i] + h[1:4]
                if h[4] == 0:
                    r += ['Нет']
                else:
                    r += ['Да']
                result.append(r)

        self.ui.table_my.clear()
        self.ui.table_my.setHorizontalHeaderLabels(
            ['ID', 'Адрес', 'Общая площадь', 'Срок эксплуатации', 'Продается'])
        self.ui.table_my.setRowCount(len(result))
        self.ui.table_my.setColumnCount(5)
        for i in range(len(result)):
            for j in range(5):
                self.ui.table_my.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))

    def T_my_sales(self):
        result = []
        amount = self.house.get_sales_amount()
        for i in range(amount):
            r = []
            s = [i] + self.house.get_sale(i)
            print(s)
            if (s[2] == self.user and s[5] == 1):
                r.append(i)
                h = self.house.get_home(s[1])
                r.append(h[1])
                r.append(h[2])
                r.append(h[3])
                r.append(s[4])
                print(r)
                result.append(r)

        self.ui.table_my_sale.clear()
        self.ui.table_my_sale.setHorizontalHeaderLabels(
            ['ID объявления', 'Адрес', 'Общая площадь', 'Срок эксплуатации', 'Стоимость'])
        self.ui.table_my_sale.setRowCount(len(result))
        self.ui.table_my_sale.setColumnCount(5)
        for i in range(len(result)):
            for j in range(5):
                self.ui.table_my_sale.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))

    def T_all_sales(self):
        result = []
        amount = self.house.get_sales_amount()
        for i in range(amount):
            r = [i] + self.house.get_sale(i)
            if (r[3] == '0x0000000000000000000000000000000000000000'):
                r[3] = ''
            if r[5] == 0:
                r[5] = 'Отменена'
            elif r[5] == 1:
                r[5] = 'Активна'
            elif r[5] == 2:
                r[5] = 'Завершена'
            result.append(r)

        self.ui.table_sale.clear()
        self.ui.table_sale.setHorizontalHeaderLabels(
            ['ID объявления', 'ID дома', 'Собственник', 'Покупатель', 'Стоимость', 'Статус'])
        self.ui.table_sale.setRowCount(len(result))
        self.ui.table_sale.setColumnCount(6)
        for i in range(len(result)):
            for j in range(6):
                self.ui.table_sale.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = UserWin()
    myapp.show()
    sys.exit(app.exec())
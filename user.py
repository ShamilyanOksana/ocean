from ui.user import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from ui.sale import Ui_Dialog


class UserWin(QtWidgets.QMainWindow):
    def __init__(self, house):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.house = house
        self.user = self.house.user_address
        self.s = None
        self.ui.label_user.setText(self.user)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_tables)
        self.timer.start(10000)
        try:
            self.update_tables()
        except Exception:
            pass
        try:
            self.ui.btn_sale.clicked.connect(self.sale)
        except Exception:
            pass
        try:
            self.ui.btn_cancel.clicked.connect(self.cancel_sale)
        except Exception:
            pass
        try:
            self.ui.btn_buy.clicked.connect(self.buy)
        except Exception:
            pass


    def update_tables(self):
        try:
            balance = self.house.w3.eth.getBalance(self.user)
            self.ui.label_balance.setText(str(balance // (10 ** 18)) + '  ETH')
        except Exception:
            pass
        try:
            self.T_all_houses()
        except Exception:
            pass
        try:
            self.T_my_houses()
        except Exception:
            pass
        try:
            self.T_my_sales()
        except Exception:
            pass
        try:
            self.T_all_sales()
        except Exception:
            pass

    def sale(self):
        row = self.ui.table_my.currentRow()
        house_id = int(self.ui.table_my.item(row, 0).text())
        address = self.ui.table_my.item(row, 1).text()
        s = SaleWin(self.house, house_id, address)
        s.exec_()
        self.update_tables()

    def cancel_sale(self):
        row = self.ui.table_my_sale.currentRow()
        sale_id = int(self.ui.table_my_sale.item(row, 0).text())
        self.house.stop_sale(sale_id)
        self.update_tables()

    def buy(self):
        row = self.ui.table_sale.currentRow()
        sale_id = int(self.ui.table_sale.item(row, 0).text())
        price = int(self.ui.table_sale.item(row, 4).text())
        self.house.buy(sale_id, price)
        self.update_tables()

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
                item = QtWidgets.QTableWidgetItem(str(result[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.ui.table_register.setItem(i, j, item)

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
                item = QtWidgets.QTableWidgetItem(str(result[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.ui.table_my.setItem(i, j, item)

    def T_my_sales(self):
        result = []
        amount = self.house.get_sales_amount()
        for i in range(amount):
            r = []
            s = [i] + self.house.get_sale(i)
            print(s)
            if s[2] == self.user and s[5] == 1:
                r.append(i)
                h = self.house.get_home(s[1])
                r.append(h[1])
                r.append(h[2])
                r.append(h[3])
                r.append(int(s[4]//(10**18)))
                print(r)
                result.append(r)

        self.ui.table_my_sale.clear()
        self.ui.table_my_sale.setHorizontalHeaderLabels(
            ['ID объявления', 'Адрес', 'Общая площадь', 'Срок эксплуатации', 'Стоимость'])
        self.ui.table_my_sale.setRowCount(len(result))
        self.ui.table_my_sale.setColumnCount(5)
        for i in range(len(result)):
            for j in range(5):
                item = QtWidgets.QTableWidgetItem(str(result[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.ui.table_my_sale.setItem(i, j, item)

    def T_all_sales(self):
        result = []
        amount = self.house.get_sales_amount()
        for i in range(amount):
            r = [i] + self.house.get_sale(i)
            r[4] = int(int(r[4])//(10**18))
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
                item = QtWidgets.QTableWidgetItem(str(result[i][j]))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.ui.table_sale.setItem(i, j, item)



class SaleWin(QtWidgets.QDialog):
    def __init__(self, house, house_id, address):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.house = house
        self.house_id = house_id
        self.ui.address.setText(address)
        try:
            self.ui.btn_cancel.clicked.connect(self.close)
        except Exception:
            pass
        try:
            self.ui.btn_sale.clicked.connect(self.sale_house)
        except Exception:
            pass

    def sale_house(self):
        price = int(self.ui.price.text())
        self.house.create_sale(self.house_id, price)
        self.close()

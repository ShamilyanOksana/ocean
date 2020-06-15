# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sale.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.btn_sale = QtWidgets.QPushButton(Dialog)
        self.btn_sale.setGeometry(QtCore.QRect(90, 250, 93, 28))
        self.btn_sale.setObjectName("btn_sale")
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(230, 250, 93, 28))
        self.btn_cancel.setObjectName("btn_cancel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 30, 241, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 151, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.address = QtWidgets.QLabel(Dialog)
        self.address.setGeometry(QtCore.QRect(24, 90, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.address.setFont(font)
        self.address.setText("")
        self.address.setAlignment(QtCore.Qt.AlignCenter)
        self.address.setWordWrap(True)
        self.address.setObjectName("address")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 140, 91, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.price = QtWidgets.QLineEdit(Dialog)
        self.price.setGeometry(QtCore.QRect(150, 180, 111, 22))
        self.price.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.price.setObjectName("price")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(270, 180, 55, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Продажа"))
        self.btn_sale.setText(_translate("Dialog", "Продать"))
        self.btn_cancel.setText(_translate("Dialog", "Отмена"))
        self.label.setText(_translate("Dialog", "Вы хотите продать свою недвидимость"))
        self.label_2.setText(_translate("Dialog", "находящуюся по адресу"))
        self.label_3.setText(_translate("Dialog", "Укажите цену"))
        self.price.setPlaceholderText(_translate("Dialog", "Цена"))
        self.label_4.setText(_translate("Dialog", "ETH"))

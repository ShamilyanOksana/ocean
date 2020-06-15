# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 396)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 50, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 55, 31))
        self.label_2.setObjectName("label_2")
        self.btn_auth = QtWidgets.QPushButton(self.centralwidget)
        self.btn_auth.setGeometry(QtCore.QRect(140, 270, 93, 28))
        self.btn_auth.setObjectName("btn_auth")
        self.address = QtWidgets.QComboBox(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(60, 160, 301, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.address.setFont(font)
        self.address.setObjectName("address")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 376, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вход"))
        self.label.setText(_translate("MainWindow", "ВХОД"))
        self.label_2.setText(_translate("MainWindow", "Адрес"))
        self.btn_auth.setText(_translate("MainWindow", "Войти"))

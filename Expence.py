# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Expense.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem,QMainWindow
from Add import *
from History import *
from Income import *
import psycopg2
from psycopg2 import Error


class Ui_MainWindow(object):
    def Addv(self):
        self.window = QtWidgets.QDialog()
        self.Addv1 = Ui_AddM()
        self.Addv1.setupUi(self.window)
        self.Addv1.InsertD.clicked.connect(self.Insmsg)
        self.window.show()
    def Insmsg(self):
        self.Addv1.ResIns.setText("Success")
    def Incv(self):
        self.window = QtWidgets.QDialog()
        self.Incv1 = Ui_InsM()
        self.Incv1.setupUi(self.window)
        self.window.show()
        self.Incv1.IncAddbt.clicked.connect(self.IncvAdd)
    def IncvAdd(self):
        conn = psycopg2.connect(database="Expenses", user="postgres", password="ketan9850", host="127.0.0.1",port="5432")
        cur = conn.cursor()
        cur.execute('''select exists(select 1 from expense where d::date = date('now'))''')
        c = cur.fetchone()
        if c[0] == True:
            cur.execute('''SELECT incdis FROM expense WHERE d::date = date('now')''')
            odis = cur.fetchone()
            ndis=odis[0]+" "+self.Incv1.IncDis.text()
            cur.execute('''update expense set incdis='%s' where d::date = date('now')'''%ndis)
            conn.commit()
            cur.execute('''update expense set inc=inc+%s where d::date = date('now')'''%(self.Incv1.IncAmount.text()))
            conn.commit()
            self.Res.setText("Date Added successfully")
        else:
            cur.execute('''insert into expense(d,inc,incdis) values (date('now'),%s,'%s') ;''' % (self.Incv1.IncAmount.text(),self.Incv1.IncDis.text()))
            conn.commit()
            self.Res.setText("Date Added successfully")








    def Histv(self):
        self.window = QtWidgets.QDialog()
        self.Histv1 = Ui_HistM()
        self.Histv1.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 655)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ToSpm = QtWidgets.QLCDNumber(self.centralwidget)
        self.ToSpm.setGeometry(QtCore.QRect(660, 70, 141, 41))
        self.ToSpm.setObjectName("ToSpm")
        self.Rem = QtWidgets.QLCDNumber(self.centralwidget)
        self.Rem.setGeometry(QtCore.QRect(230, 130, 141, 41))
        self.Rem.setObjectName("Rem")
        self.Tospe = QtWidgets.QLCDNumber(self.centralwidget)
        self.Tospe.setGeometry(QtCore.QRect(660, 130, 141, 41))
        self.Tospe.setObjectName("Tospe")
        self.Addbt = QtWidgets.QPushButton(self.centralwidget)
        self.Addbt.setGeometry(QtCore.QRect(330, 340, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        self.Addbt.setFont(font)
        self.Addbt.setObjectName("Addbt")
        self.Addbt.clicked.connect(self.Addv)
        self.Histbt = QtWidgets.QPushButton(self.centralwidget)
        self.Histbt.setGeometry(QtCore.QRect(600, 340, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        self.Histbt.setFont(font)
        self.Histbt.setObjectName("Histbt")
        self.Histbt.clicked.connect(self.Histv)
        self.Incbt = QtWidgets.QPushButton(self.centralwidget)
        self.Incbt.setGeometry(QtCore.QRect(90, 340, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        self.Incbt.setFont(font)
        self.Incbt.setObjectName("Incbt")
        self.Incbt.clicked.connect(self.Incv)
        self.MonIncSh = QtWidgets.QLCDNumber(self.centralwidget)
        self.MonIncSh.setGeometry(QtCore.QRect(230, 70, 141, 41))
        self.MonIncSh.setObjectName("MonIncSh")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 80, 161, 26))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 140, 141, 26))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(450, 80, 201, 26))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 140, 121, 26))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 20, 71, 26))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Sedt = QtWidgets.QLabel(self.centralwidget)
        self.Sedt.setGeometry(QtCore.QRect(640, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.Sedt.setFont(font)
        self.Sedt.setText("")
        self.Sedt.setObjectName("Sedt")
        self.Res = QtWidgets.QLabel(self.centralwidget)
        self.Res.setGeometry(QtCore.QRect(200, 500, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.Res.setFont(font)
        self.Res.setText("")
        self.Res.setObjectName("Res")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Expenses Management"))
        self.Addbt.setText(_translate("MainWindow", "Add Expense"))
        self.Histbt.setText(_translate("MainWindow", "History"))
        self.Incbt.setText(_translate("MainWindow", "Add Income"))
        self.label_6.setText(_translate("MainWindow", "Monthly Income"))
        self.label_3.setText(_translate("MainWindow", "Today\'s Spent"))
        self.label_4.setText(_translate("MainWindow", "Total Spent in Month"))
        self.label_5.setText(_translate("MainWindow", "Remaining "))
        self.label_2.setText(_translate("MainWindow", "Date :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

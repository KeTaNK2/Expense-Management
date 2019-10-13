# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'History.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication,QTableWidgetItem

import psycopg2
from psycopg2 import Error
class Ui_HistM(object):
    def sh(self):

        conn = psycopg2.connect(database="Expenses", user="postgres", password="ketan9850", host="127.0.0.1",port="5432")
        cur = conn.cursor()
        cur.execute('''select inc,incdis,spent,Food,Travel,Personal,groc,grodis,bill,billdis,oth,othdis from expense WHERE d::date = '%s' ''' % self.DS.text())
        c = cur.fetchone()
        if c==None :
            self.DSRes.setText("No Data Found ")
        else:
            self.DSRes.setText("Data Found!!!")
            conn.close()
            rowNo=0
            colNo=1
            for columns in c:
                item = QtWidgets.QTableWidgetItem(str(columns))
                self.tableWidget.setItem(rowNo,1, item)

                rowNo += 1

    def setupUi(self, HistM):
        HistM.setObjectName("HistM")
        HistM.resize(777, 542)
        self.SeachTab = QtWidgets.QTabWidget(HistM)
        self.SeachTab.setGeometry(QtCore.QRect(10, 30, 751, 481))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.SeachTab.setFont(font)
        self.SeachTab.setObjectName("SeachTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.DSRbt = QtWidgets.QPushButton(self.tab)
        self.DSRbt.setGeometry(QtCore.QRect(260, 20, 93, 28))
        self.DSRbt.setObjectName("DSRbt")
        self.DSRbt.clicked.connect(self.sh)
        self.DSRes = QtWidgets.QLabel(self.tab)
        self.DSRes.setGeometry(QtCore.QRect(430, 30, 251, 16))
        self.DSRes.setObjectName("DSRes")
        self.DS = QtWidgets.QLineEdit(self.tab)
        self.DS.setGeometry(QtCore.QRect(30, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Nova Square")
        font.setPointSize(18)
        self.DS.setFont(font)
        self.DS.setText("")
        self.DS.setObjectName("DS")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 581, 351))
        self.tableWidget.setRowCount(12)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        self.SeachTab.addTab(self.tab, "")
        self.label = QtWidgets.QLabel(HistM)
        self.label.setGeometry(QtCore.QRect(30, 0, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(HistM)
        self.SeachTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HistM)

    def retranslateUi(self, HistM):
        _translate = QtCore.QCoreApplication.translate
        HistM.setWindowTitle(_translate("HistM", "History"))
        self.DSRbt.setText(_translate("HistM", "Seach"))
        self.DSRes.setText(_translate("HistM", "TextLabel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("HistM", "Discreption"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("HistM", "Value"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("HistM", "Income"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("HistM", "Source"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("HistM", "Today Spent"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("HistM", "Food"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("HistM", "Travel"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("HistM", "Personal"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("HistM", "Groccery"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("HistM", "Gorccery Items"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("HistM", "Bills"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("HistM", "Bill Name"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("HistM", "Other"))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("HistM", "Other Item"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.SeachTab.setTabText(self.SeachTab.indexOf(self.tab), _translate("HistM", "Day"))
        self.label.setText(_translate("HistM", "Seach by :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HistM = QtWidgets.QDialog()
    ui = Ui_HistM()
    ui.setupUi(HistM)
    HistM.show()
    sys.exit(app.exec_())

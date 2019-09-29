import sys
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem,QMainWindow
from Expence import *
from Add import *
from History import *
from Income import *


from datetime import date

x = date.today()

import sqlite3
from sqlite3 import Error
class Expense (QMainWindow) :
    def __init__(self):
        super().__init__()
        self.Exp=Ui_MainWindow()
        self.Exp.setupUi(self)
        self.show()
        self.Exp.Sedt.setText(str(x))

    def Insmsg(self):
        self.Exp.Addv1.ResIns.setText("Success")





if __name__=="__main__" :
   app=QApplication(sys.argv)
   E=Expense()
   E.show()
   sys.exit(app.exec_())

















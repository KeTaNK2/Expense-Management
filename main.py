import sys
from PyQt5.QtWidgets import QDialog,QApplication,QTableWidgetItem,QMainWindow
from Expence import *
from Add import *
from History import *
from Income import *
import psycopg2
from psycopg2 import Error


from datetime import date

x = date.today()




class Expense (QMainWindow) :
    def __init__(self):
        super().__init__()
        self.Exp=Ui_MainWindow()
        self.Exp.setupUi(self)
        self.show()
        self.Exp.Sedt.setText(str(x))
        db = '''create table if not exists Expense(ID  SERIAL PRIMARY KEY,D date,inc int default 0,incdis varchar(100),spent int default 0,Food int default 0,Travel int default 0,Personal int default 0,groc int default 0,grodis varchar(100),bill int default 0,billdis varchar(100),oth int default 0,othdis varchar(100) )'''


        try:
            conn = psycopg2.connect(database="Expenses", user="postgres", password="ketan9850", host="127.0.0.1",port="5432")
            cur = conn.cursor()
            cur.execute(db)
            conn.commit()
            conn.close()
        except Error as e :
            self.Exp.Res.setText("Error")
        finally:
            self.Exp.Res.setText("Done!!")







if __name__=="__main__" :
   app=QApplication(sys.argv)
   E=Expense()
   E.show()
   sys.exit(app.exec_())

















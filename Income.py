# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Income.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InsM(object):
    def setupUi(self, InsM):
        InsM.setObjectName("InsM")
        InsM.resize(640, 480)
        self.label_7 = QtWidgets.QLabel(InsM)
        self.label_7.setGeometry(QtCore.QRect(190, 30, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.IncDis = QtWidgets.QLineEdit(InsM)
        self.IncDis.setGeometry(QtCore.QRect(50, 140, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IncDis.setFont(font)
        self.IncDis.setObjectName("IncDis")
        self.label_8 = QtWidgets.QLabel(InsM)
        self.label_8.setGeometry(QtCore.QRect(60, 90, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.IncAmount = QtWidgets.QLineEdit(InsM)
        self.IncAmount.setGeometry(QtCore.QRect(50, 250, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.IncAmount.setFont(font)
        self.IncAmount.setText("")
        self.IncAmount.setObjectName("IncAmount")
        self.label_9 = QtWidgets.QLabel(InsM)
        self.label_9.setGeometry(QtCore.QRect(60, 200, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.IncAddbt = QtWidgets.QPushButton(InsM)
        self.IncAddbt.setGeometry(QtCore.QRect(120, 350, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        self.IncAddbt.setFont(font)
        self.IncAddbt.setObjectName("IncAddbt")
        self.Resinc = QtWidgets.QLabel(InsM)
        self.Resinc.setGeometry(QtCore.QRect(330, 350, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Sanskrit Text")
        font.setPointSize(12)
        self.Resinc.setFont(font)
        self.Resinc.setText("")
        self.Resinc.setObjectName("Resinc")

        self.retranslateUi(InsM)
        QtCore.QMetaObject.connectSlotsByName(InsM)

    def retranslateUi(self, InsM):
        _translate = QtCore.QCoreApplication.translate
        InsM.setWindowTitle(_translate("InsM", "Income"))
        self.label_7.setText(_translate("InsM", "Add Month Income"))
        self.label_8.setText(_translate("InsM", "Source of  Income"))
        self.label_9.setText(_translate("InsM", "Amount"))
        self.IncAddbt.setText(_translate("InsM", "Add Income"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InsM = QtWidgets.QDialog()
    ui = Ui_InsM()
    ui.setupUi(InsM)
    InsM.show()
    sys.exit(app.exec_())

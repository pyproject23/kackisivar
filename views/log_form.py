# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(821, 508)
        Form.setStyleSheet("* {\n"
"font-size:15px;\n"
"font-family:Century Gothic, sans-serif;\n"
"}\n"
"#Form{\n"
"    background-image: url(:/images/bg.png);\n"
"    background:#28595e\n"
"}\n"
"QLineEdit, QComboBox, QTimeEdit,QTableView{\n"
"color:#333533;\n"
"background:rgba(85,170,255,100);\n"
"font-size:18px;\n"
"border-style:outset;\n"
"border: solid 1px;\n"
"border-radius:10px\n"
"}\n"
"QPushButton{\n"
"background-color:#4361ee;\n"
"border-style:outset;\n"
"border-radius:10px\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:#ef233c;\n"
"border-style:inset;\n"
"border-radius:10px\n"
"}\n"
"QCheckBox{\n"
"background:rgba(85,170,255,0);\n"
"border-style:outset;\n"
"color:white;\n"
"}\n"
"QLabel{\n"
"background:rgba(85,170,255,0);\n"
"color:white;\n"
"font-style:italic bold;\n"
"font-size:14px;\n"
"}")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(20, 80, 781, 411))
        self.tableView.setObjectName("tableView")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 20, 371, 41))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Log Kayıtları"))
        self.pushButton_4.setText(_translate("Form", "Tüm Logları Sil"))
import views.sources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_LogForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from views.log_form import Ui_LogForm
from models.log import Log
from models.veri_model import TableModel
from PyQt5.QtWidgets import QMessageBox,QHeaderView
import pandas as pd


class LogForm(QtWidgets.QWidget, Ui_LogForm):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.log = Log()
        self.setupUi()

    def setupUi(self):
        super().setupUi(self)

        self.pushButton_4.clicked.connect(self.log_temizle)
        # self.tableView.clicked.connect(self.log_sec)
        gelen_veri = self.log.logu_getir()

        veri=[]
        for kayit in gelen_veri:
            kayit = [kayit[0], kayit[1], kayit[2]]
            veri.append(kayit)

        veri = pd.DataFrame(veri, columns=['id', 'Personel Adı', 'Giriş Zamanı'])


        if len(kayit) != 0:
            self.model = TableModel(veri)
            self.tableView.setModel(self.model)
            self.tableView.show()

    def log_temizle(self):
        self.log.logu_sil()
        self.mesaj_ver()

    def mesaj_ver(self):
        self.msg = QMessageBox()
        self.msg.setStyleSheet("background:#28595e;")
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle("Dikkat")
        self.msg.setText("Loglar Silindi")
        self.msg.exec_()
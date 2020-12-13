from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views.kullanicilar_form import Ui_FormKullanici
from models.kullanici import Kullanici
from models.veri_model import TableModel
import pandas as pd


class KullaniciForm(QtWidgets.QWidget, Ui_FormKullanici):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.kullanici = Kullanici()
        self.index = 0
        self.veri = []
        self.kayit_id = 0
        self.setupUi()
        self.tableView.clicked.connect(self.veri_sec)
        self.pushButtonYeniKayit.clicked.connect(self.YeniKayit_Click)
        self.pushButtonSil.clicked.connect(self.Sil_Click)
        self.pushButtonGuncelle.clicked.connect(self.Guncelle_Click)
        self.pushButtonKaydet.clicked.connect(self.Kaydet_Click)
        self.pushButtonVazgec.clicked.connect(self.Vazgec_Click)

    def setupUi(self):
        super().setupUi(self)
        self.pasif()
        self.tableView_listele()

    def tableView_listele(self):
        gelen_veri = self.kullanici.verileri_getir()
        kayit_sayisi = (len(gelen_veri))
        if (kayit_sayisi>0):
            self.veri = []
            for kayit in gelen_veri:
                kayit = [kayit[0], kayit[1], kayit[3], kayit[4], kayit[5]]
                self.veri.append(kayit)
            self.veri = pd.DataFrame(self.veri, columns=['id', 'Kullanıcı Adı','Personel Adı', 'Eposta','Kayıt Tarihi'])

            self.model = TableModel(self.veri)
            self.tableView.setModel(self.model)
            self.verileri_doldur()

    def veri_sec(self):
        try:
            index = self.tableView.currentIndex()
            NewIndex = self.tableView.model().index(index.row(), 0)
            self.index = NewIndex.row()
            self.verileri_doldur()
        except Exception as e:
            self.Mesaj("Hata", "Kayıt bulunamadı", "hata")

    def verileri_doldur(self):
        try:
            self.lineEditKullaniciAdi.setText(self.veri[self.index][1])
            self.lineEditParola.setText(self.veri[self.index][2])
            self.lineEditKullaniciAdiSoyadi.setText(self.veri[self.index][3])
            self.lineEditKullaniciAdi_5.setText(self.veri[self.index][4])
        except Exception as e:
            return

    def YeniKayit_Click(self):
        self.aktif()
        self.kayit_id = 0
        self.lineEditKullaniciAdi.setText("")
        self.lineEditParola.setText("")
        self.lineEditKullaniciAdiSoyadi.setText("")
        self.lineEditKullaniciAdi_5.setText("")

    def Sil_Click(self):
        try:
            self.kayit_id = self.veri[self.index][0]
            if (self.kayit_id > 0):
                cevap = QMessageBox.No
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Question)
                msg.setStyleSheet("background:#28595e;")
                msg.setWindowTitle("Dikkat")
                msg.setText("Silmek istiyormusnuz?")
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg.setDefaultButton(QMessageBox.No)
                cevap=msg.exec_()
                if cevap == QMessageBox.Yes:
                    kullanici2 = Kullanici(self.kayit_id)
                    kullanici2.sil()
                    self.Mesaj("Silme", "Kayıt Başarıyla Silindi","bilgi")
                    self.tableView_listele()
        except Exception as e:
            self.Mesaj("Silme", "Silinecek kayıt bulunamadı", "uyari")


    def Guncelle_Click(self):
        self.kayit_id = self.veri[self.index][0]
        self.aktif()

    def Kaydet_Click(self):
        self.pasif()
        try:
            kullanici_adi = str.strip(self.lineEditKullaniciAdi.text())
            kullanici_parola = str.strip(self.lineEditParola.text())
            personel_adi_soyadi = self.lineEditKullaniciAdiSoyadi.text()
            personel_mail_adresi = str.strip(self.lineEditKullaniciAdi_5.text())
            kullanici1 = Kullanici(self.kayit_id, kullanici_adi, kullanici_parola, personel_adi_soyadi,
                                    personel_mail_adresi)
            kullanici1.kaydet()
            if (self.kayit_id > 0):
                self.Mesaj("Kayıt","Kayıt Güncellendi")
            else:
                self.Mesaj("Kayıt", "Yeni Kayıt Eklendi")
            self.tableView_listele()
        except Exception as e:
            self.Mesaj("Kaydet", "Kayıt yapılırken hata oluştu.", "hata")

    def Vazgec_Click(self):
        self.pasif()
        self.kayit_id = 0

    def aktif(self):
        self.groupBoxVeriler.setEnabled(True)
        self.pushButtonKaydet.setEnabled(True)
        self.pushButtonVazgec.setEnabled(True)
        self.tableView.setEnabled(False)
        self.pushButtonYeniKayit.setEnabled(False)
        self.pushButtonGuncelle.setEnabled(False)
        self.pushButtonSil.setEnabled(False)

    def pasif(self):
        self.groupBoxVeriler.setEnabled(False)
        self.pushButtonKaydet.setEnabled(False)
        self.pushButtonVazgec.setEnabled(False)
        self.tableView.setEnabled(True)
        self.pushButtonYeniKayit.setEnabled(True)
        self.pushButtonGuncelle.setEnabled(True)
        self.pushButtonSil.setEnabled(True)

    def Mesaj(self, baslik="", mesaj="",ikon="bilgi"):
        msg1 = QMessageBox()
        if (ikon=="bilgi"):
            msg1.setIcon(QMessageBox.Information)
        elif(ikon=="uyari"):
            msg1.setIcon(QMessageBox.Warning)
        else:
            msg1.setIcon(QMessageBox.Critical)
        msg1.setStyleSheet("background:#28595e;")
        msg1.setWindowTitle(baslik)
        msg1.setText(mesaj)
        msg1.exec_()
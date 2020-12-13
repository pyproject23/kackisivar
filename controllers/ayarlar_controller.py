from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from views.ayarlar_form import Ui_AyarlarForm
from models.ayarlar import Ayarlar
from models.kullanici import Kullanici
# from datetime import time, datetime


class AyarlarForm(QtWidgets.QWidget, Ui_AyarlarForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kullanici = Kullanici()
        self.setupUi()
        self.ayarlar = Ayarlar().ayarlari_getir()
        self.pushButton.clicked.connect(self.ayarlari_guncelle)

    def setupUi(self):
        super().setupUi(self)
        self.verileri_doldur()

    def verileri_doldur(self):
        try:
            self.ayarlar = Ayarlar().ayarlari_getir()
            self.lineEditOkulAdi.setText(self.ayarlar[3])
            self.comboBoxGorevli.clear()
            kullanicilar = self.kullanici.verileri_getir()
            self.comboBoxGorevli.addItem(self.ayarlar[1], self.ayarlar[4])
            for k in kullanicilar:
                self.comboBoxGorevli.addItem(k[3], k[0])
            saat = str.split(self.ayarlar[5], ":")
            saat = [int(i) for i in saat]
            self.timeEditMailSaat.setTime(QtCore.QTime(*saat))
            self.lineEditKameraTipi.setText(self.ayarlar[6])
            self.lineEditKameraAyari.setText(self.ayarlar[7])
            self.lineEditKisiLimiti.setText(str(self.ayarlar[8]))
            self.lineEditSmtpAdres.setText(self.ayarlar[9])
            self.lineEditSmtpKulAdi.setText(self.ayarlar[10])
            self.lineEditSmtpParola.setText(self.ayarlar[11])
            self.lineEditSmtpPortNo.setText(str(self.ayarlar[12]))
            self.checkBoxTLS.setChecked(self.ayarlar[13])
        except Exception as e:
            return
    def ayarlari_guncelle(self):
        try:
            okul = str.strip(self.lineEditOkulAdi.text())
            gorevli_id = self.comboBoxGorevli.itemData(self.comboBoxGorevli.currentIndex())
            mail_saati = self.timeEditMailSaat.text()
            kamera_turu = str.strip(self.lineEditKameraTipi.text())
            kamera_ayari = str.strip(self.lineEditKameraAyari.text())
            kisi_siniri = str.strip(self.lineEditKisiLimiti.text())
            smtp_server_adres = str.strip(self.lineEditSmtpAdres.text())
            smtp_kullanici_adi = str.strip(self.lineEditSmtpKulAdi.text())
            smtp_kullanici_parola = str.strip(self.lineEditSmtpParola.text())
            smtp_port_numarasi = str.strip(self.lineEditSmtpPortNo.text())
            if self.checkBoxTLS.isChecked():
                smtp_tls = 1
            else:
                smtp_tls = 0
            Ayarlar.kaydet(id=1, okul_adi=okul, gorevli_id=gorevli_id, mail_gonderme_saati=mail_saati, kamera_turu=kamera_turu, kamera_ayari=kamera_ayari, kisi_siniri=kisi_siniri, smtp_server_adres=smtp_server_adres, smtp_kullanici_adi=smtp_kullanici_adi, smtp_kullanici_parola=smtp_kullanici_parola, smtp_port_numarasi=smtp_port_numarasi, smtp_tls=smtp_tls)
            self.verileri_doldur()
            # print(smtp_tls)
            # print("güncelle")
        except Exception as e:
            self.Mesaj("Hata", "Kayıt işlemi gerçekleştirilemedi", "hata")

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
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from views.anaekran import Ui_MainWindow
from models.kullanici import *
from models.gunluk_rapor import GunlukRapor
from models.ayarlar import Ayarlar
from controllers.menu_controller import AnaMenu
from controllers.goruntu_isleme import GoruntuIsleme
from controllers.mail_uyari import Mail
from controllers.mail_gunluk_rapor import Mail_Gunluk_Rapor
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from controllers.grafik_saatlik import SaatlikGrafik
from models.veri_tasi import Veri
import datetime


class AnaEkran(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        super().__init__(self)
        self.ana_menu = AnaMenu()
        # global gelen ve giden değerlerinin bir önceki değerlerini saklamak için
        self.gelen_onceki_deger = 0
        self.giden_onceki_deger = 0

        # Kişi Sınırını al
        self.ayarlar = Ayarlar.ayarlari_getir()
        # print(self.ayarlar)
        self.kisi_siniri = self.ayarlar[8]
        self.kisi_siniri_mail_gonderildi = False
        # Günlkük rapor için mail gönderim saatini al
        self.mail_gonderim_saati = self.ayarlar[5]
        self.gunluk_rapor_maili_gonderildi_mi = False

        # global sayici değişkeni tanımla
        self.sayici = None
        # Günlük rapor maili için zamanlama nesnesi
        mail_gunluk_rapor = Mail_Gunluk_Rapor(self)
        mail_gunluk_rapor.start()

        # günlük grafik için plot
        self.gunluk_rapor = GunlukRapor()
        self.gunluk_grafik = plt

        self.setupUi(self)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.menuAyarlar.triggered.connect(self.show_ayarlar)
        self.menuKullanicilar.triggered.connect(self.show_kullanicilar)
        self.menuLoglar.triggered.connect(self.show_log)
        self.menuAnasayfa.triggered.connect(self.kapat)
        self.menuHakkinda.triggered.connect(self.show_hakkimizda)
        self.pushButtonBaslat.clicked.connect(self.sayima_basla)
        self.verticalLayoutGun.addWidget(FigureCanvas(self.gunluk_grafik.figure(figsize=(10, 5))))
        g_ad = self.ayarlar[1]
        g_eposta = self.ayarlar[14]
        self.statusbar.showMessage(f"Görevli :{g_ad} - E-posta: {g_eposta}")
        self.statusbar.setStyleSheet("color:white; font-size:13px;")
        # icon = QtGui.QIcon()
        # icon.addFile(u"../images/nokta.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.setWindowIcon(icon)

        self.gunluk_grafik_ciz()

        self.saatlik_rapor = GunlukRapor()
        self.saatlik_grafik = SaatlikGrafik(self, self.saatlik_rapor)
        self.saatlik_grafik.start()

        self.verticalLayoutSaat.addWidget(FigureCanvas(self.saatlik_grafik.plt.figure(figsize=(10, 5))))

    def show_ayarlar(self):
        Veri.anaekran = self
        self.ana_menu.show_ayarlar()

    def show_kullanicilar(self):
        Veri.anaekran = self
        self.ana_menu.show_kullanicilar()

    def show_log(self):
        Veri.anaekran = self
        self.ana_menu.show_log()

    def show_hakkimizda(self):
        self.ana_menu.show_hakkimizda()

    def kapat(self):
        QtCore.QCoreApplication.quit()

    def sayima_basla(self):
        if self.sayici is not None or self.sayici:
            self.sayici.cap.release()
            self.sayici.quit()

        self.sayici = GoruntuIsleme(self)

        if self.radioButtonDemo.isChecked():
            self.radioButtonCanli.setChecked(False)
            self.sayici.sayim_tipi = "demo"

        if self.radioButtonCanli.isChecked():
            self.radioButtonDemo.setChecked(False)
            self.sayici.sayim_tipi = "canli"

        self.sayici.changePixmap.connect(self.setImage)
        self.sayici.start()
        self.gelen_onceki_deger = 0
        self.giden_onceki_deger = 0

    @pyqtSlot(QImage)
    def setImage(self, image):
        # label içinde video gösterme
        self.label_video.setPixmap(QPixmap.fromImage(image))

        gelen = self.sayici.cnt_down + int(self.sayici.count_down)
        giden = self.sayici.cnt_up + int(self.sayici.count_up)
        mevcut = gelen - giden
        # anlık giriş çıkış verisi
        self.label_giren_sayisi.setText("GİDEN:"+str(giden)+" GELEN:"+str(gelen)+" İÇERİDE:"+str(mevcut))
        # Gelen ve giden değerleri  gelen_giden_veriyi_yaz metoduna gönderilecek
        self.gelen_giden_veriyi_yaz(gelen, giden)

        # kişi sınırını kontrol et
        icerideki_kisi_sayisi = int(gelen)-int(giden)
        if icerideki_kisi_sayisi >= self.kisi_siniri and self.kisi_siniri_mail_gonderildi is False:
            print("mail gönderildi")
            mesaj = "<h1>KAÇKİŞİVAR Programı Uyarı Mesajı</h1><br>"+"Gelen:"+str(gelen)+"<br>"+"Giden:"+str(giden)+"<br>"+"Kişi Sınırı:"+str(self.kisi_siniri)+" kişiyi geçmiştir."
            baslik = "Kişi Sınırı Aşıldı..."
            uyari_maili_gonder = Mail(self)
            uyari_maili_gonder.yazi = mesaj
            uyari_maili_gonder.baslik = baslik
            uyari_maili_gonder.start()
            uyari_maili_gonder.quit()
            self.kisi_siniri_mail_gonderildi = True

        # içerideki kişi sayısı sınrıdan küçük ise tekrar mail gönderebilmek için kisi_siniri_mail_gonderildi = False yapılacak
        if (self.kisi_siniri_mail_gonderildi is True and icerideki_kisi_sayisi < self.kisi_siniri):
            self.kisi_siniri_mail_gonderildi = False

    def gelen_giden_veriyi_yaz(self, gelen_sayisi, giden_sayisi):
        if (self.gelen_onceki_deger != gelen_sayisi):
            # Gelen sayısı toplam geldiği için önceki değerden çıkarılarak anlık gelen sayısı bulunuyor
            gelen_anlik_sayi = int(gelen_sayisi)-int(self.gelen_onceki_deger)
            zaman = datetime.datetime.now()
            # Veri tabana kaydet
            # durum=0 Gelen olduğunu belirtiyor
            if self.radioButtonCanli.isChecked():
                gunluk_rapor = GunlukRapor(None, zaman, 0, gelen_anlik_sayi)
                gunluk_rapor.kaydet()
            print("Gelen:"+str(gelen_anlik_sayi)+" Zaman:"+str(zaman))
            self.gelen_onceki_deger = gelen_sayisi

        if (self.giden_onceki_deger != giden_sayisi):
            # Giden sayısı toplam geldiği için önceki değerden çıkarılarak anlık giden sayısı bulunuyor
            giden_anlik_sayi = int(giden_sayisi)-int(self.giden_onceki_deger)
            zaman = datetime.datetime.now()
            # Veri tabana kaydet
            # durum=1 Giden olduğunu belirtiyor
            if self.radioButtonCanli.isChecked():
                gunluk_rapor = GunlukRapor(None, zaman, 1, giden_anlik_sayi)
                gunluk_rapor.kaydet()
            print("Giden:"+str(giden_anlik_sayi)+" Zama:"+str(zaman))
            self.giden_onceki_deger = giden_sayisi

    def gunluk_grafik_ciz(self):
        try:
            self.gunluk_rapor = GunlukRapor()
            self.gunluk_veri = self.gunluk_rapor.gunluk_giris_cikis_verisini_al()
            print(self.gunluk_veri)

            self.giris_gun = [float(s) for s in self.gunluk_veri["Gün"]]
            self.gunluk_grafik.bar(self.giris_gun, self.gunluk_veri["Giriş Sayısı"], label="Gelen", width=.5)

            self.cikis_gun = [float(s)+0.2 for s in self.gunluk_veri["Gün"]]
            self.gunluk_grafik.bar(self.cikis_gun, self.gunluk_veri["Çıkış Sayısı"], label="Giden", color='r',width=.5)

            self.gunluk_grafik.legend()
            self.gunluk_grafik.xlabel('Günler ')
            self.gunluk_grafik.ylabel('Kişi Sayı')
            self.gunluk_grafik.title('Günlük Rapor')
            del self.gunluk_rapor
            self.gunluk_grafik.draw()
        except:
            pass

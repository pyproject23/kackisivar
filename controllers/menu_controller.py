from controllers.ayarlar_controller import AyarlarForm
from controllers.kullanici_controller import KullaniciForm
from controllers.log_controller import LogForm
from controllers.hakkimizda_controller import Hakkimizda_Form
from models.veri_tasi import Veri
from models.ayarlar import Ayarlar
from PyQt5.QtWidgets import QMessageBox


class AnaMenu:

    def __init__(self):
        self.anaekran = None

    def show_kullanicilar(self):
        if self.login():
            self.kullanicilar = KullaniciForm()
            self.kullanicilar.show()
        else:
            self.Mesaj("Kullanıcılar ekranını sadece görevli görebilir")

    def show_ayarlar(self):
        if self.login():
            self.ayarlar = AyarlarForm()
            self.ayarlar.show()
        else:
            self.Mesaj("Ayarlar ekranını sadece görevli görebilir")

    def show_log(self):
        if self.login():
            self.log = LogForm()
            self.log.show()
        else:
            self.Mesaj("Logları sadece görevli görebilir")

    def show_hakkimizda(self):
        self.hakkimizda = Hakkimizda_Form()
        self.hakkimizda.show()

    def login(self):
        login_id = Veri.giris_kullanicisi[0]
        gorevli_id = Ayarlar.ayarlari_getir()[4]
        if int(login_id) == int(gorevli_id):
            return True
        return False

    def Mesaj(self,  mesaj="", ikon="bilgi"):
        g_ad = Ayarlar.ayarlari_getir()[1]
        g_eposta = Ayarlar.ayarlari_getir()[14]
        Veri.anaekran.statusbar.showMessage(f"Görevli :{g_ad} - E-posta: {g_eposta}")
        mesajKutusu = QMessageBox()
        mesajKutusu.setIcon(QMessageBox.Critical)
        mesajKutusu.setStyleSheet("background:#28595e; color:white;")
        mesajKutusu.setWindowTitle("Sınırlı Yetkili Kullanıcı")
        mesajKutusu.setText(mesaj)
        mesajKutusu.exec_()

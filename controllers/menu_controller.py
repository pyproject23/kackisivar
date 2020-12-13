from controllers.ayarlar_controller import AyarlarForm
from controllers.kullanici_controller import KullaniciForm
from controllers.log_controller import LogForm
from controllers.hakkimizda_controller import Hakkimizda_Form


class AnaMenu:

    def __init__(self):
        pass

    def show_kullanicilar(self):
        self.kullanicilar = KullaniciForm()
        self.kullanicilar.show()

    def show_ayarlar(self):
        self.ayarlar = AyarlarForm()
        self.ayarlar.show()

    def show_log(self):
        self.log = LogForm()
        self.log.show()

    def show_hakkimizda(self):
        self.hakkimizda= Hakkimizda_Form()
        self.hakkimizda.show()
       

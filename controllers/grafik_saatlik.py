# from models.gunluk_rapor import GunlukRapor
from PyQt5.QtCore import QThread
from matplotlib import pyplot as plt
# import time


class SaatlikGrafik(QThread):

    def __init__(self, parent, rapor=None):
        super().__init__(parent)
        self.plt = plt
        self.rapor = rapor
        # self.saatlik_veri = saatlik_veri
        self.saatlik_veri = None
        # self.saatlik_veri = self.rapor.saatlik_giris_cikis_verisini_al()
        self.giris_saat = 0
        self.giris_sayi = 0
        self.cikis_saat = 0

    def run(self):
        try:
            self.saatlik_veri = self.rapor.saatlik_giris_cikis_verisini_al()
            print(self.saatlik_veri)

            self.giris_saat = [float(s) for s in self.saatlik_veri["Saat"]]
            self.giris_sayi = [int(s) for s in self.saatlik_veri["Giriş Sayısı"]]
            self.plt.bar(self.giris_saat, self.giris_sayi, label="Gelen", width=.5)

            self.cikis_saat = [float(s)+0.2 for s in self.saatlik_veri["Saat"]]
            self.cikis_sayi = [int(s) for s in self.saatlik_veri["Çıkış Sayısı"]]
            self.plt.bar(self.cikis_saat, self.cikis_sayi, label="Giden", color='r',width=.5)

            self.plt.legend()
            self.plt.xlabel('Saatler ')
            self.plt.ylabel('Kişi Sayı')
            self.plt.title('Saatlik Rapor')

            self.plt.draw()
        except:
            pass

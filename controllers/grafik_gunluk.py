from models.ayarlar import Ayarlar
from models.gunluk_rapor import GunlukRapor
from PyQt5.QtCore import QThread
from matplotlib import pyplot as plt
import pandas as pd
import datetime
import time


class GunlukGrafik(QThread):

    def __init__(self, parent):
        super().__init__(parent)
        self.plt = plt
        self.rapor = None
        # self.rapor = GunlukRapor()
        self.gunluk_veri = None
        self.giris_gun = 0
        self.cikis_gun = 0

    def run(self):
        # try:
        self.rapor = GunlukRapor()
        self.gunluk_veri = self.rapor.gunluk_giris_cikis_verisini_al()
        # pd_veri = pd.DataFrame(gunluk_veri, columns=["Saat", "Giriş/Çıkış", "Sayı"])
        # saatler = pd_veri["Saat"]
        print(self.gunluk_veri)
        self.giris_gun = [float(s) for s in self.gunluk_veri["Gün"]]
        self.plt.bar(self.giris_gun, self.gunluk_veri["Giriş Sayısı"], label="Gelen", width=.5)
        self.cikis_gun = [float(s)+0.2 for s in self.gunluk_veri["Gün"]]
        self.plt.bar(self.cikis_gun, self.gunluk_veri["Çıkış Sayısı"], label="Giden", color='r',width=.5)
        self.plt.legend()
        self.plt.xlabel('Günler ')
        self.plt.ylabel('Kişi Sayı')
        self.plt.title('Saatlik Rapor')

        self.plt.draw()
        # except:
        #    return

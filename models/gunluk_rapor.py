from models.db import DB
from datetime import datetime


class GunlukRapor:

    def __init__(self, id=None, zaman=None, durum=None, sayi=None):
        self.id = id
        self.zaman = zaman
        self.durum = durum
        self.sayi = sayi

    def kaydet(self):
        DB.baglan()

        if self.id is None:
            sorgu = "INSERT INTO gunluk_rapor (zaman, durum, sayi) VALUES (?,?,?)"
            veri = [self.zaman, self.durum, self.sayi]
        else:
            sorgu = "UPDATE gunluk_rapor SET zaman=?, durum=?, sayi=? WHERE id=?"
            veri = [self.zaman, self.durum, self.sayi, self.id]

        DB.imlec.execute(sorgu, veri)
        DB.baglantiyi_kapat()

    def sil(self):
        DB.baglan()
        sorgu = "DELETE FROM gunluk_rapor WHERE id=?"
        veri = [self.id, ]
        DB.imlec.execute(sorgu, veri)
        DB.baglantiyi_kapat()

    def tum_raporlari_sil(self):
        DB.baglan()
        sorgu = "DELETE FROM gunluk_rapor"
        DB.imlec.execute(sorgu)
        DB.baglantiyi_kapat()

    def verileri_getir(self):
        DB.baglan()
        DB.imlec.execute("SELECT * FROM gunluk_rapor ORDER BY id DESC")
        kayitlar = DB.imlec.fetchall()
        DB.baglantiyi_kapat()
        return kayitlar


if __name__ == "__main__":
    rapor = GunlukRapor()
    rapor.verileri_getir()

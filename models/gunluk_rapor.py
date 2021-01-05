# from db import DB
from models.db import DB
from datetime import datetime
import pandas as pd


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

    def gunluk_giris_sayisini_ver(self):
        DB.baglan()
        DB.imlec.execute("select sum(sayi) from gunluk_rapor where durum = 0 and date(zaman) = date('now','localtime')")
        giris_sayisi = DB.imlec.fetchone()
        DB.baglantiyi_kapat()
        return giris_sayisi[0]

    def gunluk_cikis_sayisini_ver(self):
        DB.baglan()
        DB.imlec.execute("select sum(sayi) from gunluk_rapor where durum = 1 and date(zaman) = date('now','localtime')")
        giden_sayisi = DB.imlec.fetchone()
        DB.baglantiyi_kapat()
        return giden_sayisi[0]

    def saatlik_giris_cikis_verisini_al(self):
        DB.baglan()
        # DB.imlec.execute("select strftime('%H',zaman) as saat, durum, sum(sayi) as toplam  from gunluk_rapor where  date(zaman) = date('2020-12-12') GROUP BY strftime('%H',zaman),durum;")
        DB.imlec.execute("select strftime('%H',zaman) as saat, durum, sum(sayi) as toplam  from gunluk_rapor where  date(zaman) = date('now','localtime') GROUP BY strftime('%H',zaman),durum;")
        sonuclar = DB.imlec.fetchall()
        DB.baglantiyi_kapat()
        saatler = [kayit[0] for kayit in sonuclar if kayit[1] == 0]
        giris = [kayit[2] for kayit in sonuclar if kayit[1] == 0]
        cikis = [kayit[2] for kayit in sonuclar if kayit[1] == 1]
        __kayitlar = pd.DataFrame()
        __kayitlar["Saat"] = pd.Series(saatler)
        __kayitlar["Giriş Sayısı"] = pd.Series(giris)
        __kayitlar["Çıkış Sayısı"] = pd.Series(cikis)
        return __kayitlar

    def gunluk_giris_cikis_verisini_al(self):
        DB.baglan()
        DB.imlec.execute("select strftime('%d',zaman) as gun, durum, sum(sayi) as toplam  from gunluk_rapor Where strftime('%Y-%m',zaman) = strftime('%Y-%m',date('now','localtime'))   GROUP BY strftime('%d',zaman),durum;")
        # DB.imlec.execute("select strftime('%d',zaman) as gun, durum, sum(sayi) as toplam  from gunluk_rapor Where strftime('%Y-%m',zaman) = strftime('%Y-%m',date('2020-12-12'))   GROUP BY strftime('%d',zaman),durum;")
        sonuclar = DB.imlec.fetchall()
        DB.baglantiyi_kapat()
        gunler = [kayit[0] for kayit in sonuclar if kayit[1] == 0]
        giris = [kayit[2] for kayit in sonuclar if kayit[1] == 0]
        cikis = [kayit[2] for kayit in sonuclar if kayit[1] == 1]
        __kayitlar = pd.DataFrame()
        __kayitlar["Gün"] = pd.Series(gunler)
        __kayitlar["Giriş Sayısı"] = pd.Series(giris)
        __kayitlar["Çıkış Sayısı"] = pd.Series(cikis)
        return __kayitlar


if __name__ == "__main__":
    rapor = GunlukRapor()
    rapor.verileri_getir()

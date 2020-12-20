import os
import sqlite3 as sql
from datetime import datetime
import models.db


class Kullanici:

    def __init__(self, id=None, kullanici_adi=None, kullanici_parola=None,personel_adi_soyadi=None, personel_mail_adresi=None):
        self.id = id
        self.kullanici_adi = kullanici_adi
        self.kullanici_parola = kullanici_parola
        self.personel_adi_soyadi = personel_adi_soyadi
        self.personel_mail_adresi = personel_mail_adresi
        self.kayit_tarihi = datetime.now()

        self.veritabani = "kackisivar.sqlite"
        self.dosya = os.path.abspath(__file__)
        self.dosya = str.rstrip(self.dosya, "kullanici.py")
        self.dosya += self.veritabani
        print(self.dosya)
        self.vt = ""
        self.imlec = ""
        self.veritabani_olusmus_mu = False
        self.baglan()

    def baglan(self):
        self.veritabani_olusmus_mu = os.path.exists(self.dosya)
        if not self.veritabani_olusmus_mu:
            models.db.olustur()
        else:
            print("{} veritabanı dosyası mevcut!".format(self.veritabani))
        self.vt = sql.connect(self.dosya)
        self.imlec = self.vt.cursor()

    def kaydet(self):
        self.baglan()
        if self.id is None:
            sorgu = "INSERT INTO kullanicilar\n"
            "(kullanici_adi, kullanici_parola, personel_adi_soyadi,\n"
            "personel_mail_adresi, kayit_tarihi) \n"
            "VALUES (?, ?, ?, ?, ?)"
            veri =[self.kullanici_adi, self.kullanici_parola, self.personel_adi_soyadi, self.personel_mail_adresi, self.kayit_tarihi]
        else:
            sorgu = "UPDATE kullanicilar SET kullanici_adi=?, kullanici_parola=?, personel_adi_soyadi=?, personel_mail_adresi=?, kayit_tarihi=? WHERE id=?"
            veri =[self.kullanici_adi, self.kullanici_parola, self.personel_adi_soyadi, self.personel_mail_adresi, self.kayit_tarihi, self.id]

        self.imlec.execute(sorgu, veri)
        self.vt.commit()
        self.vt.close()

    def sil(self):
        self.baglan()
        sorgu = "DELETE FROM kullanicilar WHERE id=?"
        veri = [self.id, ]
        self.imlec.execute(sorgu, veri)
        self.vt.commit()
        self.vt.close()

    def verileri_getir(self):
        self.baglan()
        self.imlec.execute("SELECT * FROM kullanicilar")
        kayitlar = self.imlec.fetchall()
        self.vt.commit()
        self.vt.close()
        return kayitlar

    def giris_yap(self, k_adi, parola):
        self.baglan()
        sorgu = "SELECT * FROM kullanicilar WHERE kullanici_adi=? AND kullanici_parola=?"
        veri = [k_adi, parola]
        self.imlec.execute(sorgu, veri)
        login = self.imlec.fetchone()
        self.vt.commit()
        self.vt.close()
        return login
"""
# select k.id, k.personel_adi_soyadi, a.id, a.okul_adi, a.gorevli_id,
a.mail_gonderme_saati, a.kamera_turu, a.kamera_ayari, a.kisi_siniri,
a.smtp_server_adres, a.smtp_kullanici_adi, a.smtp_kullanici_parola,
a.smtp_port_numarasi, a.smtp_tls from ayarlar as a, kullanicilar as k
where a.gorevli_id = k.id
"""

if __name__ == "__main__":
    """
    kullanici = Kullanici(kullanici_adi="eray", kullanici_parola="er123", personel_adi_soyadi="Eray Taştekin", personel_mail_adresi="eray_tastekin@hotmail.com")
    kullanici.kaydet()
    kullanici = Kullanici(kullanici_adi="hamdi", kullanici_parola="ha123", personel_adi_soyadi="Hamdii Gümüş", personel_mail_adresi="hamdigumus@tutamail.com")
    kullanici.kaydet()
    kullanici = Kullanici(kullanici_adi="harun", kullanici_parola="ha123", personel_adi_soyadi="Harun Yıldız", personel_mail_adresi="h.yildiz@msn.com")
    kullanici.kaydet()
    kullanici = Kullanici(kullanici_adi="ismail", kullanici_parola="is123", personel_adi_soyadi="İsmail Ay", personel_mail_adresi="isml76@yahoo.com")
    kullanici.kaydet()
    kullanici = Kullanici(kullanici_adi="tahir", kullanici_parola="ta123", personel_adi_soyadi="Tahir Battal", personel_mail_adresi="tahirbattal@gmail.com")
    kullanici.kaydet()
    kullanici = Kullanici(id=5,kullanici_adi="tahir", kullanici_parola="tb123", personel_adi_soyadi="Tahir Battal", personel_mail_adresi="tahirbattal@gmail.com")
    kullanici.kaydet()
    kullanici = Kullanici(id=6)
    kullanici.sil()
    """
    kullanici = Kullanici()
    kullanici.verileri_getir()

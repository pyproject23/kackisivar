# import os
# import sqlite3 as sql
# import models.db
from models.db_deneme import DB


class Ayarlar:

    @staticmethod
    def kaydet(id=None, okul_adi=None, gorevli_id=None, mail_gonderme_saati=None, kamera_turu=None, kamera_ayari=None, kisi_siniri=None, smtp_server_adres=None, smtp_kullanici_adi=None, smtp_kullanici_parola=None, smtp_port_numarasi=None, smtp_tls=None, silinecek=False):
        """
        veritabani = "kackisivar.sqlite"
        dosya = os.path.abspath(__file__)
        dosya = str.rstrip(dosya, "ayarlar.py")
        dosya += veritabani
        # print(dosya)
        veritabani_olusmus_mu = os.path.exists(dosya)

        if not veritabani_olusmus_mu:
            models.db.olustur()
        else:
            print("{} veritabanı dosyası mevcut!".format(veritabani))

        vt = sql.connect(dosya)
        imlec = vt.cursor()
        """
        DB.baglan()

        sorgu = "UPDATE ayarlar SET okul_adi=?, gorevli_id=?, mail_gonderme_saati=?, kamera_turu=?, kamera_ayari=?, kisi_siniri=?, smtp_server_adres=?, smtp_kullanici_adi=?, smtp_kullanici_parola=?, smtp_port_numarasi=?, smtp_tls=? WHERE id=?"

        veri =[okul_adi, gorevli_id, mail_gonderme_saati, kamera_turu, kamera_ayari, kisi_siniri, smtp_server_adres, smtp_kullanici_adi, smtp_kullanici_parola, smtp_port_numarasi, smtp_tls, id]

        DB.imlec.execute(sorgu, veri)
        DB.baglantiyi_kapat()
        # imlec.execute(sorgu, veri)
        # vt.commit()
        # vt.close()

    @staticmethod
    def ayarlari_getir():
        """
        veritabani = "kackisivar.sqlite"
        dosya = os.path.abspath(__file__)
        dosya = str.rstrip(dosya, "ayarlar.py")
        dosya += veritabani
        # print(dosya)
        veritabani_olusmus_mu = os.path.exists(dosya)
        # print(dosya)

        if not veritabani_olusmus_mu:
            models.db.olustur()
        else:
            print("Ayarlar:{} veritabanı dosyası mevcut!".format(veritabani))

        vt = sql.connect(dosya)
        imlec = vt.cursor()
        """

        DB.baglan()
        DB.imlec.execute("select k.id, k.personel_adi_soyadi, a.id, a.okul_adi, a.gorevli_id, a.mail_gonderme_saati, a.kamera_turu, a.kamera_ayari, a.kisi_siniri, a.smtp_server_adres, a.smtp_kullanici_adi, a.smtp_kullanici_parola, a.smtp_port_numarasi, a.smtp_tls from ayarlar as a, kullanicilar as k where k.id = a.gorevli_id")
        ayarlar = DB.imlec.fetchone()
        # print(kayit)
        return ayarlar


if __name__ == "__main__":
    # pass
    # Ayarlar.kaydet(id=1, okul_adi="PyProject MTAL", gorevli_id=4, mail_gonderme_saati="20:00", kamera_turu="USB", kamera_ayari=None, kisi_siniri=15, smtp_server_adres="127.0.0.1", smtp_kullanici_adi="admin@localhost", smtp_kullanici_parola="12345", smtp_port_numarasi=587, smtp_tls=None)
    # Ayarlar.kaydet(silinecek=True)
    Ayarlar.ayarlari_getir()

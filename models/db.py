import sqlite3 as sql
import os


class DB:
    veritabani = "kackisivar.sqlite"

    @staticmethod
    def olustur():
        veritabani = "kackisivar.sqlite"
        dosya = os.path.abspath(__file__)
        dosya = str.rstrip(dosya, "db.py")
        dosya += veritabani
        vt = sql.connect(dosya)
        imlec = vt.cursor()

        imlec.execute('CREATE TABLE "kullanicilar" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "kullanici_adi" TEXT(20), "kullanici_parola" TEXT(20), "personel_adi_soyadi" TEXT(100), "personel_mail_adresi" TEXT(250), "kayit_tarihi" TEXT(50) )')

        imlec.execute('CREATE TABLE "ayarlar" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "okul_adi" TEXT(250), "gorevli_id" INTEGER, "mail_gonderme_saati" TEXT(5), "usb_id" int(1), "demo_video" TEXT(250), "kisi_siniri" INTEGER, "smtp_server_adres" TEXT(100), "smtp_kullanici_adi" TEXT(50), "smtp_kullanici_parola" TEXT(50), "smtp_port_numarasi" INTEGER DEFAULT 587, "smtp_tls" INTEGER DEFAULT 1 )')

        imlec.execute('CREATE TABLE "gunluk_rapor" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "zaman" TEXT(50), "durum" INTEGER DEFAULT 0, "sayi" INTEGER DEFAULT 0 )')

        imlec.execute('CREATE TABLE "log" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "kullanici_id" INTEGER, "zaman" TEXT(50) )')

        imlec.execute('INSERT INTO "kullanicilar" ("kullanici_adi", "kullanici_parola","personel_adi_soyadi") values ("admin","admin","Kaç Kişi Var")')

        imlec.execute('INSERT INTO "ayarlar" ("gorevli_id","kisi_siniri", "mail_gonderme_saati", "usb_id") VALUES (1,"100", "18:00:00", 1)')

        vt.commit()
        vt.close()

    @classmethod
    def baglan(cls):
        cls.dosya = os.path.abspath(__file__)
        cls.dosya = str.rstrip(cls.dosya, "db.py")
        cls.dosya += cls.veritabani

        veritabani_olusmus_mu = os.path.exists(cls.dosya)

        if not veritabani_olusmus_mu:
            DB.olustur()
        else:
            print("{} veritabanı dosyası mevcut!".format(cls.veritabani))
        cls.vt = sql.connect(cls.dosya)
        cls.imlec = cls.vt.cursor()

    @classmethod
    def baglantiyi_kapat(cls):
        cls.vt.commit()
        cls.vt.close()

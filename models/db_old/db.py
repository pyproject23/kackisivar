import sqlite3 as sql


def olustur():
    vt = sql.connect("kackisivar.sqlite")
    imlec = vt.cursor()

    imlec.execute('CREATE TABLE "kullanicilar" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "kullanici_adi" TEXT(20), "kullanici_parola" TEXT(20), "personel_adi_soyadi" TEXT(100), "personel_mail_adresi" TEXT(250), "kayit_tarihi" TEXT(50) )')

    imlec.execute('CREATE TABLE "ayarlar" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "okul_adi" TEXT(250), "gorevli_id" INTEGER, "mail_gonderme_saati" TEXT(5), "kamera_turu" TEXT(250), "kamera_ayari" TEXT(250), "kisi_siniri" INTEGER, "smtp_server_adres" TEXT(100), "smtp_kullanici_adi" TEXT(50), "smtp_kullanici_parola" TEXT(50), "smtp_port_numarasi" INTEGER DEFAULT 587, "smtp_tls" INTEGER )')

    imlec.execute('CREATE TABLE "gunluk_rapor" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "zaman" TEXT(50), "durum" INTEGER DEFAULT 0, "sayi" INTEGER DEFAULT 0 )')

    imlec.execute('CREATE TABLE "log" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "kullanici_id" INTEGER, "zaman" TEXT(50) )')

    imlec.execute('INSERT INTO ayarlar ("id") VALUES (1)')

    vt.commit()

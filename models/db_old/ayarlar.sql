BEGIN TRANSACTION;
CREATE TABLE "ayarlar" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "okul_adi" TEXT(250), "gorevli_id" INTEGER, "mail_gonderme_saati" TEXT(5), "kamera_turu" TEXT(250), "kamera_ayari" TEXT(250), "kisi_siniri" INTEGER, "smtp_server_adres" TEXT(100), "smtp_kullanici_adi" TEXT(50), "smtp_kullanici_parola" TEXT(50), "smtp_port_numarasi" INTEGER DEFAULT 587, "smtp_tls" INTEGER );
INSERT INTO `ayarlar` () VALUES (1,'PyProject MTAL',2,'18:13','1','TestVideo.mp4',2,'smtp.gmail.com','kackisivar@gmail.com','Py1qaz2wsx',587,1);
COMMIT;

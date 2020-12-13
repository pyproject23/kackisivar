from models.db import DB
from datetime import datetime


class Kullanici:

    def __init__(self, id=None, kullanici_adi=None, kullanici_parola=None,personel_adi_soyadi=None, personel_mail_adresi=None):
        self.id = id
        self.kullanici_adi = kullanici_adi
        self.kullanici_parola = kullanici_parola
        self.personel_adi_soyadi = personel_adi_soyadi
        self.personel_mail_adresi = personel_mail_adresi
        self.kayit_tarihi = datetime.now()

    def kaydet(self):
        DB.baglan()
        if (self.id==0) or self.id is None:
            sorgu = "INSERT INTO kullanicilar (kullanici_adi, kullanici_parola, personel_adi_soyadi, personel_mail_adresi, kayit_tarihi)  VALUES (?, ?, ?, ?, ?)"
            veri = [self.kullanici_adi, self.kullanici_parola, self.personel_adi_soyadi, self.personel_mail_adresi, self.kayit_tarihi]
        else:
            sorgu = "UPDATE kullanicilar SET kullanici_adi=?, kullanici_parola=?, personel_adi_soyadi=?, personel_mail_adresi=?, kayit_tarihi=? WHERE id=?"
            veri = [self.kullanici_adi, self.kullanici_parola, self.personel_adi_soyadi, self.personel_mail_adresi, self.kayit_tarihi, self.id]
        DB.imlec.execute(sorgu, veri)
        DB.baglantiyi_kapat()

    def sil(self):
        DB.baglan()
        sorgu = "DELETE FROM kullanicilar WHERE id=?"
        veri = [self.id, ]
        DB.imlec.execute(sorgu, veri)
        DB.baglantiyi_kapat()

    def verileri_getir(self):
        DB.baglan()
        DB.imlec.execute("SELECT * FROM kullanicilar")
        kayitlar = DB.imlec.fetchall()
        DB.baglantiyi_kapat()
        return kayitlar

    def giris_yap(self, k_adi, parola):
        DB.baglan()
        sorgu = "SELECT * FROM kullanicilar WHERE kullanici_adi=? AND kullanici_parola=?"
        veri = [k_adi, parola]
        DB.imlec.execute(sorgu, veri)
        login = DB.imlec.fetchone()
        DB.baglantiyi_kapat()
        return login


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

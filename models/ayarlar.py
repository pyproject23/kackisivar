from models.db import DB


class Ayarlar:

    @staticmethod
    def kaydet(id=None, okul_adi=None, gorevli_id=None, mail_gonderme_saati=None, usb_id=None, demo_video=None, kisi_siniri=None, smtp_server_adres=None, smtp_kullanici_adi=None, smtp_kullanici_parola=None, smtp_port_numarasi=None, smtp_tls=None):
        DB.baglan()

        sorgu = "UPDATE ayarlar SET okul_adi=?, gorevli_id=?, mail_gonderme_saati=?, usb_id=?, demo_video=?, kisi_siniri=?, smtp_server_adres=?, smtp_kullanici_adi=?, smtp_kullanici_parola=?, smtp_port_numarasi=?, smtp_tls=? WHERE id=?"

        veri =[okul_adi, gorevli_id, mail_gonderme_saati, usb_id, demo_video, kisi_siniri, smtp_server_adres, smtp_kullanici_adi, smtp_kullanici_parola, smtp_port_numarasi, smtp_tls, id]

        DB.imlec.execute(sorgu, veri)
        DB.baglantiyi_kapat()

    @staticmethod
    def ayarlari_getir():
        DB.baglan()
        DB.imlec.execute("select k.id, k.personel_adi_soyadi, a.id, a.okul_adi, a.gorevli_id, a.mail_gonderme_saati, a.usb_id, a.demo_video, a.kisi_siniri, a.smtp_server_adres, a.smtp_kullanici_adi, a.smtp_kullanici_parola, a.smtp_port_numarasi, a.smtp_tls, k.personel_mail_adresi from ayarlar as a, kullanicilar as k where k.id = a.gorevli_id")
        ayarlar = DB.imlec.fetchone()
        DB.baglantiyi_kapat()
        return ayarlar


if __name__ == "__main__":
    # pass
    # Ayarlar.kaydet(id=1, okul_adi="PyProject MTAL", gorevli_id=4, mail_gonderme_saati="20:00", usb_id="USB", demo_video=None, kisi_siniri=15, smtp_server_adres="127.0.0.1", smtp_kullanici_adi="admin@localhost", smtp_kullanici_parola="12345", smtp_port_numarasi=587, smtp_tls=None)
    # Ayarlar.kaydet(silinecek=True)
    Ayarlar.ayarlari_getir()

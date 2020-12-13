from datetime import datetime
from models.db import DB
# import time


class Log:

    @staticmethod
    def logu_guncelle(kullanici_id=None, logu_sil=False):
        DB.baglan()
        zaman = datetime.now()
        if logu_sil is True:
            sorgu = "DELETE FROM log"
            DB.imlec.execute(sorgu)
        else:
            sorgu = "INSERT INTO log (kullanici_id, zaman) VALUES(?, ?)"
            veri = [kullanici_id, zaman]
            DB.imlec.execute(sorgu, veri)
        DB.baglantiyi_kapat()

    @staticmethod
    def logu_getir():
        DB.baglan()
        # DB.imlec.execute("SELECT * FROM log")
        DB.imlec.execute("SELECT log.id,kullanicilar.personel_adi_soyadi,log.zaman, kullanicilar.id "
                          "FROM log INNER JOIN kullanicilar ON log.kullanici_id = kullanicilar.id")
        loglar = DB.imlec.fetchall()
        DB.baglantiyi_kapat()
        return loglar

    @staticmethod
    def logu_sil():
        DB.baglan()
        DB.imlec.execute("DELETE FROM log")
        DB.baglantiyi_kapat()


if __name__ == "__main__":
    # pass
    # Log.logu_guncelle(2)
    # time.sleep(1)
    # Log.logu_guncelle(4)
    # time.sleep(6)
    # Log.logu_guncelle(1)
    # time.sleep(4)
    # Log.logu_guncelle(1)
    # Log.logu_guncelle(logu_sil=True)
    # Log.logu_guncelle(logu_sil=True)
    Log.logu_getir()

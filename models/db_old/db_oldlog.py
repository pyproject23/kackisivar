import os
import sqlite3 as sql
from datetime import datetime
import models.db
# import time


class Log:

    @staticmethod
    def logu_guncelle(kullanici_id=None, logu_sil=False):
        veritabani = "kackisivar.sqlite"
        dosya = os.path.abspath(__file__)
        dosya = str.rstrip(dosya, "log.py")
        dosya += veritabani
        print(dosya)
        veritabani_olusmus_mu = os.path.exists(dosya)

        if not veritabani_olusmus_mu:
            models.db.olustur()
        else:
            print("{} veritabanı dosyası mevcut!".format(veritabani))

        vt = sql.connect(dosya)
        imlec = vt.cursor()

        zaman = datetime.now()
        if logu_sil is True:
            sorgu = "DELETE FROM log"
            imlec.execute(sorgu)
        else:
            sorgu = "INSERT INTO log (kullanici_id, zaman) VALUES(?, ?)"
            veri = [kullanici_id, zaman]
            imlec.execute(sorgu, veri)
        vt.commit()
        vt.close()

    @staticmethod
    def logu_getir():
        veritabani = "kackisivar.sqlite"
        dosya = os.path.abspath(__file__)
        dosya = str.rstrip(dosya, "log.py")
        dosya += veritabani
        print(dosya)
        veritabani_olusmus_mu = os.path.exists(dosya)

        if not veritabani_olusmus_mu:
            models.db.olustur()
        else:
            print("{} veritabanı dosyası mevcut!".format(veritabani))

        vt = sql.connect(dosya)
        imlec = vt.cursor()

        imlec.execute("SELECT * FROM log")
        kayitlar = imlec.fetchall()
        return kayitlar
        # for kayit in kayitlar:
        #    print(kayit)


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

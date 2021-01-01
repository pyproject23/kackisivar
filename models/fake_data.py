from gunluk_rapor import GunlukRapor
import random


def fake_data_olustur():

    yil = "2020"
    for ay in range(11, 13):
        for gun in range(1, 31):
            for saat in range(8, 19):
                for dakika in range(60):
                    for saniye in range(20):
                        if ay < 10:
                            ay = "0" + str(ay)
                        if gun < 10:
                            gun = "0" + str(gun)
                        if saat < 10:
                            saat = "0" + str(saat)
                        if dakika < 10:
                            dakika = "0" + str(dakika)
                        if saniye * 3 < 10:
                            sn = "0" + str(saniye * 3)
                        if saat == 8 or saat == 16:
                            zaman = f"{yil}-{ay}-{gun} {saat}:{dakika}:{sn}"
                            if int(saat) == 8 and int(sn) <= 17:
                                sayi = random.randint(0, 5)
                                durum = 0
                            else:
                                durum = 1
                                sayi = random.randint(0, 2)
                            if int(saat) == 16 and int(sn) <= 17:
                                durum = 1
                                sayi = random.randint(0, 5)
                            else:
                                durum = 0
                                sayi = random.randint(0, 2)
                        else:
                            sayi = random.randint(0, 2)
                            zaman = f"{yil}-{ay}-{gun} {saat}:{dakika}:{sn}"
                            durum = random.randint(0, 1)
                        if sayi > 0:
                            rapor = GunlukRapor(zaman=zaman, durum=durum, sayi=sayi)
                            rapor.kaydet()
                            print(zaman, "-", durum, "-", sayi)


if __name__ == "__main__":
    fake_data_olustur()

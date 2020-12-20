from gunluk_rapor import GunlukRapor
import random


def fake_data_olustur():

    yil = "2020"
    for ay in range(11, 13):
        for gun in range(1, 31):
            for saat in range(8, 19):
                for dakika in range(60):
                    for saniye in range(20):
                        if saat == 8 or saat == 16:
                            zaman = "{}-{}-{} {}:{}:{}".format(yil, ay, gun, saat, dakika, saniye*3)
                            if saat == 8 and saniye <= 17:
                                sayi = random.randint(0, 5)
                                durum = 0
                            else:
                                durum = 1
                                sayi = random.randint(0, 2)
                            if saat == 16 and saniye <= 17:
                                durum = 1
                                sayi = random.randint(0, 5)
                            else:
                                durum = 0
                                sayi = random.randint(0, 2)
                        else:
                            sayi = random.randint(0, 2)
                            zaman = "{}-{}-{} {}:{}:{}".format(yil, ay, gun, saat, dakika, saniye*3)
                            durum = random.randint(0, 1)
                        if sayi > 0:
                            rapor = GunlukRapor(zaman=zaman, durum=durum, sayi=sayi)
                            rapor.kaydet()
                            print(zaman, "-", durum, "-", sayi)

if __name__ == "__main__":
    fake_data_olustur()

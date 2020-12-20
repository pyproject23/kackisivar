import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models.ayarlar import Ayarlar
from models.gunluk_rapor import GunlukRapor
from PyQt5.QtCore import QThread
import datetime
import time


class Mail_Gunluk_Rapor(QThread):

    def __init__(self, parent):
        super().__init__(parent)
        self.baslik = "KAÇKİŞİVAR uygulaması günlük raporu"
        self.durum = False
        self.mesaj = MIMEMultipart()
        self.mail = None
        self.ayarlar1 = Ayarlar.ayarlari_getir()
        self.rapor = None
        self.tarih = datetime.datetime.now()
        self.saat = str.split(self.ayarlar1[5], ":")
        self.gunlukRapor_gelen = 0
        self.gunlukRapor_giden = 0
        self.mevcut = 0

    def run(self):
        try:
            send_time = datetime.datetime(self.tarih.year,self.tarih.month,self.tarih.day,int(self.saat[0]),int(self.saat[1]),0) # set your sending time in UTC
            time.sleep(send_time.timestamp() - time.time())
            self.send_email()
        except:
            return

    def send_email(self):
        if self.durum is False:
            self.rapor = GunlukRapor()
            self.gunlukRapor_gelen = self.rapor.gunluk_giris_sayisini_ver()
            self.gunlukRapor_giden = self.rapor.gunluk_cikis_sayisini_ver()
            self.mevcut = self.gunlukRapor_gelen - self.gunlukRapor_giden
            self.yazi="<h1>KAÇKİŞİVAR Programı " +str(datetime.datetime.now().date())+ " Tarihli Günlük Raporu</h1><br>"+"Toplam Gelen:"+str(self.gunlukRapor_gelen)+"<br>"+"Toplam Giden:"+str(self.gunlukRapor_giden)+"<br>"+"İçeride Kalan Kişi Sayısı:"+str(self.mevcut)

            self.durum = True
            self.mesaj['from'] = self.ayarlar1[10]
            self.mesaj['to'] = self.ayarlar1[14]
            self.mesaj['subject'] = self.baslik
            mesaj_yapisi = MIMEText(self.yazi, 'html')
            self.mesaj.attach(mesaj_yapisi)
            try:
                self.mail = smtplib.SMTP(self.ayarlar1[9], self.ayarlar1[12])
                self.mail.ehlo()
                self.mail.starttls()
                self.mail.login(self.ayarlar1[10], self.ayarlar1[11])
                self.mail.sendmail(self.mesaj['from'], self.mesaj['to'], self.mesaj.as_string())
                print('Günlük Rapor mail gönderildi')
                self.mail.close()
            except:
                print('Mail Gönderme Sırasında hata oluştu')

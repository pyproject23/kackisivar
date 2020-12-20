import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models.ayarlar import Ayarlar
from PyQt5.QtCore import QThread

class Mail(QThread):

    def __init__(self, parent):
        super().__init__(parent)
        self.yazi = ""
        self.baslik = ""
        self.durum = False
        self.mesaj = MIMEMultipart()
        self.mail = None
        self.ayarlar = Ayarlar.ayarlari_getir()

    def run(self):
       if self.durum is False:
            self.mesaj['from'] = self.ayarlar[10]
            self.mesaj['to'] = self.ayarlar[14]
            self.mesaj['subject'] = self.baslik
            mesaj_yapisi = MIMEText(self.yazi, 'html')
            self.mesaj.attach(mesaj_yapisi)
            try:
                self.mail = smtplib.SMTP(self.ayarlar[9], self.ayarlar[12])
                self.mail.ehlo()
                self.mail.starttls()
                self.mail.login(self.ayarlar[10], self.ayarlar[11])
                self.mail.sendmail(self.mesaj['from'], self.mesaj['to'], self.mesaj.as_string())
                print(self.baslik +' Mail gönderildi')
                self.mail.close()
            except:
                print('Mail Gönderme Sırasında hata oluştu')
            self.durum=True

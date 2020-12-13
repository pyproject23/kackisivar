from PyQt5 import QtCore, QtGui, QtWidgets
from views.login_form import Ui_LoginForm
from models.kullanici import Kullanici
from models.log import Log


class LoginForm(QtWidgets.QWidget, Ui_LoginForm):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login_kontrol)
        self.lineEditParola.returnPressed.connect(self.pushButton.click)
        self.lineEditKullaniciAdi.returnPressed.connect(self.pushButton.click)

    def login_kontrol(self):
        kullanici_adi = str.strip(self.lineEditKullaniciAdi.text())
        parola = str.strip(self.lineEditParola.text())
        kullanici = Kullanici()
        # kullanici.verileri_getir()
        giris = kullanici.giris_yap(kullanici_adi, parola)
        if giris:
            id = giris[0]
            Log.logu_guncelle(id)
            # self.window.gorevli = list(giris)
            # Veri.giris_kullanicisi = list(giris)
            # print("dd:",self.window.gorevli)
            # durum = "Görevli :{} - {}".format(giris[2], giris[3])
            # self.window.statusbar.showMessage(durum)
            self.window.show()
            self.close()
        else:
            self.label.setStyleSheet("color:red;")
            self.label.setText("Hatalı Kullanıcı Bilgileri!!!")

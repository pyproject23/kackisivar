from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from views.anaekran import Ui_MainWindow
from models.kullanici import *
from controllers.menu_controller import AnaMenu
from controllers.goruntu_isleme import GoruntuIsleme


class AnaEkran(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ana_menu = AnaMenu()
        self.setupUi(self)

        self.sayici = GoruntuIsleme(self)
        self.sayici.changePixmap.connect(self.setImage)
        self.sayici.start()
        # self.show()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label_video.setPixmap(QPixmap.fromImage(image))

        self.label_giren_sayisi.setText("GİDEN:"+str(self.sayici.cnt_up+ int(self.sayici.count_up))+" GELEN:"+str(self.sayici.cnt_down+ int(self.sayici.count_down)))


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.menuAyarlar.triggered.connect(self.show_ayarlar)
        self.menuKullanicilar.triggered.connect(self.show_kullanicilar)
        self.menuLoglar.triggered.connect(self.show_log)
        self.menuAnasayfa.triggered.connect(self.kapat)
        self.menuHakkinda.triggered.connect(self.show_hakkimizda)

    def show_ayarlar(self):
        self.ana_menu.show_ayarlar()

    def show_kullanicilar(self):
        self.ana_menu.show_kullanicilar()

    def show_log(self):
        self.ana_menu.show_log()

    def show_hakkimizda(self):
        self.ana_menu.show_hakkimizda()

    def kapat(self):
        QtCore.QCoreApplication.quit()

from PyQt5 import QtCore, QtGui, QtWidgets
from views.hakkimizda_form import Ui_HakkimizdaForm
import webbrowser as wb
class Hakkimizda_Form(QtWidgets.QWidget, Ui_HakkimizdaForm):
    
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()
        
    
    

    def setupUi(self):
        super().setupUi(self)
        self.commandLinkButton.clicked.connect(self.siteye_yonlendir)

    def siteye_yonlendir(self):
        website = "https://github.com/pyproject23/kackisivar"
        wb.open(website)
        
from PyQt5 import QtCore, QtGui, QtWidgets
from controllers.login_controller import LoginForm
from controllers.main_controller import AnaEkran
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('motif')
    MainWindow = QtWidgets.QMainWindow()
    ui = AnaEkran()
    ui.setupUi(MainWindow)
    # MainWindow.show()
    login = LoginForm()
    login.window = MainWindow
    login.show()
    sys.exit(app.exec_())

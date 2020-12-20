from PyQt5 import QtCore, QtGui, QtWidgets
from controllers.login_controller import LoginForm
from controllers.main_controller import AnaEkran
import sys
from os import environ, name


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"
    if name == "posix":
        environ["QT_QPA_PLATFORM"] = "wayland"


if __name__ == "__main__":
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("Kaç Kişi Var")
    MainWindow = QtWidgets.QMainWindow()
    ui = AnaEkran()
    ui.setupUi(MainWindow)
    # MainWindow.show()

    login = LoginForm()
    login.window = MainWindow
    login.show()
    sys.exit(app.exec_())

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from vCotizacion import Ui_cotizacion
import Logo_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(604, 330)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_cotizacion = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cotizacion.setGeometry(QtCore.QRect(160, 160, 111, 51))
        self.pb_cotizacion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_cotizacion.setObjectName("pb_cotizacion")
        self.pb_bd = QtWidgets.QPushButton(self.centralwidget)
        self.pb_bd.setGeometry(QtCore.QRect(330, 160, 121, 51))
        self.pb_bd.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_bd.setObjectName("pb_bd")
        self.label_bienvenido = QtWidgets.QLabel(self.centralwidget)
        self.label_bienvenido.setGeometry(QtCore.QRect(70, 30, 231, 81))
        self.label_bienvenido.setObjectName("label_bienvenido")
        self.label_sitioweb = QtWidgets.QLabel(self.centralwidget)
        self.label_sitioweb.setGeometry(QtCore.QRect(320, 240, 271, 41))
        self.label_sitioweb.setObjectName("label_sitioweb")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 0, 231, 141))
        self.label.setStyleSheet("border-image: url(:/logob/LogoNegrops.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pb_cotizacion.setText(_translate("MainWindow", "Cotización"))
        self.pb_bd.setText(_translate("MainWindow", "Base de Datos"))
        self.label_bienvenido.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600; color:#ffff00;\">BIENVENIDO |</span></p></body></html>"))
        self.label_sitioweb.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))
        self.pb_cotizacion.clicked.connect(self.abrircotizacion)
        self.pb_bd.clicked.connect(self.abrirbd)

     
    def abrircotizacion(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_cotizacion()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def abrirbd(self):
        import os
        os.system('menu_cotizador.py')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

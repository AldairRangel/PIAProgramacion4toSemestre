# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vclientevalido.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_V_clientevalido(object):
    def setupUi(self, V_clientevalido):
        V_clientevalido.setObjectName("V_clientevalido")
        V_clientevalido.resize(475, 218)
        V_clientevalido.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(V_clientevalido)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_leyenda = QtWidgets.QLabel(self.centralwidget)
        self.lb_leyenda.setGeometry(QtCore.QRect(0, 30, 471, 101))
        self.lb_leyenda.setObjectName("lb_leyenda")
        V_clientevalido.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(V_clientevalido)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 21))
        self.menubar.setObjectName("menubar")
        V_clientevalido.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(V_clientevalido)
        self.statusbar.setObjectName("statusbar")
        V_clientevalido.setStatusBar(self.statusbar)

        self.retranslateUi(V_clientevalido)
        QtCore.QMetaObject.connectSlotsByName(V_clientevalido)

    def retranslateUi(self, V_clientevalido):
        _translate = QtCore.QCoreApplication.translate
        V_clientevalido.setWindowTitle(_translate("V_clientevalido", "MainWindow"))
        self.lb_leyenda.setText(_translate("V_clientevalido", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">CLIENTE VALIDO.</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">INGRESA DATOS EN LOS CAMPOS</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">RESTANTES Y PRESIONA GUARDAR.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    V_clientevalido = QtWidgets.QMainWindow()
    ui = Ui_V_clientevalido()
    ui.setupUi(V_clientevalido)
    V_clientevalido.show()
    sys.exit(app.exec_())

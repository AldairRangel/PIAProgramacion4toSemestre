# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vusuarionovalido.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_V_usuarionovalido(object):
    def setupUi(self, V_usuarionovalido):
        V_usuarionovalido.setObjectName("V_usuarionovalido")
        V_usuarionovalido.resize(475, 243)
        V_usuarionovalido.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(V_usuarionovalido)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_leyenda = QtWidgets.QLabel(self.centralwidget)
        self.lb_leyenda.setGeometry(QtCore.QRect(0, 20, 471, 161))
        self.lb_leyenda.setObjectName("lb_leyenda")
        V_usuarionovalido.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(V_usuarionovalido)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 21))
        self.menubar.setObjectName("menubar")
        V_usuarionovalido.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(V_usuarionovalido)
        self.statusbar.setObjectName("statusbar")
        V_usuarionovalido.setStatusBar(self.statusbar)

        self.retranslateUi(V_usuarionovalido)
        QtCore.QMetaObject.connectSlotsByName(V_usuarionovalido)

    def retranslateUi(self, V_usuarionovalido):
        _translate = QtCore.QCoreApplication.translate
        V_usuarionovalido.setWindowTitle(_translate("V_usuarionovalido", "MainWindow"))
        self.lb_leyenda.setText(_translate("V_usuarionovalido", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">USUARIO NO VALIDO.</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">INTENTA CON UN REGISTRO</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">DADO PREVIAMENTE DE ALTA.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    V_usuarionovalido = QtWidgets.QMainWindow()
    ui = Ui_V_usuarionovalido()
    ui.setupUi(V_usuarionovalido)
    V_usuarionovalido.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vusuarioactualizado.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_V_usuarioaactualizado(object):
    def setupUi(self, V_usuarioaactualizado):
        V_usuarioaactualizado.setObjectName("V_usuarioaactualizado")
        V_usuarioaactualizado.resize(402, 206)
        V_usuarioaactualizado.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(V_usuarioaactualizado)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_leyenda = QtWidgets.QLabel(self.centralwidget)
        self.lb_leyenda.setGeometry(QtCore.QRect(0, 30, 401, 101))
        self.lb_leyenda.setObjectName("lb_leyenda")
        V_usuarioaactualizado.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(V_usuarioaactualizado)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
        self.menubar.setObjectName("menubar")
        V_usuarioaactualizado.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(V_usuarioaactualizado)
        self.statusbar.setObjectName("statusbar")
        V_usuarioaactualizado.setStatusBar(self.statusbar)

        self.retranslateUi(V_usuarioaactualizado)
        QtCore.QMetaObject.connectSlotsByName(V_usuarioaactualizado)

    def retranslateUi(self, V_usuarioaactualizado):
        _translate = QtCore.QCoreApplication.translate
        V_usuarioaactualizado.setWindowTitle(_translate("V_usuarioaactualizado", "MainWindow"))
        self.lb_leyenda.setText(_translate("V_usuarioaactualizado", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">USUARIO</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">ACTUALIZADO</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">SATISFACTORIAMENTE</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    V_usuarioaactualizado = QtWidgets.QMainWindow()
    ui = Ui_V_usuarioaactualizado()
    ui.setupUi(V_usuarioaactualizado)
    V_usuarioaactualizado.show()
    sys.exit(app.exec_())

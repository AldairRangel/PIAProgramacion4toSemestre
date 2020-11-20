from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_V_usuarioeliminado(object):
    def setupUi(self, V_usuarioeliminado):
        V_usuarioeliminado.setObjectName("V_usuarioeliminado")
        V_usuarioeliminado.resize(402, 216)
        V_usuarioeliminado.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(V_usuarioeliminado)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_leyenda = QtWidgets.QLabel(self.centralwidget)
        self.lb_leyenda.setGeometry(QtCore.QRect(0, 30, 401, 101))
        self.lb_leyenda.setObjectName("lb_leyenda")
        V_usuarioeliminado.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(V_usuarioeliminado)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 21))
        self.menubar.setObjectName("menubar")
        V_usuarioeliminado.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(V_usuarioeliminado)
        self.statusbar.setObjectName("statusbar")
        V_usuarioeliminado.setStatusBar(self.statusbar)

        self.retranslateUi(V_usuarioeliminado)
        QtCore.QMetaObject.connectSlotsByName(V_usuarioeliminado)

    def retranslateUi(self, V_usuarioeliminado):
        _translate = QtCore.QCoreApplication.translate
        V_usuarioeliminado.setWindowTitle(_translate("V_usuarioeliminado", "MainWindow"))
        self.lb_leyenda.setText(_translate("V_usuarioeliminado", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">USUARIO</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">ELIMINADO</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffff00;\">SATISFACTORIAMENTE</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    V_usuarioeliminado = QtWidgets.QMainWindow()
    ui = Ui_V_usuarioeliminado()
    ui.setupUi(V_usuarioeliminado)
    V_usuarioeliminado.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Veliminarusuario(object):
    def EliminarUser(self):
        with sqlite3.connect('bdpaneles.db') as conn:
            c = conn.cursor()
            usuarioDel = str(self.textEdit.toPlainText())
            c.execute('DELETE FROM User WHERE Usuario = "'+usuarioDel+'";')
            import os
            os.system('vusuarioeliminado.py')
        conn.close()

    def setupUi(self, Veliminarusuario):
        Veliminarusuario.setObjectName("Veliminarusuario")
        Veliminarusuario.resize(481, 292)
        Veliminarusuario.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Veliminarusuario)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_eliminarusuario = QtWidgets.QLabel(self.centralwidget)
        self.lb_eliminarusuario.setGeometry(QtCore.QRect(10, 0, 461, 31))
        self.lb_eliminarusuario.setObjectName("lb_eliminarusuario")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 461, 31))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 110, 351, 51))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Tahoma\";")
        self.textEdit.setObjectName("textEdit")
        self.lb_web = QtWidgets.QLabel(self.centralwidget)
        self.lb_web.setGeometry(QtCore.QRect(310, 230, 161, 21))
        self.lb_web.setObjectName("lb_web")
        self.pb_efectuarmov = QtWidgets.QPushButton(self.centralwidget)
        self.pb_efectuarmov.setGeometry(QtCore.QRect(160, 180, 181, 31))
        self.pb_efectuarmov.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.pb_efectuarmov.setObjectName("pb_efectuarmov")
        self.pb_efectuarmov.clicked.connect(self.EliminarUser)
        Veliminarusuario.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Veliminarusuario)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 21))
        self.menubar.setObjectName("menubar")
        Veliminarusuario.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Veliminarusuario)
        self.statusbar.setObjectName("statusbar")
        Veliminarusuario.setStatusBar(self.statusbar)

        self.retranslateUi(Veliminarusuario)
        QtCore.QMetaObject.connectSlotsByName(Veliminarusuario)

    def retranslateUi(self, Veliminarusuario):
        _translate = QtCore.QCoreApplication.translate
        Veliminarusuario.setWindowTitle(_translate("Veliminarusuario", "MainWindow"))
        self.lb_eliminarusuario.setText(_translate("Veliminarusuario", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\">ELIMINAR USUARIO</span></p></body></html>"))
        self.label.setText(_translate("Veliminarusuario", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffff00;\">Ingresa el usuario a eliminar:</span></p></body></html>"))
        self.lb_web.setText(_translate("Veliminarusuario", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))
        self.pb_efectuarmov.setText(_translate("Veliminarusuario", "EFECTUAR MOVIMIENTO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Veliminarusuario = QtWidgets.QMainWindow()
    ui = Ui_Veliminarusuario()
    ui.setupUi(Veliminarusuario)
    Veliminarusuario.show()
    sys.exit(app.exec_())

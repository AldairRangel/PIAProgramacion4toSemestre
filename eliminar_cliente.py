from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Veliminarcliente(object):
    def EliminarCliente(self): #Funcion eliminar cliente
        with sqlite3.connect('bdpaneles.db') as conn: #conexión bd
            c = conn.cursor()
            ClienteDel = str(self.textEdit.toPlainText())
            c.execute('DELETE FROM Cliente WHERE correo_contacto = "'+ClienteDel+'";') #Borrar cliente con dato almacenado en cuadro de texto
            import os
            os.system('vclienteeliminado.py') #ventana informativa
        conn.close()

    def setupUi(self, Veliminarcliente): #Ventana PyQt5
        Veliminarcliente.setObjectName("Veliminarcliente")
        Veliminarcliente.resize(481, 292)
        Veliminarcliente.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Veliminarcliente)
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
        Veliminarcliente.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Veliminarcliente)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 21))
        self.menubar.setObjectName("menubar")
        Veliminarcliente.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Veliminarcliente)
        self.statusbar.setObjectName("statusbar")
        Veliminarcliente.setStatusBar(self.statusbar)

        self.retranslateUi(Veliminarcliente)
        QtCore.QMetaObject.connectSlotsByName(Veliminarcliente)

    def retranslateUi(self, Veliminarcliente):
        _translate = QtCore.QCoreApplication.translate
        Veliminarcliente.setWindowTitle(_translate("Veliminarcliente", "MainWindow"))
        self.lb_eliminarusuario.setText(_translate("Veliminarcliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\">ELIMINAR CLIENTE</span></p></body></html>"))
        self.label.setText(_translate("Veliminarcliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffff00;\">Ingresa el cliente a eliminar:</span></p></body></html>"))
        self.lb_web.setText(_translate("Veliminarcliente", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))
        self.pb_efectuarmov.setText(_translate("Veliminarcliente", "EFECTUAR MOVIMIENTO"))
        self.pb_efectuarmov.clicked.connect(self.EliminarCliente)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Veliminarcliente = QtWidgets.QMainWindow()
    ui = Ui_Veliminarcliente()
    ui.setupUi(Veliminarcliente)
    Veliminarcliente.show()
    sys.exit(app.exec_())

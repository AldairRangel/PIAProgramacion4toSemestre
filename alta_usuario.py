from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_V_Alta_usuario(object):
        def GuardarAltaUsuario(self): #Función para guardar usuario
                with sqlite3.connect('bdpaneles.db') as conn: #conexión db
                        c=conn.cursor()
                        usuario = str(self.TE_usuario.toPlainText())
                        contrasena = str(self.TE_contrasena.toPlainText())
                        nombre = str(self.TE_nombre.toPlainText())
                        apellidos = str(self.TE_apellidos.toPlainText())
                        correoElectronico = str(self.TE_correo.toPlainText())
                        tipoDeUsuario = str(self.TE_tipousuario.toPlainText()) #linea 14 insert datos de linea 8 a 13
                        c.execute('INSERT INTO user VALUES("'+usuario+'","'+contrasena+'","'+nombre+'","'+apellidos+'","'+correoElectronico+'","'+tipoDeUsuario+'");')
                        import os
                        os.system('vusuarioagregado.py') #ventana informativa
                conn.close()

        def setupUi(self, V_Alta_usuario): #Ventana PyQt5
                V_Alta_usuario.setObjectName("V_Alta_usuario")
                V_Alta_usuario.resize(565, 471)
                V_Alta_usuario.setStyleSheet("background-color: rgb(0, 0, 0);")
                self.centralwidget = QtWidgets.QWidget(V_Alta_usuario)
                self.centralwidget.setObjectName("centralwidget")
                self.lb_titulo = QtWidgets.QLabel(self.centralwidget)
                self.lb_titulo.setGeometry(QtCore.QRect(0, 0, 631, 31))
                self.lb_titulo.setObjectName("lb_titulo")
                self.lb_nombreusuario = QtWidgets.QLabel(self.centralwidget)
                self.lb_nombreusuario.setGeometry(QtCore.QRect(10, 70, 131, 41))
                self.lb_nombreusuario.setObjectName("lb_nombreusuario")
                self.lb_contrasena = QtWidgets.QLabel(self.centralwidget)
                self.lb_contrasena.setGeometry(QtCore.QRect(10, 130, 131, 31))
                self.lb_contrasena.setObjectName("lb_contrasena")
                self.lb_nombre = QtWidgets.QLabel(self.centralwidget)
                self.lb_nombre.setGeometry(QtCore.QRect(0, 180, 141, 31))
                self.lb_nombre.setObjectName("lb_nombre")
                self.lb_apellido = QtWidgets.QLabel(self.centralwidget)
                self.lb_apellido.setGeometry(QtCore.QRect(0, 230, 141, 31))
                self.lb_apellido.setObjectName("lb_apellido")
                self.lb_correo = QtWidgets.QLabel(self.centralwidget)
                self.lb_correo.setGeometry(QtCore.QRect(0, 280, 141, 31))
                self.lb_correo.setObjectName("lb_correo")
                self.lb_tipousuario = QtWidgets.QLabel(self.centralwidget)
                self.lb_tipousuario.setGeometry(QtCore.QRect(0, 330, 141, 31))
                self.lb_tipousuario.setObjectName("lb_tipousuario")
                self.lb_paginaweb = QtWidgets.QLabel(self.centralwidget)
                self.lb_paginaweb.setGeometry(QtCore.QRect(380, 410, 181, 16))
                self.lb_paginaweb.setObjectName("lb_paginaweb")
                self.TE_usuario = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_usuario.setGeometry(QtCore.QRect(160, 70, 391, 41))
                self.TE_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_usuario.setObjectName("TE_usuario")
                self.TE_contrasena = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_contrasena.setGeometry(QtCore.QRect(160, 120, 391, 41))
                self.TE_contrasena.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_contrasena.setObjectName("TE_contrasena")
                self.TE_nombre = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_nombre.setGeometry(QtCore.QRect(160, 170, 391, 41))
                self.TE_nombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_nombre.setObjectName("TE_nombre")
                self.TE_apellidos = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_apellidos.setGeometry(QtCore.QRect(160, 220, 391, 41))
                self.TE_apellidos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_apellidos.setObjectName("TE_apellidos")
                self.TE_correo = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_correo.setGeometry(QtCore.QRect(160, 270, 391, 41))
                self.TE_correo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_correo.setObjectName("TE_correo")
                self.TE_tipousuario = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_tipousuario.setGeometry(QtCore.QRect(160, 320, 61, 41))
                self.TE_tipousuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_tipousuario.setObjectName("TE_tipousuario")
                self.Boton_guardar = QtWidgets.QPushButton(self.centralwidget)
                self.Boton_guardar.setGeometry(QtCore.QRect(250, 340, 111, 51))
                self.Boton_guardar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 11pt \"Tahoma\";")
                self.Boton_guardar.setObjectName("Boton_guardar")
                self.Boton_guardar.clicked.connect(self.GuardarAltaUsuario)
                self.Boton_guardar_2 = QtWidgets.QPushButton(self.centralwidget)
                self.Boton_guardar_2.setGeometry(QtCore.QRect(370, 340, 161, 51))
                self.Boton_guardar_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 11pt \"Tahoma\";")
                self.Boton_guardar_2.setObjectName("Boton_guardar_2")
                V_Alta_usuario.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(V_Alta_usuario)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 21))
                self.menubar.setObjectName("menubar")
                V_Alta_usuario.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(V_Alta_usuario)
                self.statusbar.setObjectName("statusbar")
                V_Alta_usuario.setStatusBar(self.statusbar)

                self.retranslateUi(V_Alta_usuario)
                self.Boton_guardar_2.clicked.connect(self.TE_tipousuario.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_correo.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_apellidos.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_nombre.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_contrasena.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_usuario.clear)
                QtCore.QMetaObject.connectSlotsByName(V_Alta_usuario)

        def retranslateUi(self, V_Alta_usuario):
                _translate = QtCore.QCoreApplication.translate
                V_Alta_usuario.setWindowTitle(_translate("V_Alta_usuario", "MainWindow"))
                self.lb_titulo.setText(_translate("V_Alta_usuario", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\">ALTA DE USUARIO</span></p></body></html>"))
                self.lb_nombreusuario.setText(_translate("V_Alta_usuario", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Nombre de usuario:</span></p></body></html>"))
                self.lb_contrasena.setText(_translate("V_Alta_usuario", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Contraseña:</span></p></body></html>"))
                self.lb_nombre.setText(_translate("V_Alta_usuario", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Nombre(s):</span></p></body></html>"))
                self.lb_apellido.setText(_translate("V_Alta_usuario", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Apellidos:</span></p></body></html>"))
                self.lb_correo.setText(_translate("V_Alta_usuario", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Correo electronico:</span></p></body></html>"))
                self.lb_tipousuario.setText(_translate("V_Alta_usuario", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Tipo usuario:</span></p></body></html>"))
                self.lb_paginaweb.setText(_translate("V_Alta_usuario", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))
                self.Boton_guardar.setText(_translate("V_Alta_usuario", "Guardar"))
                self.Boton_guardar_2.setText(_translate("V_Alta_usuario", "Borrar datos ingresados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    V_Alta_usuario = QtWidgets.QMainWindow()
    ui = Ui_V_Alta_usuario()
    ui.setupUi(V_Alta_usuario)
    V_Alta_usuario.show()
    sys.exit(app.exec_())

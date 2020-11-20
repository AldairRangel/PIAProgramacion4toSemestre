from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(301, 485)
        Login.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_usuario = QtWidgets.QLabel(self.centralwidget)
        self.lb_usuario.setGeometry(QtCore.QRect(0, 110, 301, 21))
        self.lb_usuario.setObjectName("lb_usuario")
        self.ingresar_usuario = QtWidgets.QTextEdit(self.centralwidget)
        self.ingresar_usuario.setGeometry(QtCore.QRect(10, 150, 281, 41))
        self.ingresar_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 11pt \"Arial Black\";")
        self.ingresar_usuario.setObjectName("ingresar_usuario")
        self.lb_contrasena = QtWidgets.QLabel(self.centralwidget)
        self.lb_contrasena.setGeometry(QtCore.QRect(0, 230, 301, 21))
        self.lb_contrasena.setObjectName("lb_contrasena")
        self.ingresar = QtWidgets.QPushButton(self.centralwidget)
        self.ingresar.setGeometry(QtCore.QRect(90, 340, 121, 41))
        self.ingresar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"Tahoma\";")
        self.ingresar.setObjectName("ingresar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 430, 151, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 0, 101, 91))
        self.label_2.setStyleSheet("border-image: url(:/login/logo_login.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.ingresar_contrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.ingresar_contrasena.setGeometry(QtCore.QRect(10, 270, 281, 41))
        self.ingresar_contrasena.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"Arial\";")
        self.ingresar_contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ingresar_contrasena.setObjectName("ingresar_contrasena")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 301, 21))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.lb_usuario.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">USUARIO:</span></p></body></html>"))
        self.lb_contrasena.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">CONTRASEÑA:</span></p></body></html>"))
        self.ingresar.setText(_translate("Login", "INGRESAR"))
        self.label.setText(_translate("Login", "<html><head/><body><p><span style=\" font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))
        self.ingresar.clicked.connect(self.verificar_login)

    def verificar_login(self):
        while True:
            contraseña = str(self.ingresar_contrasena.text())
            v_usuario = str(self.ingresar_usuario.toPlainText())
            with sqlite3.connect('bdpaneles.db') as conn:
                c = conn.cursor()
                encontrar_usuario = ("SELECT TipoUsuario FROM User WHERE Usuario = ? AND Contraseña = ?")
                c.execute(encontrar_usuario,[(v_usuario),(contraseña)])
                results = c.fetchall()
                if results:
                    for i in results:
                        for n in i:
                            decision = n
                    if decision == 1:
                        import os
                        os.system('menu_admin.py')
                    else:
                        import os
                        os.system('Menu_principal.py')
                else:
                    import os
                    os.system('error_login.py')
                break
import logologin_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

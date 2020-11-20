from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MenuAdmin(object):
    def setupUi(self, MenuAdmin):
        MenuAdmin.setObjectName("MenuAdmin")
        MenuAdmin.resize(699, 236)
        MenuAdmin.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MenuAdmin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 41))
        self.label.setStyleSheet("font: 14pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 170, 201, 20))
        self.label_2.setObjectName("label_2")
        self.Alta_usuario = QtWidgets.QPushButton(self.centralwidget)
        self.Alta_usuario.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.Alta_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Alta_usuario.setObjectName("Alta_usuario")
        self.Actualizar_usuario = QtWidgets.QPushButton(self.centralwidget)
        self.Actualizar_usuario.setGeometry(QtCore.QRect(120, 100, 141, 31))
        self.Actualizar_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Actualizar_usuario.setObjectName("Actualizar_usuario")
        self.Eliminar_usuario = QtWidgets.QPushButton(self.centralwidget)
        self.Eliminar_usuario.setGeometry(QtCore.QRect(270, 100, 141, 31))
        self.Eliminar_usuario.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Eliminar_usuario.setObjectName("Eliminar_usuario")
        self.Ver_usuarios = QtWidgets.QPushButton(self.centralwidget)
        self.Ver_usuarios.setGeometry(QtCore.QRect(420, 100, 131, 31))
        self.Ver_usuarios.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Ver_usuarios.setObjectName("Ver_usuarios")
        self.Base_datos = QtWidgets.QPushButton(self.centralwidget)
        self.Base_datos.setGeometry(QtCore.QRect(560, 100, 131, 31))
        self.Base_datos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Base_datos.setObjectName("Base_datos")
        MenuAdmin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuAdmin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 21))
        self.menubar.setObjectName("menubar")
        MenuAdmin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuAdmin)
        self.statusbar.setObjectName("statusbar")
        MenuAdmin.setStatusBar(self.statusbar)

        self.retranslateUi(MenuAdmin)
        QtCore.QMetaObject.connectSlotsByName(MenuAdmin)

    def retranslateUi(self, MenuAdmin):
        _translate = QtCore.QCoreApplication.translate
        MenuAdmin.setWindowTitle(_translate("MenuAdmin", "MainWindow"))
        self.label.setText(_translate("MenuAdmin", "<html><head/><body><p><span style=\" font-weight:600; color:#ffff00;\">ADMINISTRADOR</span></p></body></html>"))
        self.label_2.setText(_translate("MenuAdmin", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))
        self.Alta_usuario.setText(_translate("MenuAdmin", "Alta Usuario"))
        self.Actualizar_usuario.setText(_translate("MenuAdmin", "Actualizar Usuario"))
        self.Eliminar_usuario.setText(_translate("MenuAdmin", "Eliminar Usuario"))
        self.Ver_usuarios.setText(_translate("MenuAdmin", "Ver Usuarios"))
        self.Base_datos.setText(_translate("MenuAdmin", "Base de Datos"))
        self.Alta_usuario.clicked.connect(self.AbrirAltaUsuario)
        self.Actualizar_usuario.clicked.connect(self.ActualizarUsuario)
        self.Eliminar_usuario.clicked.connect(self.AbrirEliminarUsuario)
        self.Ver_usuarios.clicked.connect(self.AbrirRegistrosUsuarios)
        self.Base_datos.clicked.connect(self.AbrirBD)

    def AbrirAltaUsuario(self):
            import os
            os.system('alta_usuario.py')
    
    def ActualizarUsuario(self):
            import os
            os.system('update_usuario.py')

    def AbrirEliminarUsuario(self):
            import os
            os.system('eliminar_usuario.py')
    
    def AbrirRegistrosUsuarios(self):
            import os
            os.system('verregistrosusuarios.py')

    def AbrirBD(self):
            import os
            os.system('Menu_cotizador.py')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuAdmin = QtWidgets.QMainWindow()
    ui = Ui_MenuAdmin()
    ui.setupUi(MenuAdmin)
    MenuAdmin.show()
    sys.exit(app.exec_())

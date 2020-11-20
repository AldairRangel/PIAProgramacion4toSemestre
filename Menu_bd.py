from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu_bd(object):
    def setupUi(self, Menu_bd):
        Menu_bd.setObjectName("Menu_bd")
        Menu_bd.resize(615, 276)
        Menu_bd.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(Menu_bd)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(0, 0, 601, 31))
        self.titulo.setObjectName("titulo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 601, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 200, 211, 31))
        self.label_2.setObjectName("label_2")
        self.Alta_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.Alta_cliente.setGeometry(QtCore.QRect(40, 150, 101, 31))
        self.Alta_cliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Alta_cliente.setObjectName("Alta_cliente")
        self.Actualizar_datos = QtWidgets.QPushButton(self.centralwidget)
        self.Actualizar_datos.setGeometry(QtCore.QRect(150, 150, 131, 31))
        self.Actualizar_datos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Actualizar_datos.setObjectName("Actualizar_datos")
        self.Eliminar_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.Eliminar_cliente.setGeometry(QtCore.QRect(290, 150, 131, 31))
        self.Eliminar_cliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Eliminar_cliente.setObjectName("Eliminar_cliente")
        self.Mostrar_clientes = QtWidgets.QPushButton(self.centralwidget)
        self.Mostrar_clientes.setGeometry(QtCore.QRect(430, 150, 131, 31))
        self.Mostrar_clientes.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Mostrar_clientes.setObjectName("Mostrar_clientes")
        Menu_bd.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Menu_bd)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menubar.setObjectName("menubar")
        Menu_bd.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Menu_bd)
        self.statusbar.setObjectName("statusbar")
        Menu_bd.setStatusBar(self.statusbar)

        self.retranslateUi(Menu_bd)
        QtCore.QMetaObject.connectSlotsByName(Menu_bd)

    def retranslateUi(self, Menu_bd):
        _translate = QtCore.QCoreApplication.translate
        Menu_bd.setWindowTitle(_translate("Menu_bd", "MainWindow"))
        self.titulo.setText(_translate("Menu_bd", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">BASE DE DATOS</span></p></body></html>"))
        self.label.setText(_translate("Menu_bd", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#eb9b0f;\">Selecciona la tarea a realizar:</span></p></body></html>"))
        self.label_2.setText(_translate("Menu_bd", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))
        self.Alta_cliente.setText(_translate("Menu_bd", "Alta Cliente"))
        self.Actualizar_datos.setText(_translate("Menu_bd", "Actualizar Datos"))
        self.Eliminar_cliente.setText(_translate("Menu_bd", "Eliminar Cliente"))
        self.Mostrar_clientes.setText(_translate("Menu_bd", "Mostrar Clientes"))
        self.Alta_cliente.clicked.connect(self.AltaDeCliente)
        #self.Actualizar_datos.clicked.connect(self.ActualizarDatos)
        #self.Eliminar_cliente.clicked.connect(self.EliminarCliente)
        #self.Mostrar_clientes.clicked.connect(self.MostrarClientes)

    def AltaDeCliente(self):
            import os
            os.system('Alta_cliente.py')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu_bd = QtWidgets.QMainWindow()
    ui = Ui_Menu_bd()
    ui.setupUi(Menu_bd)
    Menu_bd.show()
    sys.exit(app.exec_())

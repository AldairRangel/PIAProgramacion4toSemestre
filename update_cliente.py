from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import date

class Ui_V_updatecliente(object):
        def VerificarCliente(self):
                with sqlite3.connect('bdpaneles.db') as conn:
                        datousuario = self.TE_idcliente.toPlainText() #toPlainText
                        usuario = str(datousuario)
                        cursorm = conn.cursor()
                        cursorm.execute("SELECT Id_cliente FROM Cliente")
                        listausuarios = []
                        infousuarios = cursorm.fetchall()
                        for dato in infousuarios:
                                for n in dato:
                                        infousuarios = str(n)
                                        listausuarios.append(infousuarios)
                        if usuario in listausuarios:
                                import os
                                os.system('vclientevalido.py')
                        else:
                                import os
                                os.system('vclientenovalido.py')

        def ActualizarClientes(self):
                with sqlite3.connect('bdpaneles.db') as conn:
                        c= conn.cursor()
                        id_clienteC = str(self.TE_idcliente.toPlainText())
                        nombresC = str(self.TE_nombres.toPlainText())
                        apellidosC = str(self.TE_apellidos.toPlainText())
                        direccionC = str(self.TE_direccion.toPlainText())
                        municipioC = str(self.TE_municipio.toPlainText())
                        correoC = str(self.TE_correo.toPlainText())
                        telefonoC = str(self.TE_telefono.toPlainText())
                        panelesC = str(self.TE_panelescotizados.toPlainText())
                        today = str(date.today())
                        datos = (id_clienteC, nombresC, apellidosC, direccionC, municipioC, correoC, telefonoC, panelesC, today, id_clienteC)
                        c.execute('UPDATE Cliente SET Id_cliente = ?, Nombres = ?, Apellidos = ?, Direccion = ?, Municipio = ?, correo_contacto = ?, Telefono = ?, Paneles_cotizados = ?, fecha_cotizacion = ? WHERE id_cliente = ?', datos)
                        import os
                        os.system('vclienteactualizado.py')
                conn.close()   

        def setupUi(self, V_updatecliente):
                V_updatecliente.setObjectName("V_updatecliente")
                V_updatecliente.resize(560, 629)
                V_updatecliente.setStyleSheet("background-color: rgb(0, 0, 0);")
                self.centralwidget = QtWidgets.QWidget(V_updatecliente)
                self.centralwidget.setObjectName("centralwidget")
                self.lb_titulo = QtWidgets.QLabel(self.centralwidget)
                self.lb_titulo.setGeometry(QtCore.QRect(0, 0, 551, 31))
                self.lb_titulo.setObjectName("lb_titulo")
                self.lb_nombres = QtWidgets.QLabel(self.centralwidget)
                self.lb_nombres.setGeometry(QtCore.QRect(10, 120, 131, 41))
                self.lb_nombres.setObjectName("lb_nombres")
                self.lb_apellidos = QtWidgets.QLabel(self.centralwidget)
                self.lb_apellidos.setGeometry(QtCore.QRect(10, 180, 131, 31))
                self.lb_apellidos.setObjectName("lb_apellidos")
                self.lb_direccion = QtWidgets.QLabel(self.centralwidget)
                self.lb_direccion.setGeometry(QtCore.QRect(0, 230, 151, 31))
                self.lb_direccion.setObjectName("lb_direccion")
                self.lb_municipio = QtWidgets.QLabel(self.centralwidget)
                self.lb_municipio.setGeometry(QtCore.QRect(0, 280, 151, 31))
                self.lb_municipio.setObjectName("lb_municipio")
                self.lb_correo = QtWidgets.QLabel(self.centralwidget)
                self.lb_correo.setGeometry(QtCore.QRect(0, 330, 141, 31))
                self.lb_correo.setObjectName("lb_correo")
                self.lb_panelescotizados = QtWidgets.QLabel(self.centralwidget)
                self.lb_panelescotizados.setGeometry(QtCore.QRect(10, 430, 141, 31))
                self.lb_panelescotizados.setObjectName("lb_panelescotizados")
                self.lb_paginaweb = QtWidgets.QLabel(self.centralwidget)
                self.lb_paginaweb.setGeometry(QtCore.QRect(370, 560, 181, 16))
                self.lb_paginaweb.setObjectName("lb_paginaweb")
                self.TE_nombres = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_nombres.setGeometry(QtCore.QRect(160, 120, 391, 41))
                self.TE_nombres.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_nombres.setObjectName("TE_nombres")
                self.TE_apellidos = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_apellidos.setGeometry(QtCore.QRect(160, 170, 391, 41))
                self.TE_apellidos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_apellidos.setObjectName("TE_apellidos")
                self.TE_direccion = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_direccion.setGeometry(QtCore.QRect(160, 220, 391, 41))
                self.TE_direccion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_direccion.setObjectName("TE_direccion")
                self.TE_municipio = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_municipio.setGeometry(QtCore.QRect(160, 270, 391, 41))
                self.TE_municipio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_municipio.setObjectName("TE_municipio")
                self.TE_correo = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_correo.setGeometry(QtCore.QRect(160, 320, 391, 41))
                self.TE_correo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_correo.setObjectName("TE_correo")
                self.TE_panelescotizados = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_panelescotizados.setGeometry(QtCore.QRect(160, 420, 61, 41))
                self.TE_panelescotizados.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_panelescotizados.setObjectName("TE_panelescotizados")
                self.Boton_guardar = QtWidgets.QPushButton(self.centralwidget)
                self.Boton_guardar.setGeometry(QtCore.QRect(240, 490, 111, 51))
                self.Boton_guardar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 11pt \"Tahoma\";")
                self.Boton_guardar.setObjectName("Boton_guardar")
                self.Boton_guardar.clicked.connect(self.ActualizarClientes)
                self.Boton_guardar_2 = QtWidgets.QPushButton(self.centralwidget)
                self.Boton_guardar_2.setGeometry(QtCore.QRect(360, 490, 161, 51))
                self.Boton_guardar_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 11pt \"Tahoma\";")
                self.Boton_guardar_2.setObjectName("Boton_guardar_2")
                self.lb_telefono = QtWidgets.QLabel(self.centralwidget)
                self.lb_telefono.setGeometry(QtCore.QRect(0, 380, 141, 31))
                self.lb_telefono.setObjectName("lb_telefono")
                self.TE_telefono = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_telefono.setGeometry(QtCore.QRect(160, 370, 391, 41))
                self.TE_telefono.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_telefono.setObjectName("TE_telefono")
                self.lb_idcliente = QtWidgets.QLabel(self.centralwidget)
                self.lb_idcliente.setGeometry(QtCore.QRect(10, 70, 131, 41))
                self.lb_idcliente.setObjectName("lb_idcliente")
                self.TE_idcliente = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_idcliente.setGeometry(QtCore.QRect(160, 70, 131, 41))
                self.TE_idcliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_idcliente.setObjectName("TE_idcliente")
                self.Boton_verificarid = QtWidgets.QPushButton(self.centralwidget)
                self.Boton_verificarid.setGeometry(QtCore.QRect(90, 490, 141, 51))
                self.Boton_verificarid.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 11pt \"Tahoma\";")
                self.Boton_verificarid.setObjectName("Boton_verificarid")
                self.Boton_verificarid.clicked.connect(self.VerificarCliente)
                V_updatecliente.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(V_updatecliente)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
                self.menubar.setObjectName("menubar")
                V_updatecliente.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(V_updatecliente)
                self.statusbar.setObjectName("statusbar")
                V_updatecliente.setStatusBar(self.statusbar)

                self.retranslateUi(V_updatecliente)
                self.Boton_guardar_2.clicked.connect(self.TE_panelescotizados.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_correo.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_municipio.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_direccion.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_apellidos.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_nombres.clear)
                QtCore.QMetaObject.connectSlotsByName(V_updatecliente)

        def retranslateUi(self, V_updatecliente):
                _translate = QtCore.QCoreApplication.translate
                V_updatecliente.setWindowTitle(_translate("V_updatecliente", "MainWindow"))
                self.lb_titulo.setText(_translate("V_updatecliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\">ACTUALIZACIÓN DATOS DE CLIENTE</span></p></body></html>"))
                self.lb_nombres.setText(_translate("V_updatecliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Nombres:</span></p></body></html>"))
                self.lb_apellidos.setText(_translate("V_updatecliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Apellidos:</span></p></body></html>"))
                self.lb_direccion.setText(_translate("V_updatecliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Dirección:</span></p></body></html>"))
                self.lb_municipio.setText(_translate("V_updatecliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Municipio:</span></p></body></html>"))
                self.lb_correo.setText(_translate("V_updatecliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Correo electronico:</span></p></body></html>"))
                self.lb_panelescotizados.setText(_translate("V_updatecliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Paneles cotizados:</span></p></body></html>"))
                self.lb_paginaweb.setText(_translate("V_updatecliente", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))
                self.Boton_guardar.setText(_translate("V_updatecliente", "Guardar"))
                self.Boton_guardar_2.setText(_translate("V_updatecliente", "Borrar datos ingresados"))
                self.lb_telefono.setText(_translate("V_updatecliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Telefono:</span></p></body></html>"))
                self.lb_idcliente.setText(_translate("V_updatecliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">ID de cliente:</span></p></body></html>"))
                self.Boton_verificarid.setText(_translate("V_updatecliente", "Verificar ID cliente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    V_updatecliente = QtWidgets.QMainWindow()
    ui = Ui_V_updatecliente()
    ui.setupUi(V_updatecliente)
    V_updatecliente.show()
    sys.exit(app.exec_())

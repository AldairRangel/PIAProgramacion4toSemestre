from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from datetime import date

class Ui_V_Alta_cliente(object):
        def GuardarAltaCliente(self): #Función para guardar cliente nuevo
                with sqlite3.connect('bdpaneles.db') as conn:
                        c=conn.cursor()
                        c.execute('SELECT COUNT(*) FROM Cliente;') #Contar ultimo id registrado
                        cliente = c.fetchall()
                        for i in cliente:
                                for j in i:
                                        id_cliente = j + 1 #asignar nuevo id
                        id_cliente_progresivo = str(id_cliente) #id almacenado
                        nombresC = str(self.TE_nombres.toPlainText())
                        apellidosC = str(self.TE_apellidos.toPlainText())
                        direccionC = str(self.TE_direccion.toPlainText())
                        municipioC = str(self.TE_municipio.toPlainText())
                        correoC = str(self.TE_correo.toPlainText())
                        telefonoC = str(self.TE_telefono.toPlainText())
                        panelesC = str(self.TE_panelescotizados.toPlainText())
                        today = str(date.today())
                        c.execute('INSERT INTO Cliente VALUES("'+id_cliente_progresivo+'", "'+nombresC+'", "'+apellidosC+'", "'+direccionC+'", "'+municipioC+'", "'+correoC+'", "'+telefonoC+'", "'+panelesC+'", "'+today+'");')
                        import os
                        os.system('vclienteagregado.py') #ventana cliente agregado
                conn.close()   

        def setupUi(self, V_Alta_cliente): #Ventana PyQt5
                V_Alta_cliente.setObjectName("V_Alta_cliente")
                V_Alta_cliente.resize(559, 531)
                V_Alta_cliente.setStyleSheet("background-color: rgb(0, 0, 0);")
                self.centralwidget = QtWidgets.QWidget(V_Alta_cliente)
                self.centralwidget.setObjectName("centralwidget")
                self.lb_titulo = QtWidgets.QLabel(self.centralwidget)
                self.lb_titulo.setGeometry(QtCore.QRect(0, 0, 551, 31))
                self.lb_titulo.setObjectName("lb_titulo")
                self.lb_nombres = QtWidgets.QLabel(self.centralwidget)
                self.lb_nombres.setGeometry(QtCore.QRect(10, 70, 131, 41))
                self.lb_nombres.setObjectName("lb_nombres")
                self.lb_apellidos = QtWidgets.QLabel(self.centralwidget)
                self.lb_apellidos.setGeometry(QtCore.QRect(10, 130, 131, 31))
                self.lb_apellidos.setObjectName("lb_apellidos")
                self.lb_direccion = QtWidgets.QLabel(self.centralwidget)
                self.lb_direccion.setGeometry(QtCore.QRect(0, 180, 151, 31))
                self.lb_direccion.setObjectName("lb_direccion")
                self.lb_municipio = QtWidgets.QLabel(self.centralwidget)
                self.lb_municipio.setGeometry(QtCore.QRect(0, 230, 151, 31))
                self.lb_municipio.setObjectName("lb_municipio")
                self.lb_correo = QtWidgets.QLabel(self.centralwidget)
                self.lb_correo.setGeometry(QtCore.QRect(0, 280, 141, 31))
                self.lb_correo.setObjectName("lb_correo")
                self.lb_panelescotizados = QtWidgets.QLabel(self.centralwidget)
                self.lb_panelescotizados.setGeometry(QtCore.QRect(10, 380, 141, 31))
                self.lb_panelescotizados.setObjectName("lb_panelescotizados")
                self.lb_paginaweb = QtWidgets.QLabel(self.centralwidget)
                self.lb_paginaweb.setGeometry(QtCore.QRect(380, 460, 181, 16))
                self.lb_paginaweb.setObjectName("lb_paginaweb")
                self.TE_nombres = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_nombres.setGeometry(QtCore.QRect(160, 70, 391, 41))
                self.TE_nombres.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_nombres.setObjectName("TE_nombres")
                self.TE_apellidos = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_apellidos.setGeometry(QtCore.QRect(160, 120, 391, 41))
                self.TE_apellidos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_apellidos.setObjectName("TE_apellidos")
                self.TE_direccion = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_direccion.setGeometry(QtCore.QRect(160, 170, 391, 41))
                self.TE_direccion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_direccion.setObjectName("TE_direccion")
                self.TE_municipio = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_municipio.setGeometry(QtCore.QRect(160, 220, 391, 41))
                self.TE_municipio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_municipio.setObjectName("TE_municipio")
                self.TE_correo = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_correo.setGeometry(QtCore.QRect(160, 270, 391, 41))
                self.TE_correo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_correo.setObjectName("TE_correo")
                self.TE_panelescotizados = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_panelescotizados.setGeometry(QtCore.QRect(160, 370, 61, 41))
                self.TE_panelescotizados.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_panelescotizados.setObjectName("TE_panelescotizados")
                self.Boton_guardar = QtWidgets.QPushButton(self.centralwidget)
                self.Boton_guardar.setGeometry(QtCore.QRect(250, 390, 111, 51))
                self.Boton_guardar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 11pt \"Tahoma\";")
                self.Boton_guardar.setObjectName("Boton_guardar")
                self.Boton_guardar_2 = QtWidgets.QPushButton(self.centralwidget)
                self.Boton_guardar_2.setGeometry(QtCore.QRect(370, 390, 161, 51))
                self.Boton_guardar_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 11pt \"Tahoma\";")
                self.Boton_guardar_2.setObjectName("Boton_guardar_2")
                self.lb_telefono = QtWidgets.QLabel(self.centralwidget)
                self.lb_telefono.setGeometry(QtCore.QRect(0, 330, 141, 31))
                self.lb_telefono.setObjectName("lb_telefono")
                self.TE_telefono = QtWidgets.QTextEdit(self.centralwidget)
                self.TE_telefono.setGeometry(QtCore.QRect(160, 320, 391, 41))
                self.TE_telefono.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
                self.TE_telefono.setObjectName("TE_telefono")
                V_Alta_cliente.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(V_Alta_cliente)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 21))
                self.menubar.setObjectName("menubar")
                V_Alta_cliente.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(V_Alta_cliente)
                self.statusbar.setObjectName("statusbar")
                V_Alta_cliente.setStatusBar(self.statusbar)

                self.retranslateUi(V_Alta_cliente)
                self.Boton_guardar_2.clicked.connect(self.TE_panelescotizados.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_correo.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_municipio.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_direccion.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_apellidos.clear)
                self.Boton_guardar_2.clicked.connect(self.TE_nombres.clear)
                QtCore.QMetaObject.connectSlotsByName(V_Alta_cliente)

        def retranslateUi(self, V_Alta_cliente):
                _translate = QtCore.QCoreApplication.translate
                V_Alta_cliente.setWindowTitle(_translate("V_Alta_cliente", "MainWindow"))
                self.lb_titulo.setText(_translate("V_Alta_cliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\">ALTA DE CLIENTE</span></p></body></html>"))
                self.lb_nombres.setText(_translate("V_Alta_cliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Nombres:</span></p></body></html>"))
                self.lb_apellidos.setText(_translate("V_Alta_cliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Apellidos:</span></p></body></html>"))
                self.lb_direccion.setText(_translate("V_Alta_cliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Dirección:</span></p></body></html>"))
                self.lb_municipio.setText(_translate("V_Alta_cliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Municipio:</span></p></body></html>"))
                self.lb_correo.setText(_translate("V_Alta_cliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Correo electronico:</span></p></body></html>"))
                self.lb_panelescotizados.setText(_translate("V_Alta_cliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Paneles cotizados:</span></p></body></html>"))
                self.lb_paginaweb.setText(_translate("V_Alta_cliente", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))
                self.Boton_guardar.setText(_translate("V_Alta_cliente", "Guardar"))
                self.Boton_guardar_2.setText(_translate("V_Alta_cliente", "Borrar datos ingresados"))
                self.lb_telefono.setText(_translate("V_Alta_cliente", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Telefono:</span></p></body></html>"))
                self.Boton_guardar.clicked.connect(self.GuardarAltaCliente)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    V_Alta_cliente = QtWidgets.QMainWindow()
    ui = Ui_V_Alta_cliente()
    ui.setupUi(V_Alta_cliente)
    V_Alta_cliente.show()
    sys.exit(app.exec_())

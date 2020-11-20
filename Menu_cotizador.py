from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_V_cotizadorBD(object):
    def setupUi(self, V_cotizadorBD):
        V_cotizadorBD.setObjectName("V_cotizadorBD")
        V_cotizadorBD.resize(651, 224)
        V_cotizadorBD.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(V_cotizadorBD)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lb_titulo.setGeometry(QtCore.QRect(20, 0, 301, 41))
        self.lb_titulo.setStyleSheet("font: 14pt \"Arial\";")
        self.lb_titulo.setObjectName("lb_titulo")
        self.Alta_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.Alta_cliente.setGeometry(QtCore.QRect(20, 80, 101, 31))
        self.Alta_cliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Alta_cliente.setObjectName("Alta_cliente")
        self.Actualizar_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.Actualizar_cliente.setGeometry(QtCore.QRect(130, 80, 141, 31))
        self.Actualizar_cliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Actualizar_cliente.setObjectName("Actualizar_cliente")
        self.lb_pagweb = QtWidgets.QLabel(self.centralwidget)
        self.lb_pagweb.setGeometry(QtCore.QRect(490, 160, 151, 16))
        self.lb_pagweb.setObjectName("lb_pagweb")
        self.Consulta_clientes = QtWidgets.QPushButton(self.centralwidget)
        self.Consulta_clientes.setGeometry(QtCore.QRect(280, 80, 211, 31))
        self.Consulta_clientes.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Consulta_clientes.setObjectName("Consulta_clientes")
        self.Eliminar_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.Eliminar_cliente.setGeometry(QtCore.QRect(500, 80, 141, 31))
        self.Eliminar_cliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Eliminar_cliente.setObjectName("Eliminar_cliente")
        V_cotizadorBD.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(V_cotizadorBD)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menubar.setObjectName("menubar")
        V_cotizadorBD.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(V_cotizadorBD)
        self.statusbar.setObjectName("statusbar")
        V_cotizadorBD.setStatusBar(self.statusbar)

        self.retranslateUi(V_cotizadorBD)
        QtCore.QMetaObject.connectSlotsByName(V_cotizadorBD)

    def retranslateUi(self, V_cotizadorBD):
        _translate = QtCore.QCoreApplication.translate
        V_cotizadorBD.setWindowTitle(_translate("V_cotizadorBD", "MainWindow"))
        self.lb_titulo.setText(_translate("V_cotizadorBD", "<html><head/><body><p><span style=\" font-weight:600; color:#ffff00;\">COTIZADOR - BASE DE DATOS</span></p></body></html>"))
        self.Alta_cliente.setText(_translate("V_cotizadorBD", "Alta Cliente"))
        self.Actualizar_cliente.setText(_translate("V_cotizadorBD", "Actualizar Cliente"))
        self.lb_pagweb.setText(_translate("V_cotizadorBD", "<html><head/><body><p><span style=\" font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))
        self.Consulta_clientes.setText(_translate("V_cotizadorBD", "Consultar Clientes Cotizados"))
        self.Eliminar_cliente.setText(_translate("V_cotizadorBD", "Eliminar Cliente"))
        
        self.Alta_cliente.clicked.connect(self.AltaDeCliente)  
        self.Actualizar_cliente.clicked.connect(self.ActualizarClientes)
        self.Consulta_clientes.clicked.connect(self.ConsultarClientesGuardados)
        self.Eliminar_cliente.clicked.connect(self.EliminarClientes)

    def AltaDeCliente(self):
            import os
            os.system('alta_cliente.py')

    def ActualizarClientes(self):
            import os
            os.system('update_cliente.py')

    def ConsultarClientesGuardados(self):
            import os
            os.system('verregistrosclientes.py')
   
    def EliminarClientes(self):
            import os
            os.system('eliminar_cliente.py')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    V_cotizadorBD = QtWidgets.QMainWindow()
    ui = Ui_V_cotizadorBD()
    ui.setupUi(V_cotizadorBD)
    V_cotizadorBD.show()
    sys.exit(app.exec_())
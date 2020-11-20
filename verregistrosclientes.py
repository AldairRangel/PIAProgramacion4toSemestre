from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_v_clientesregistrados(object):
    def OrdenDeRegistroClientes(self):
        with sqlite3.connect('bdpaneles.db') as conn:
            c = conn.cursor()
            consulta = c.execute('SELECT * FROM Cliente;')
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(consulta):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def OrdenClientesApellidos(self):
        with sqlite3.connect('bdpaneles.db') as conn:
            c = conn.cursor()
            consulta = c.execute('SELECT * FROM Cliente ORDER BY Apellidos ASC;')
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(consulta):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def setupUi(self, v_clientesregistrados):
        v_clientesregistrados.setObjectName("v_clientesregistrados")
        v_clientesregistrados.resize(945, 544)
        v_clientesregistrados.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(v_clientesregistrados)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 931, 331))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.lb_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lb_titulo.setGeometry(QtCore.QRect(10, 10, 931, 31))
        self.lb_titulo.setObjectName("lb_titulo")
        self.pb_orden = QtWidgets.QPushButton(self.centralwidget)
        self.pb_orden.setGeometry(QtCore.QRect(310, 420, 141, 41))
        self.pb_orden.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_orden.setObjectName("pb_orden")
        self.pb_orden.clicked.connect(self.OrdenDeRegistroClientes)
        self.pb_apellidoasc = QtWidgets.QPushButton(self.centralwidget)
        self.pb_apellidoasc.setGeometry(QtCore.QRect(520, 420, 181, 41))
        self.pb_apellidoasc.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_apellidoasc.setObjectName("pb_apellidoasc")
        self.pb_apellidoasc.clicked.connect(self.OrdenClientesApellidos)
        self.lb_web = QtWidgets.QLabel(self.centralwidget)
        self.lb_web.setGeometry(QtCore.QRect(720, 480, 231, 31))
        self.lb_web.setObjectName("lb_web")
        v_clientesregistrados.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(v_clientesregistrados)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 21))
        self.menubar.setObjectName("menubar")
        v_clientesregistrados.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(v_clientesregistrados)
        self.statusbar.setObjectName("statusbar")
        v_clientesregistrados.setStatusBar(self.statusbar)

        self.retranslateUi(v_clientesregistrados)
        QtCore.QMetaObject.connectSlotsByName(v_clientesregistrados)

    def retranslateUi(self, v_clientesregistrados):
        _translate = QtCore.QCoreApplication.translate
        v_clientesregistrados.setWindowTitle(_translate("v_clientesregistrados", "MainWindow"))
        self.lb_titulo.setText(_translate("v_clientesregistrados", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\">CLIENTES MONTERREY PANELES SOLARES</span></p></body></html>"))
        self.pb_orden.setText(_translate("v_clientesregistrados", "Orden de registro"))
        self.pb_apellidoasc.setText(_translate("v_clientesregistrados", "Por apellido ascendente"))
        self.lb_web.setText(_translate("v_clientesregistrados", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    v_clientesregistrados = QtWidgets.QMainWindow()
    ui = Ui_v_clientesregistrados()
    ui.setupUi(v_clientesregistrados)
    v_clientesregistrados.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_v_usuariosregistrados(object):
    def OrdenDeRegistro(self):
        with sqlite3.connect('bdpaneles.db') as conn:
            c = conn.cursor()
            consulta = c.execute('SELECT * FROM User;')
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(consulta):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def UsuarioAscendente(self):
        with sqlite3.connect('bdpaneles.db') as conn:
            c = conn.cursor()
            consulta = c.execute('SELECT * FROM User ORDER BY Usuario ASC;')
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(consulta):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        conn.close()


    def setupUi(self, v_usuariosregistrados):
        v_usuariosregistrados.setObjectName("v_usuariosregistrados")
        v_usuariosregistrados.resize(659, 558)
        v_usuariosregistrados.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(v_usuariosregistrados)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 641, 331))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.lb_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lb_titulo.setGeometry(QtCore.QRect(10, 10, 641, 31))
        self.lb_titulo.setObjectName("lb_titulo")
        self.pb_orden = QtWidgets.QPushButton(self.centralwidget)
        self.pb_orden.setGeometry(QtCore.QRect(150, 430, 141, 31))
        self.pb_orden.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_orden.setObjectName("pb_orden")
        self.pb_orden.clicked.connect(self.OrdenDeRegistro)
        self.pb_usuarioasc = QtWidgets.QPushButton(self.centralwidget)
        self.pb_usuarioasc.setGeometry(QtCore.QRect(350, 430, 161, 31))
        self.pb_usuarioasc.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.pb_usuarioasc.setObjectName("pb_usuarioasc")
        self.pb_usuarioasc.clicked.connect(self.UsuarioAscendente)
        self.lb_web = QtWidgets.QLabel(self.centralwidget)
        self.lb_web.setGeometry(QtCore.QRect(430, 490, 231, 31))
        self.lb_web.setObjectName("lb_web")
        v_usuariosregistrados.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(v_usuariosregistrados)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 21))
        self.menubar.setObjectName("menubar")
        v_usuariosregistrados.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(v_usuariosregistrados)
        self.statusbar.setObjectName("statusbar")
        v_usuariosregistrados.setStatusBar(self.statusbar)

        self.retranslateUi(v_usuariosregistrados)
        QtCore.QMetaObject.connectSlotsByName(v_usuariosregistrados)

    def retranslateUi(self, v_usuariosregistrados):
        _translate = QtCore.QCoreApplication.translate
        v_usuariosregistrados.setWindowTitle(_translate("v_usuariosregistrados", "MainWindow"))
        self.lb_titulo.setText(_translate("v_usuariosregistrados", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffff00;\">USUARIOS MONTERREY PANELES SOLARES</span></p></body></html>"))
        self.pb_orden.setText(_translate("v_usuariosregistrados", "Orden de registro"))
        self.pb_usuarioasc.setText(_translate("v_usuariosregistrados", "Usuario Ascendente"))
        self.lb_web.setText(_translate("v_usuariosregistrados", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffff00;\">monterreypanelsolar.com</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    v_usuariosregistrados = QtWidgets.QMainWindow()
    ui = Ui_v_usuariosregistrados()
    ui.setupUi(v_usuariosregistrados)
    v_usuariosregistrados.show()
    sys.exit(app.exec_())

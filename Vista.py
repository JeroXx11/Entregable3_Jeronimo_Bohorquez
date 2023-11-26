from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QMessageBox, QSlider, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import os

class Vista(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("InicioSesion.ui",self)
    def AñadirControlador(self,Coordinador):
        self.mi_Controlador = Coordinador
        self.SetUp()
    def SetUp(self):
        self.pushButton.clicked.connect(self.Inicio, self.AbrirSlider)

    def Inicio(self):
        Usuario = self.lineEdit.text()
        Contraseña = self.lineEdit_2.text()
        resultado = self.Controlador.Validar(Usuario,Contraseña)
        if resultado:
            texto = "El usuario esta en el sistema"
            msj = QMessageBox(self)
            msj.setIcon(QMessageBox.Information)
            msj.setText(texto)
            msj.windowTitle("Info")
            msj.show
        else:
            texto = "Usuario Incorrecto"
            msj = QMessageBox(self)
            msj.setIcon(QMessageBox.Warning)
            msj.setText(texto)
            msj.windowTitle("Alerta")
            msj.show
        print(resultado)
    def AbrirSlider(self):
        Ventana_slider = ventanaSlider(self)
        Ventana_slider.AñadirControlador(self.Mensajero)
        self.hide()
        Ventana_slider.show()
class ventanaSlider(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        loadUi("Slider.ui",self)
        #Vista = parent
        self.setup()
    def setup(self):
        self.carpeta = "Circle of Willis"
        lista_archivos = os.listdir(self.carpeta)
        self.slider.valueChanged.connect(self.Cargar)
        self.pushButton.clicked.connect(self.salir)
        for archivo in lista_archivos:
            self.slider.addItem(archivo)
    def Cargar(self):
        imagen = self.slider.valueChanged.connect()
        self.Controlador.img_conextion(imagen)
        pixmap = QPixmap("temp_image.png")
        self.img.setPixmap(pixmap)
        os.remove('temp_image.png')
    def salir(self):
        ventana_login = Vista(self)
        ventana_login.AñadirControlador(self.Mensajero)
        self.hide()
        ventana_login.show()
    def Controlador(self,c):
        Controlador = c
    
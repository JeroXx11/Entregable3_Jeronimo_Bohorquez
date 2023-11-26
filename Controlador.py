from PyQt5.QtWidgets import QApplication
from Modelo import InicioSesionModelo
from Vista import Vista
import sys 

class InicioSesionControlador:
    def __init__(self,Vista,InicioSesionModelo):
        self.mi_Modelo = InicioSesionModelo
        self.mi_Vista = Vista
    def VerificarInicio(self,l,p):
        return self.mi_Modelo.Validar(l, p)
    def img_conextion(self, imagen):
        self.mi_Modelo.picture_creator(imagen)
def main():
    app = QApplication(sys.argv)
    mi_Vista = Vista()
    mi_Modelo = InicioSesionModelo
    mi_Controlador = InicioSesionControlador (mi_Vista,mi_Modelo)
    mi_Vista.AñadirControlador(mi_Controlador)
    mi_Vista.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main() 
        
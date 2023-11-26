from PyQt5.QtWidgets import QWidget
import pydicom
import matplotlib.pyplot as plt
class InicioSesionModelo:
    def __init__(self):
        self.validar_usuario = "medicoAnalitico"
        self.validar_contraseña = "bio12345"
    def setusuario(self,l):
        self.validar_usuario = l
    def setcontraseña(self,p):
        self.validar_contraseña = p
    def Validar(self,p,l):
        return (self.validar_usuario == l) and (self.validar_contraseña == p)
class VentanaSliderModelo(QWidget):
    def __init__(self):
        super().__init__()
        self.carpeta = 'Circle of Willis'

    def picture_creator(self, imagen):
        ds = pydicom.dcmread(self.carpeta+'/'+imagen)
        pixel_data = ds.pixel_array
        if (len(pixel_data.shape))==3:
            slice_index = pixel_data.shape[0] // 2
            selected_slice = pixel_data[slice_index, :, :]
            plt.imshow(selected_slice, cmap=plt.cm.bone)
        else:
            plt.imshow(pixel_data, cmap = plt.cm.bone)
        plt.axis('off')
        plt.savefig("temp_image.png")
# Signal y slots
import sys
from PySide6.QtWidgets import *

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signal y Slots')
        # botón
        self.boton = QPushButton('Click aquí')
        
        # Conectamos el evento checado (por default el False)
        # boton.setCheckable(True)
        
        # # Conectamos otro slot al evento checar 
        # boton.clicked.connect(self.evento_checar)
        
        # # Conectamos el evento (signal)click con el slot(evento_click)
        # boton.clicked.connect(self.evento_click)
        
        # Asociamos la señal de click al slot evento_click
        self.boton.clicked.connect(self.evento_click)
        
        # Conectamos a la señal de cambio de título
        self.windowTitleChanged.connect(self.cambio_titulo_app)
        
        # Publicamos el botón
        self.setCentralWidget(self.boton)
        
    def evento_click(self):
        # Cambiar el texto del botón y el titulo de la ventana
        self.boton.setText('Nuevo texto botón')
        self.boton.setEnabled(False)
        self. setWindowTitle('Nuevo titulo de la App')
        print('Evento click')
        
    def cambio_titulo_app(self, nuevo_titulo):
        print(f'Nuevo titulo de la app: {nuevo_titulo}')
        
    # def evento_checar(self, checar): 
    #     self.boton_checado = checar
    #     print(f'Checado? {self.boton_checado}')  
        
    # def evento_click(self):
    #     print('Has hecho click')
    #     # Accedemos al estado del boton (checado)
    #     print(f'Botón checado desde evento click? {self.boton_checado}')
            
if __name__ =='__main__':
    # Creamos el objeto aplicacion
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
import sys 
from PySide6.QtWidgets import *

class VentanaPrincipal(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signal y Slots')
        self.setFixedSize(400, 200)
        
        # Definimos la etiqueta y linea de edición
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        
        # Conectamos el widget de entrada_texto con la etiqueta
        # la señal es texChanged, slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        
        # Publicamos los componentes usando un layout
        disposición = QVBoxLayout()
        disposición.addWidget(self.entrada_texto)
        disposición.addWidget(self.etiqueta)
        
        # Crear un contenedor
        contenedor = QWidget()
        contenedor.setLayout(disposición)
        
        # Publicamos el contenedor
        self.setCentralWidget(contenedor)
        
if __name__ =='__main__':
    # Creamos el objeto aplicacion
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
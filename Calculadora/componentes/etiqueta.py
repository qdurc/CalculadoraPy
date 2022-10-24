from PySide6.QtCore import *
from PySide6.QtWidgets import *

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        
        # Creamos componentes de tipo etiqueta
        etiqueta = QLabel('Hola')
        
        # Modificamos el valor inicial
        etiqueta.setText('Saludos')
        
        # Modificar la fuente
        fuente = etiqueta.font()
        fuente.setPointSize(25)
        etiqueta.setFont(fuente)
        
        # Modificar la alineación de la etiqueta
        etiqueta.setAlignment(Qt.AlignCenter)
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # Publicamos este componente
        self.setCentralWidget(etiqueta)
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
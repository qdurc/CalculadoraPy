from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        self.setFixedSize(500, 600)
        
        # Creamos componentes de tipo etiqueta
        etiqueta = QLabel('Hola')
        etiqueta.setPixmap(QPixmap('/Applications/Phyton/PySide/componentes/layla.jpg'))
        etiqueta.setScaledContents(True)
        
        # Publicamos este componente
        self.setCentralWidget(etiqueta)
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
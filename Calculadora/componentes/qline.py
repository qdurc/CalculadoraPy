from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        
        # Componentes QLinesEdit
        linea_texto = QLineEdit()
        
        # Establecemos el maximo de caracteres a capturar
        linea_texto.setMaxLength(15)
        
        # Establecemos un texto de ayuda
        linea_texto.setPlaceholderText('Introduce tu nombre')
        
        # Solo lectura
        # linea_texto.setReadOnly(True)
        
        # Validación (mask)
        linea_texto.setInputMask('00-0000-0000')
        
        # Evento enter, cambio selección texto, cambio texto
        linea_texto.returnPressed.connect(self.enter_presionado)
        linea_texto.selectionChanged.connect(self.cambio_seleccion)
        linea_texto.textChanged.connect(self.cambio_texto)
        
        # Publicamos este componente
        self.setCentralWidget(linea_texto)
        
    def enter_presionado(self):
        print('Se presionó el enter')
        self.centralWidget().setText('00-0000-0000')
        
    def cambio_seleccion(self):
        print('Cambio selección de texto')
        print(self.centralWidget().selectedText())
        
    def cambio_texto(self, nuevo_texto):
        print(f'Cambio de texto {nuevo_texto}')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
from PySide6.QtWidgets import QMainWindow, QApplication, QSpinBox, QDoubleSpinBox

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        
        # QSpinBox
        # numero = QSpinBox()
        
        # QDoubleSpinBox es para valores flotantes
        numero = QDoubleSpinBox()
        
        # Establece valor minimo y el valor maximo
        # numero.setMinimum(-5)
        # numero.setMaximum(8)
        numero.setRange(-5.5, 8.8)
        
        # Establecemos un prefijo y sufijo
        numero.setPrefix('$')
        numero.setSuffix('c')
        
        # Establecemos el salto (step)
        numero.setSingleStep(.5)
        
        # Nos conectamos al evento de cambio de valor
        # Envia el valor numerico
        numero.valueChanged.connect(self.cambio_valor)
        
        # Envia el valor en texto incluyendo prefijo y sufijo
        numero.textChanged.connect(self.cambio_texto)
       
        # Publicamos este componente
        self.setCentralWidget(numero)
    
    def cambio_valor(self, nuevo_valor):
        print(f'Numero valor: {nuevo_valor}')
        
    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto: {nuevo_texto}')
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
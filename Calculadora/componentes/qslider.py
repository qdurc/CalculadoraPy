from PySide6.QtWidgets import QMainWindow, QApplication, QSlider 

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle('Componentes')
        
        # QSlider es para valores numericos enteros en un slider (deslizador)
        # componente = QSlider(Qt.vertical
        componente = QSlider()
        
        # componente.setMinimum(-5)
        # componente.setMaximum(8)
        componente.setRange(-5, 8)
        
        # Conectamos a las señales 
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_valor) 
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_liberado)
       
        # Publicamos este componente
        self.setCentralWidget(componente)
        
    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor}')
        
    def slider_cambio_valor(self, nueva_posicion):
        print (f'Nueva posicion: {nueva_posicion}')
        
    def slider_presionado(self):
        print(f'Slider presionado')
        
    def slider_liberado(self):
        print(f'Slider liberado')
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
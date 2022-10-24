from PySide6.QtWidgets import QMainWindow, QApplication, QListWidget

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        
        # Componentes QListWidget 
        lista = QListWidget()
        
        # Agregamos elementos
        lista.addItem('Uno')
        lista.addItems(['Dos', 'Tres'])
        
        # Monitoreamos el cambio de elemento selcceionado
        lista.currentItemChanged.connect(self.cambio_elemento)
        lista.currentTextChanged.connect(self.cambio_texto)
        
        # Publicamos este componente
        self.setCentralWidget(lista)
        
    def cambio_elemento(self, nuevo_elemento):
        print(f'Nuevo indice seleccionado: {nuevo_elemento.text()}')
        
    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto seleccionado {nuevo_texto}')
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
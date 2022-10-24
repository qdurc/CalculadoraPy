from PySide6.QtCore import *
from PySide6.QtWidgets import *

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        
        # Creamos un nuevo checkbox
        checkbox = QCheckBox('Este es un checkbox')
        
        # Tenemos 3 estados (0-Apagado, 1-Sin estado, 2-Encendido)
        # Activamos el tercer estado
        checkbox.setTristate(False)
    
        # Conectar la señal de cambio de componentes
        checkbox.stateChanged.connect(self.mostrar_estado)
        
        # Publicamos este componente
        self.setCentralWidget(checkbox)
        
    def mostrar_estado(self, estado):
        print(f'Estado checkbox: {estado}')
        # Trabajamos con las constantes
        if estado == Qt.Checked:
            print('Estado checado')
        elif estado == Qt.PartiallyChecked:
            print('Checkbox parcialmente checado')
        elif estado == Qt.Unchecked:
            print('Checkbox apagado')
        else:
            print('Checkbox con estado inválido')

if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
from PySide6.QtWidgets import QMainWindow, QApplication, QComboBox

class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes')
        
        # Creamos un nuevo combo box (drop down list)
        combobox = QComboBox()
        
        # Agregamos elementos
        combobox.addItem('Uno')
        combobox.addItems(['Dos', 'Tres'])
        
        # Monitoreamos el cambio de elementos seleccionado, tanto de indice como de texto
        combobox.currentIndexChanged.connect(self.cambio_indice) 
        combobox.currentTextChanged.connect(self.cambio_texto) 
        
        # Hacemos editable el combobox
        combobox.setEditable(True)
        
        # Especificamos la politica de inserción
        # combobox.setInsertPolicy(QComboBox.NoInsert)
        
        # Agregar al inicio de nuestro combobox
        # combobox.setInsertPolicy(QComboBox.InsertAtTop)
        
        # Modifica el elemento actual
        # combobox.setInsertPolicy(QComboBox.InsertAtCurrent)
        
        # Insertar al final
        # combobox.setInsertPolicy(QComboBox.InsertAtBottom)
        
        # Limitar cuantos elementos agregamos al combobox
        # combobox.setMaxCount(6)
        
        # Insetar antes del elemento actual
        # combobox.setInsertPolicy(QComboBox.InsertBeforeCurrent)
        
        # Insetar después del elemento actual
        # combobox.setInsertPolicy(QComboBox.InsertAfterCurrent)
        
        # Insetar alfabeticamente
        combobox.setInsertPolicy(QComboBox.InsertAlphabetically)
    
        # Publicamos este componente
        self.setCentralWidget(combobox)
        
    def cambio_indice(self, nuevo_indice):
        print(f'Nuevo indice seleccionado: {nuevo_indice}')
        
    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto seleccionado {nuevo_texto}')
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    app.exec()
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Clase base de Qt (Pyside)
# Se encarga de procesar los eventos (event loop)
app = QApplication()
# Crear objeto ventana
# Cualquier componentes puede ser una ventana en pyside
# ventana = QWidget()
# ventana = QPushButton('Botón PySide')
ventana = QMainWindow()
# Cambiar el titulo
ventana.setWindowTitle('Hola Mundo con PySide')
# Modificar el tamaño de la ventana
ventana.resize(600, 400)
# Mostrar ventana
ventana.show()
# Se ejecuta la aplicación
sys.exit(app.exec())

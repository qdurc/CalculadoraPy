from functools import partial
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton
from PySide6.QtCore import *

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setFixedSize(235, 235) 
        self.componente_general = QWidget(self)
        self.setCentralWidget(self.componente_general)
        
        self.layout_principal = QVBoxLayout()
        self.componente_general.setLayout(self.layout_principal)
        
        self._crear_area_captura()
        self._crear_botones()
        self._conectar_botones()
        
    def _crear_area_captura(self):
        self.linea_entrada = QLineEdit()
        
        self.linea_entrada.setFixedHeight(35)
        self.linea_entrada.setAlignment(Qt.AlignRight)
        self.linea_entrada.setReadOnly(True)
        
        self.layout_principal.addWidget(self.linea_entrada)
        
    def _crear_botones(self):
        self.botones = {}
        layout_botones = QGridLayout()
        # Text | Position
        botones = {
            '7':(0,0),
            '8':(0,1),
            '9':(0,2),
            '/':(0,3),
            '4':(1,0),
            '5':(1,1),
            '6':(1,2),
            '*':(1,3),
            '1':(2,0),
            '2':(2,1),
            '3':(2,2),
            '-':(2,3),
            '0':(3,0),
            '.':(3,1),
            'C':(3,2),
            '+':(3,3),
            '=':(3,4)
        }
        
        for texto_boton, posicion in botones.items():
            self.botones[texto_boton] = QPushButton(texto_boton)
            self.botones[texto_boton].setFixedSize(40,40)
            
            layout_botones.addWidget(self.botones[texto_boton], posicion[0], posicion[1])
        
        self.layout_principal.addLayout(layout_botones)
        
    def _conectar_botones(self):
        for texto_boton, boton in self.botones.items():
            if texto_boton not in {'=','C'}:
                # boton.clicked.connect(lambda: self._construir_expresion(texto_boton))
                boton.clicked.connect(partial(self._construir_expresion, texto_boton))
            
            self.botones['C'].clicked.connect(self._limpiar_linea_entrada)
            self.botones['='].clicked.connect(self._calcular_resultado)
            self.linea_entrada.returnPressed.connect(self._calcular_resultado)
                
    def _construir_expresion(self, texto_boton):
        expresion = self.obtener_texto() + texto_boton
        self.actualizar_texto(expresion)
        
    def obtener_texto(self):
        return self.linea_entrada.text()
    
    def actualizar_texto(self, texto):
        self.linea_entrada.setText(texto)
        self.linea_entrada.setFocus()
        
    def _limpiar_linea_entrada(self):
        self.actualizar_texto('')
        
    def _calcular_resultado(self):
        resultado = self._evaluar_expresion(self.obtener_texto())
        self.actualizar_texto(resultado)
        
    def _evaluar_expresion(self, expresion):
        try:
            resultado = str(eval(expresion))
        except Exception as e:
            resultado = 'Ocurrió un error'
        return resultado
        
if __name__ == '__main__':
    app = QApplication()
    calculadora = Calculadora()
    calculadora.show()
    app.exec()
    
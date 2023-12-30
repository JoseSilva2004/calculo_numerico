#Calculo Numerico
#Realizado por Jose Silva. CI: 30230054

#Importo tanto la libreria unittest para las pruebas como el archivo biseccion
import unittest
from biseccion import *

class TestBiseccion(unittest.TestCase):
    def test_raiz(self):
        self.assertLess(abs(funcion(Biseccion(funcion,0,1,0.04))),0.04) #Pasará la prueba solo si el resultado de la comprobacion sea menor que el margen de error

if __name__ == '__main__':
    unittest.main()

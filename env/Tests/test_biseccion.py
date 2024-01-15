#Calculo Numerico
#Realizado por Jose Silva. CI: 30230054

#Importo tanto la libreria unittest para las pruebas como el archivo biseccion
import unittest
from biseccion import *

class TestBiseccion(unittest.TestCase):
    def test_biseccion1(self):
        #Variables
        a = 0 #Intervalo a
        b = 1 #Intervalo b
        error = 0.01 #Error absoluto
        funcion = lambda x: ma.atan(x) + x - 1 #Funcion

        self.assertLess(abs(funcion(Biseccion(funcion,a,b,error))),error) #Pasará la prueba solo si el resultado de la comprobacion sea menor que el margen de error

    def test_biseccion2(self):
        a = 0.5
        b = 1
        error = 0.01
        funcion = lambda x: ma.sqrt(x**2 + 1) - ma.tan(x)    

        self.assertLess(abs(funcion(Biseccion(funcion,a,b,error))),error)

if __name__ == '__main__':
    unittest.main()

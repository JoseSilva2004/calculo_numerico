#Calculo Numerico
#Realizado por Jose Silva. CI: 30230054

#Importo las librerias
import unittest
from newton_raphson import *

#Declaro la clase para probar el metodo de newton raphson
class TestNewtonRaphson(unittest.TestCase):
    def test_newthon_raphson(self):
        self.assertLess(abs(function(newton_raphson(0.5,0.002,100))),0.002)

if __name__ == '__main__':
    unittest.main()
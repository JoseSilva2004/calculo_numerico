#Calculo Numerico
#Realizado por Jose Silva. CI: 30230054

#Importo las librerias
import unittest
from newton_raphson import *

#Declaro la clase para probar el metodo de newton raphson
class TestNewtonRaphson(unittest.TestCase):
    def test_newthon_raphson1(self):
        x0 = 0.5
        max_iteraciones = 100
        margen_error = 0.01
        funcion = lambda x: 1 - x**2 - ma.atan(x)

        verificarConvergencia(funcion,x0,first_derivative(funcion,x0),second_derivative(funcion,x0))
        self.assertLess(abs(funcion(newton_raphson(funcion,x0,margen_error,max_iteraciones))),margen_error)
        print("\n**********************************************************")

    def test_newthon_raphson2(self):
        x0 = 1
        max_iteraciones = 100
        margen_error = 0.01
        funcion = lambda x: ma.cos(x) - x

        verificarConvergencia(funcion,x0,first_derivative(funcion,x0), second_derivative(funcion,x0))
        self.assertLess(abs(funcion(newton_raphson(funcion,x0,margen_error,max_iteraciones))),margen_error)


if __name__ == '__main__':
    unittest.main()
#Calculo Numerico
#Realizado por Jose Silva. CI: 30230054

#Importo tanto la libreria unittest para las pruebas como el archivo biseccion
import math as ma
import unittest
from biseccion import Biseccion
from newton_raphson import newton_raphson
from suma_rieman import Suma_Rieman
from trapecio import Trapecio

class Tests(unittest.TestCase):
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

    def test_newton_raphson1(self):
        x0 = 0.5
        max_iteraciones = 100
        margen_error = 0.01
        funcion = lambda x: 1 - x**2 - ma.atan(x)

        self.assertLess(abs(funcion(newton_raphson(funcion,x0,margen_error,max_iteraciones))),margen_error)
        print("\n**********************************************************")

    def test_newton_raphson2(self):
        x0 = 1
        max_iteraciones = 100
        margen_error = 0.01
        funcion = lambda x: ma.cos(x) - x

        self.assertLess(abs(funcion(newton_raphson(funcion,x0,margen_error,max_iteraciones))),margen_error)

    def test_suma_rieman(self):
        #Variables
        a, b, n = 0, 1, 10000
        funcion = lambda x: x**2
        self.assertLess(Suma_Rieman(funcion,a,b,n), 1)

    def test_trapecio(self):
        #Variables
        a, b, n = 1, 2, 100000
        funcion = lambda x: 3*x*ma.cos(x**2)

        self.assertLess(Trapecio(funcion,a,b,n), 2)


if __name__ == '__main__':
    unittest.main()
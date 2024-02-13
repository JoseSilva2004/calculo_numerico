import unittest
from suma_rieman import *

class TestSumaRieman(unittest.TestCase):
    def suma_rieman1(self):
        #Variables
        a, b, n = 0, 1, 10000
        funcion = lambda x: x**2
        self.assertLess(funcion(Suma_Rieman(funcion,a,b,n)), 1)

if __name__ == '__main__':
    unittest.main()
        

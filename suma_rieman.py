#Calculo Numerico
#Realizado Por: Jose Silva: 30230054

import math

def funcion(x):
    return x*math.sqrt(x**2 + 1)

#Aproximacion de integracion numerica por el metodo de la suma de rieman
def Suma_Rieman(fx,a,b,n):
    h = (b - a) / n
    return sum(fx(a + i * h) * h for i in range(n))

if __name__ == '__main__':
    print(Suma_Rieman(funcion, a = 0, b = 1, n = 10000))
    print("Hola")
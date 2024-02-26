#Calculo Numerico
#Realizado por: Jose Silva: 30230054

import math

def funcion(x):
    return 3*x*math.cos(x**2)

def Trapecio(fx,a, b, n):  
    h = (b - a) / n
    suma = 0
    
    for i in range(1 ,n):
        xi = a + i * h
        suma += fx(xi)
        trapecio = h * ((fx(a)) + (fx(b)) / 2 + suma)
        
    return trapecio

if __name__ == '__main__':
    a, b = 0, 1 #Intervalo inferior, intervalo superior
    n = 10000   #Numero de iteraciones

    resultado = Trapecio(funcion,a, b, n)
    print(resultado)
    

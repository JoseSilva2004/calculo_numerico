import math as ma
##Calculo Numerico
##Realizado Por: Jose Silva. CI:30230054

'''
    Implementacion del metodo de biseccion para encontrar
    la raíz de una función

'''
def Biseccion(fx, a, b, N, limite_iter = 100):
    
    #Aqui se verifica que fx(a) y fx(b) tengan signos opuestos
    if fx(a) * fx(b) >= 0:
        raise ValueError("La funcion debe tener signos opuestos en los extremos del intervalo.")

    #inicializar las variables
    c = (a + b) / 2
    error = abs(b - a)
    iteraciones = 0
    #iterar hasta que se alcanze la cantidad desea
    while error > N and iteraciones <= limite_iter:
        iteraciones += 1
        #Calcular el valor de la funcion en el punto medio
        fc = fx(c)

        #verifica si la raíz está en el subintervalo [a, c] o [c, b]
        if fc == 0:
            return c
        elif fc * fx(a) < 0:
            b = c
        else:
            a = c
        
        #calcular el nuevo punto medio y el error
        c_previo = c
        c = (a + b) / 2
        error = abs(c - c_previo)
    
    if iteraciones >= 100:
        print("Se ha excedido el numero maximo de iteraciones")
    else:
        return c

def funcion(x):
    return ma.exp(x) - 3*x**2

if __name__ == '__main__':
    raiz = Biseccion(funcion, 0, 1, 0.04)
    print(raiz)


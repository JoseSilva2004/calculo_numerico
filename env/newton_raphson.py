##Funcion para el metodo de newton-raphson
def derivada(funcion, x, h):
    #Esta funcion calcula la derivada de una funcion en un punto x
    #usando el método de las diferencias finitas, h es el tamaño del paso
    return (funcion(x + h) - funcion(x)) / h

def function(x):
    return x**2 + 2*x - 3

def calcular_derivadas(funcion, x, h=0.001):
    primera_derivada = (funcion(x + h) - funcion(x)) / h
    segunda_derivada = (funcion(x + 2 * h) - 2 * funcion(x + h) + funcion(x)) / (h ** 2)

    return primera_derivada, segunda_derivada

print(calcular_derivadas(function, 1))

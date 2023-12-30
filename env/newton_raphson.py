import math as ma
#Calculo Numerico
#Realizado por Jose Silva. CI: 30230054

def first_derivate(funcion, x, h=0.02): ##Calcular primera derivada
    primera_derivada = (funcion(x + h) - funcion(x)) / h   
    return primera_derivada

def second_derivate(funcion, x, h=0.02): ##Calcular segunda derivada
    segunda_derivada = (funcion(x + 2 * h) - 2 * funcion(x + h) + funcion(x)) / (h ** 2)
    return segunda_derivada

def function(x):
    return ma.exp(x) - 3*x**2   ##Defino la funcion


##Funcion para verificar si la funcion converge o no
def verificarConvergencia(funcion, primera_derivada, segunda_derivada) -> float:  ##Recibe como parametro la funcion, la primera y segunda derivada
    #Defino los intervalos y el punto medio
    a = 1
    b = 2
    x0 = a / b

    converge = funcion(x0) * segunda_derivada / pow(primera_derivada, 2)

    if (abs(converge) < 1): ##Si el resultado es menor que 1 es porque converge, de lo contrario hay que ir a la formula iterativa
        print(f"\nLa funcion convergera en el punto {x0}")
    else:
        print("El teorema de Newton-Raphson no decide")
    
    return abs(converge)

print(verificarConvergencia(function, first_derivate(function,0.5), second_derivate(function,0.5)))

# ##Funcion para el metodo de newton-raphson
def newton_raphson(x0, margen_error, max_iteraciones):
    iteracion = 0
    error_relativo = 1
    x = x0

    while error_relativo > margen_error and iteracion < max_iteraciones:
        x_nuevo = x - function(x) / first_derivate(function,x)
        error_relativo = abs(x_nuevo - x)
        x = x_nuevo
        iteracion += 1

    # Imprimir el resultado
    if iteracion == max_iteraciones:
        print("El método no converge después de", max_iteraciones, "iteraciones.")
    else:
        print("\nLa raíz es:", x, "después de", iteracion, "iteraciones.")
        return x

if __name__ == '__main__':
    # Definir el punto inicial, el margen de error y el número máximo de iteraciones
    x0 = 0.5
    margen_error = 0.002
    max_iteraciones = 100
    
    resultado = newton_raphson(x0, margen_error, max_iteraciones)
    comprobacion = function(resultado)
    print("\nEl resultado de la comprobacion es: ", abs(comprobacion))

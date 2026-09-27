""" 
EJERCICIO 1
Escribir una función que reciba como parámetros dos números enteros. 
Calcular y devolver el resultado de la multiplicación de ambos valores utilizando solamente sumas.
 Por ejemplo 4 * 3= 4 + 4 + 4



def multiplicacion(numero1, numero2):

    resultado = 0
    for i in range (numero2) :
        resultado = resultado 
    
    return resultado
"""


""" 

EJERCICIO 5
Desarrollar la función signo(n) que reciba un número entero y devuelva 1, -1 o 0 
según el valor recibido sea positivo, negativo o nulo. 


def signo(entero):
    if entero > 0:
        return 1
    elif entero < 0:
        return -1
    else:
        return 0
numero = int(input("Ingrese un número entero: "))
resultado = signo(numero)
print(f"El signo de {numero} es: {resultado}")
"""






""" 
Escribir la función comparar(a,b) que reciba como parámetros dos números enteros y devuelva 1 si el primero es mayor que el segundo,
 0 si son iguales o -1 si el primero es menor que el segundo. 
 En este ejercicio debe aprovecharse la función del ejercicio anterior.
   Ejemplo: comparar(4,2) devuelve 1, y comparar(2,4) devuelve -1.
""" 




def signo(entero):
    if entero > 0:
        return 1
    elif entero < 0:
        return -1
    else:
        return 0


def comparar(a, b):
    return signo(a - b)   
numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero:"))
resultado = comparar (numero1,numero2)
print( f"El resultado de comparar {numero1} y {numero2} es: {resultado}")
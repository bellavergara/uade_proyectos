# examen de Fundamentos de Informatica

"""
Ejercicio 1

Diseñar una función para mostrar un título filas de asteriscos, la longitud de la
fila de asteriscos y el texto del título se recibe como parámetro.
Ejemplo: título (“Ejercicio 1”, 15) muestra:
***************
Ejercicio 1
***************
Desarrollar un programa principal para mostrar el título: “Aprendiendo Funciones”, del ejercicio,
 agregando un título al iniciar el programa relacionado a lo que va a resolver el problema. 
"""

# la funcion toma como parametro 2 datos. 
# len ( me devuelve la cantidad de caracteres de ese string)


"""
def mostrar_titulo(texto, longitud):
    print("*" * longitud)
    print(texto)
    print("*" * longitud)


def programa_principal():
    mostrar_titulo("Aprendiendo Funciones", len("Aprendiendo Funciones"))
    texto = "Ejercicio 1 de examen "
    mostrar_titulo(texto, len(texto))


programa_principal()


"""

"""

Ejercicio 2
Una calculadora tiene cuatro operaciones básicas (a saber: sumar, restar, multiplicar, dividir). 
Desarrolle una función para realizar cada operación,
 que reciba como parámetros dos números ingresados por el usuario y devuelva el resultado de la operación.
   Resuelva la división por restas sucesivas (investigar cómo se resuelve).
 
Desarrollar un programa principal con un menú que permita realizar una operación y posea una opción para Salir. 
Luego de cada operación realizada se debe volver a presentar el menú. ingresado.
​​No se permite el uso de las siguientes estructuras de control:  
​​while True o break ocontinue  

"""

print (input(" Ingrese el primer numero, por favor:"))
print (input("Ingrese el segundo numero, por favor:"))

def sumar (numero1,numero2):
    return numero1 + numero2


def restar (numero1, numero2):
    return numero1 - numero2

def multiplicar (numero1, numero2):
    return numero1 * numero2


def dividir(numero1, numero2):
    if numero2 == 0:
        return "Error: no se puede dividir por 0"
    contador = 0
    resto = numero1
    while resto >= numero2:
        resto = resto - numero2
        contador += 1
    return contador 


def principal():
    opcion = 0
    while opcion != -1:
        print("Hola, seleccione la operación que quiere realizar:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("-1. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion != -1:
            numero1 = float(input("Ingrese el primer número, por favor: "))
            numero2 = float(input("Ingrese el segundo número, por favor: "))

            if opcion == 1:
                print(f"El resultado es: {sumar(numero1, numero2)}")
            elif opcion == 2:
                print(f"El resultado es: {restar(numero1, numero2)}")
            elif opcion == 3:
                print(f"El resultado es: {multiplicar(numero1, numero2)}")
            elif opcion == 4:
                print(f"El resultado es: {dividir(numero1, numero2)}")
            else:
                print("Opción inválida, intente de nuevo.")


principal()


























   


#clase 10
#1 EJERCICIO 1

import os
import random
"""
def limpiar_pantalla():
    # Si el sistema es Windows ('nt'), usa 'cls'. Si es Linux o Mac, usa 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')


def busquedaBinaria(lista,dato):
    # Esta función  realiza la búsqueda binaria de dato en la lista
    # definición de variables para la búsqueda
    izq = 0 
    der = len(lista) - 1
    pos = -1

    # bucle para realizar la búsqueda
    while izq <= der and pos == -1:
        centro = (izq+ der)// 2
        if lista[centro]== dato:
            pos = centro
        elif lista[centro]<dato:
            izq =centro + 1
        else: 
            der = centro -1

    return pos 


# programa para llamar a la función
limpiar_pantalla()

milista=[1,3,4,7,9,12,16,19,21,22]
dbusq = 0
ubic =0

print("Búsqueda dicotómica")
print(milista)
print()
dbusq = int(input("Dato a buscar?"))
print()

print("Presiona cualquier tecla para continuar...")
msvcrt.getch()  # Detiene la ejecución hasta una pulsación

limpiar_pantalla()

print()
print(milista)

ubic= busquedaBinaria(milista,dbusq)
print()
if ubic!= -1:
    print("El dato ", dbusq, "está en la posición: ", ubic)
else:
    print("El dato ", dbusq, "No existe en la lista.")

 """




""" 
1. Con la búsqueda binaria: escribir una función para devolver una lista con todas las posiciones que ocupa un valor pasado como parámetro, 
utilizando búsqueda secuencial en una lista desordenada. 
La función debe devolver una lista vacía si el elemento no se encuentra en la lista original. 
"""
#1. crear una lista
#2. solicitar al usuario un elemento a buscar en la lista
#3. En la función busquedaSecuencial(lista, dato): crear posiciones = [], recorrer toda la lista y, cada vez que lista[i] == dato, agregar i.
#4. Devolver posiciones (queda vacía si no hubo coincidencias).
#5. Mostrar el resultado.

""" 
def busquedaSecuencial(lista, dato):
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == dato:
            posiciones.append(i)
    return posiciones


lista_desordenada = [5, 3, 8, 1, 5, 7, 2, 5]
print ("Lista desordenada:", lista_desordenada)
valor_usuario = int(input(" Ingrese un valor para buscar en la lista: "))
resultado = busquedaSecuencial(lista_desordenada, valor_usuario)
print(f'Posiciones: {resultado}')

"""

""" 
2. Rellenar una lista con números enteros entre 0 y 100, obtenido al azar, y ordenar la lista.
Hacer un programa que pida un dato e indique si ese dato se encuentra o no en la lista generada.
Obtener el valor máximo de la lista. 
"""
#1. crear una lista con random.randint
#2. ordenar la lista / metodo burbujeo 
#3. solicitar al usuario un elemento a buscar en la lista
#4. aplicar la busqueda con todas las posiciones / te devuelve una lista con la posicion del elemento en la lista
#5. else: devolver una lista vacía si el elemento no se encuentra en la lista original
#6. obtener el valor máximo de la lista

"""
lista = [random.randint(0,100) for i in range(10)]
dato= int(input("Ingrese un dato a buscar en la lista:"))
if dato in lista:
    print(f"El dato {dato} se encuentra en la lista.")
else:
    print(f"El dato {dato} no se encuentra en la lista.")

print(f"El valor máximo de la lista es: {max(lista)}")
""" 


# EJERCICIO 3
""" 
Desarrollar un algoritmo que permita crear al azar 5 números pertenecientes a la lista A y otros
 5 números pertenecientes a la lista B.
 Crear una lista C, donde cada posición es el resultado de los elementos de B que se encuentran en A.
   La lista C debe estar ordenada. Ejemplo: se crea A=[10,2,23,45,52] y B=[45,2,12,10,23]   C=[2,10,23,45]
"""
# 1. crear lista A con ramdont
#2. crear lista B con random
#3. crear una lista C  
#4. recorrer la lista B y si el elemento de B está en A, agregarlo a C
#5. ordenar la lista C

listaA_ = [random.randint(0, 100) for i in range(5)]
listaB_ = [random.randint(0, 100) for i in range(5)]
listaC_ = []
for i in range(len(listaB_)):
    if listaB_[i] in listaA_:
        listaC_.append(listaB_[i])
listaC_.sort()
print(f"Lista A: {listaA_}")
print(f"Lista B: {listaB_}")
print(f"Lista C: {listaC_}")
 
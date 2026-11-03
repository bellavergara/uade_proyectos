
import os
import random

""" 
def limpiar_pantalla():
    # Si el sistema es Windows ('nt'), usa 'cls'. Si es Linux o Mac, usa 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')

def cargar_matriz(matrix,fil, cols):
    for f in range(fil):
        for c in range (cols):
            n = int(input("Ingrese un valor: "))
            matrix[f][c]= n

    return matrix



limpiar_pantalla()
filas = int(input("Cantidad de filas?:\n"))
columnas = int(input("Cantidad de columnas?:\n"))

matriz=[]

for f in range (filas):
    matriz.append([])
    for c in range(columnas):
        matriz[f].append(0)

cargar_matriz(matriz, filas, columnas)

for f in range(filas):
        for c in range (columnas):
            print(matriz[f][c], " ", end="")
            
        print()
"""
#CLASE 
#Ejercicio 1:
#Llenar una matriz con números del 1 al 9 (3*3).
""" 
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(0)
    return matriz

# Llenar una matriz con números del 1 al 9 (3*3).
def llenar_matriz(matriz, filas, columnas):
    numero = 1
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = numero
            numero += 1
    return matriz


limpiar_pantalla()
filas = 3
columnas = 3

matriz = crear_matriz(filas, columnas)
llenar_matriz(matriz, filas, columnas)

for f in range(filas):
    for c in range(columnas):
        print(matriz[f][c], " ", end="")
    print()

 """

""" 
2) EJERCICIO 2
Crear una matriz de 2x2 con números aleatorios entre 0 y 9.
 sume todos los elementos y muestre el resultado, con la leyenda “La suma de los elementos de la matriz es:” suma. 
"""
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def crear_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(0)
    return matriz



def llenarAleatorio(matriz,filas,columnas):
    for f in range(filas):
            for c in range(columnas):
                matriz[f][c] = random.randint(0, 9)
    return matriz

     
def sumaMatriz(matriz,fila, columna):
    suma = 0
    for f in range(fila):
            for c in range(columna):
                suma += matriz[f][c]

    return suma



limpiar_pantalla()
filas = 2
columnas = 2

matriz = crear_matriz(filas, columnas)
llenarAleatorio(matriz, filas, columnas)

for f in range(filas):
    for c in range(columnas):
        print(matriz[f][c], " ", end="")
    print()

suma = sumaMatriz(matriz, filas, columnas)
print("La suma de los elementos de la matriz es:", suma)



""" 
3) EJERCICIO 3
Multiplicar una matriz de 3x3 por un número y mostrar el resultado en una matriz resultante.
"""
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(0)
    return matriz


def llenarAleatorio(matriz,filas,columnas):
    for f in range(filas):
            for c in range(columnas):
                matriz[f][c] = random.randint(0, 9)
    return matriz


def matrizResultante(matriz, filas, columnas, numero):
    resultante = crear_matriz(filas, columnas)
    for f in range(filas):
        for c in range(columnas):
            resultante[f][c] = matriz[f][c] * numero
    return resultante


limpiar_pantalla()
filas = 3
columnas = 3

matriz = crear_matriz(filas, columnas)
llenarAleatorio(matriz, filas, columnas)

numero = int(input("Ingrese el número por el que multiplicar: "))
resultante = matrizResultante(matriz, filas, columnas, numero)

print("Matriz original:")

for f in range(filas):
    for c in range(columnas):
        print(matriz[f][c], " ", end="")
    print()

print("Matriz resultante:")
for f in range(filas):
    for c in range(columnas):
        print(resultante[f][c], " ", end="")
    print()
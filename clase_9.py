# Ejercicios clase 9

#EJEMPLOS DE CLASE/ METODO BORBUJEO
import os
import random 

""" def limpiar_pantalla():
    # Si el sistema es Windows ('nt'), usa 'cls'. Si es Linux o Mac, usa 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')


def metodoBurbujeo(lista):
    desordenada = True

    while desordenada:
        desordenada= False
        for i in range(len(lista)-1):
            if lista[i]>lista[i+1]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                desordenada=True

    return lista

def metodoInsercion(lista):

    for i in range(1,len(lista)): #Comienza con el 2do. elemento
        aux=lista[i]
        j=i
        while j>0 and lista[j-1]>aux:
            lista[j]=lista[j-1]
            j=j-1
        lista[j] = aux
    return lista


milista=[87,65,43,134,1,24,325]

print("Burbujeo")
print(milista)
print()
metodoBurbujeo(milista)
print(milista)

print("Presiona cualquier tecla para continuar...")
msvcrt.getch()  # Detiene la ejecución hasta una pulsación

limpiar_pantalla()

miotra=[98,335,3,5,324,35,1]
print("Inserción")
print(miotra)
print()
metodoInsercion(miotra)
print()
print(miotra)
"""
"""
Ejercicio 1:
Con la búsqueda binaria: escribir una función para devolver una lista con todas las posiciones que ocupa un valor
pasado como parámetro utilizando búsqueda secuencial en una lista desordenada.
La función debe devolver una lista vacía si el elemento no se encuentra en la lista original
 """

# 0 - crear una funcion para ordenar  una lista y  despues aplicar 
# 1 - crear una lista 
# 2 - ordenar la lista / metodo burbujeo 
# 3 - solicitar al usuario un elemento a buscar en la lista 
# 4 - aplicar la busqueda  con todas las posiciones  / te devuelve una lista con la posicioin del elemento en la lista 
# 5 - else: devolver una lista vacía si el elemento no se encuentra en la lista original


# ordenar la lista / metodo burbujeo 
def ordenar_lista_metodo_borbujeo(lista):
    desordenada = True

    while desordenada:
        desordenada = False

        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:

                aux = lista[i]
                lista[i] = lista[i+1]

                lista[i+1] = aux
                desordenada = True

    return lista


#4 y 5  aplicar la busqueda  con todas las posiciones  / te devuelve una lista con la posicioin del elemento en la lista 
def buscar_posiciones(lista, elemento):
    lista_posicion = []

    for i in range(len(lista)):
       if lista[i] == elemento:
           lista_posicion.append(i)

    if len(lista_posicion) > 0:
        print(f'El elemento {elemento} se encuentra en las posiciones: {lista_posicion}')
    else:
        print(f'El elemento {elemento} no se encuentra en la lista')
   
    return lista_posicion


# crear una lista vacia y llenarla con 10 elemento aleatorios en 1  y 100
lista = []
for i in range(10):
    lista.append(random.randint(1, 100))

print(f'Lista original: {lista}')
ordenar_lista_metodo_borbujeo(lista)
print(f'Lista ordenada: {lista}')

elemento = int(input("Ingrese el elemento que desea buscar en la lista: "))
buscar_posiciones(lista, elemento)


"""
Rellenar una lista con números enteros entre 0 y 100, obtenido al azar e imprimir el valor mínimo y el lugar que ocupa.
Tener en cuenta que el mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las posiciones en las que se encuentre.
La carga de datos termina cuando se obtenga un 0 como número al azar, el que no deberá cargarse en la lista.



def encontrar_posiciones(lista, elemento):
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == elemento:
            posiciones.append(i)
    return posiciones


#1 Rellenar una lista con números enteros entre 0 y 100
lista = []
while True:
    numero = random.randint(0, 100)
    if numero == 0:
        break
    lista.append(numero)

#2 Obtener el mínimo e imprimir el valor y el lugar que ocupa
if len(lista) > 0:
    minimo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]

    posiciones = encontrar_posiciones(lista, minimo)

    print(f'Lista generada: {lista}')
    print(f'El valor mínimo es {minimo} y se encuentra en las posiciones: {posiciones}')
else:
    print('La lista quedó vacía: el  número random fue 0')
"""

""" 
EJERCICIO 3
Desarrollar un algoritmo que permita crear al azar 5 números pertenecientes a la lista A y otros 5 números pertenecientes a la lista B.
Crear una lista C, donde cada posición es el resultado de la suma del número en la misma posición en la lista A con el número en la misma posición en la lista B.
Ejemplo: se crea A=[1,2,3,4,5] y B=[4,7,1,3,6]   C=[5,9,4,7,11]
"""
#Desarrollar un algoritmo que permita crear al azar 5 números pertenecientes a la lista A y otros 5 números pertenecientes a la lista B.
lista_A = []
lista_B = []

for i in range(5):
    lista_A.append(random.randint(1,10))
    lista_B.append(random.randint(1,10))


lista_C = []
for i in range(5):
    lista_C.append(lista_A[i]+ lista_B[i])

print(f'lista A :{lista_A}')
print(f'lista B :{lista_B}')
print(f'lista_C :{lista_C}')



""" 

EJERCICIO 4
Crear tres listas y ordenarlas en forma ascendente utilizando un método para cada lista:
métodos de selección, inserción y burbujeo. ¿Qué cambia para ordenar en forma descendente?
"""
# crear 3 listas
#ordernarlas en forma ascendente utilizando un método para cada lista:
#métodos de selección, inserción y burbujeo. ¿Qué cambia para ordenar en forma descendente?

lista_1 = []
lista_2 = []
lista_3=[]
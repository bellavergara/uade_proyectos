# EJEMPLOS DE CLASE
import random

def cargarLista(cantidad):
    lista=[]

    for i in range(cantidad):
        lista.append(random.randint(1,100))

    return lista



def imprimirlista(lista):

    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()


def busquedaSecuencial(lista,dato):

    i=0
    while i<len(lista) and lista[i]!=dato:
        i+=1

    if i<len(lista):
        return i
    else:
        return -1

def metodoSeleccion(lista):
    # Esta función ordena una lista por el método de Selección
    # Recibe como parámetro la lista a ordenar.
    
    largo=len(lista)   

    for i in range(largo-1):
        for j in range(i+1, largo):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 

# Programa Principal Ordenamiento de Lista

lista=[4,65,3,7,8,99,34,2]

print(lista)
print()

metodoSeleccion(lista)

print(lista)

#Programa principal
#cant =int (input("¿Cuantos elementos desea gargar?:"))

#milista = cargarLista(cant)

#imprimirlista(milista)

#n = int(input("Ingrese el número a buscar:"))
#pos = busquedaSecuencial(milista, n)

#if pos>= 0:
#    print("El elemnto ",n, " se encontró en la posición", pos)
#else:
#    print("El elemnto ",n, " NO se encontró en la lista")

    

# EJERCICIO 1 / CLASE 8
""" 
Cargar una lista, donde la cantidad de elementos se ingrese por consola, generando los elementos al azar entre 1 y 200,
 y luego imprimir la lista. Ingresar un elemento a buscar e informar la posición del elemento , y si no se encuentra, 
indicar que el elemento no se encuentra en la lista
"""
""" 

# EJERCICIO 2 / CLASE 8
Con la lista del ejercicio anterior, realizar un programa que la ordene utilizando el método 
de Selección. Imprimir la lista antes y después de ser ordenada.
"""


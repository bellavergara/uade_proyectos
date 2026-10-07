# Ejercicios clase 9
import os
import msvcrt

def limpiar_pantalla():
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
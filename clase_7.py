# para los vectores se utilizan listas for length ( recorre la cantifad de elemntos de esa lista)

# Ejercicio de practica. 
#parte 1


# parte 1:  funcion para imprimir lista

""" 
def imprimirlista(lista):
    largo = len(lista)
    for i in range(largo):
        print(lista[i], end= " ")
    


lista = []
n = int(input("Ingrese un numero o -1 para terminar el programa:"))

while n!= -1:
    lista.append(n)
    n = int(input("Ingrese un numero o -1 para terminar el programa :"))

# parte 2: calcular la cantidad de elemtnos
largolista = len(lista)
if largolista == 0 :
    print("No se ingresaron valores")
else: 
    mayor = lista[0]
    posicion = 0

    for i in range(largolista):
        if lista[i]> mayor:
            mayor = lista [i]
            posicion = i
            imprimirlista(lista)
    print ("El maximo de la lista es :", mayor, " y se encontro en la posicion : ",posicion) 

#Parte 3: eliminar el mayor
print ("Borrando el mayor que es", mayor)
del lista[posicion]
imprimirlista(lista)


"""

#EJERCICIO 1 /  CLASE 7
"""
Escribir una funcion para ingresar desde el teclado una serie de numeros entre A y B y guardarlos en una lista.
En caso de ingresar un valor fuera de rango, la funcion mostrara un mensaje de error y solicitara un nuevo numero.
Para finalizar la carga se debera ingresar -1. La funcion recibe como parametros los valores de A y B y devuelve la lista cargada
(o vacia, si el usuario no ingreso nada). Como valor de retorno. Tener en cuenta que A pyede ser mayor, menor o igual a B.
"""

def cargarlista(A, B):
    lista =[]
    n = int(input(f'Ingrese una serie de numeros entre {A} y {B}, para finalizar ingrese -1: '))
    while n!= -1:
        if (n >= A and n <= B) or (n <= A and n >= B):
          lista.append(n)
        else:
           print(f'Error! ingreso valores fuera del rango de {A} y/ o {B}')
        
        n = int(input(f'Ingrese nuevamente, una serie de numeros entre los rangos de A y B, para finalizar ingrese -1: '))

    return lista

#print(f'Lista cargada: {cargarlista(1, 5)}')
#print(f'Lista cargada: {cargarlista(9, 3)}')
#print(f'Lista cargada: {cargarlista(7, 7)}')

# Ejercicio 2 : calcular la suma de los numeros de la lista
def calcularsuma(lista):
    suma = 0 
    for i in range(len(lista)):
        suma += lista[i]
    
    return suma
"""
lista = cargarlista(1, 5)

print(f'La lista cargada es: {lista}')
print(f'La suma de los numeros de la lista es: {calcularsuma(lista)}')
"""

# Ejercicio 3: 
""" 
Determinar si la lista es capicúa(Palíndromo). Una lista capicúa se lee de igual modo de izquierda a
derecha y de derecha a izquierda. 
por ejemplo, [2,7,7,2]
es capicula, mientras que [2,7,5,2] no lo es. 
"""

def es_palindromo(lista):
    pass ## borrar esta linea

es_palindromo(cargarlista(1,5))


## 1,2,4,3,4,5 -> .pop() -> 1,2,4,3,4

## izquierda = 1,2,3,4,5
## derecha = []

## izquierda = 1,2,3,4
## derecha = 5

## izquierda = 1,2,3
## derecha = 5, 4

## izquierda = 1,2
## derecha = 5,4,3

## izquierda = 1
## derecha = 5,4,3,2

## izquierda = []
## derecha = 5,4,3,2,1

# Ejercicio 4 : 

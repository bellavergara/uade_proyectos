import os
import random 

"""
FUNCION n1  ***

1. Validación del código  10 puntos
Desarrolle una función que permita validar el código de un vehículo.
La función deberá verificar que:
El código sea un número comprendido entre 10000 y 99999.
El código no se encuentre repetido dentro de la matriz de vehículos.
La función deberá permitir determinar si el código ingresado puede ser utilizado.
"""
 #1. Crear la función validarCodigo, que recibe como parámetros: codigo y matriz_vehiculos
# 2. Crear una bandera "valido" y ponerla en True (se asume que el código es válido)
# 3. Verificar que el código esté entre 10000 y 99999; si no lo está, poner valido en False
# 4. Recorrer la matriz con un for; en cada fila comparar el código de la columna 0 con el código recibido
# 5. Si algún código de la matriz es igual al recibido, poner valido en False (está repetido)
# 6. Devolver valido (True si se puede usar, False si no)


def validarCodigo(codigo, matriz_vehiculos):
    valido = True

    if codigo < 10000 or codigo > 99999:
        valido = False

    for i in range(len(matriz_vehiculos)):
        if matriz_vehiculos[i][0] == codigo:
            valido = False

    return valido


""" 
Al iniciar el sistema, la empresa deberá indicar la cantidad de vehículos que desea administrar. 
Para cada vehículo se deberá ingresar toda la información necesaria. 
El código identificador deberá ser un número de cinco cifras, comprendido entre 10000 y 99999. 
No podrán existir dos vehículos con el mismo código. 
Tampoco se permitirá registrar dos vehículos con la misma combinación de marca y modelo. 
En caso de ingresar un dato inválido, deberá solicitarse nuevamente hasta que cumpla con las condiciones establecidas. 
Inicialmente, todos los vehículos deberán encontrarse disponibles y la cantidad de alquileres deberá comenzar en cero. 
"""

def validarModelo(matriz, modelo): 
    valido = True
    for i in range(len(matriz)):
        if matriz[i][1].lower() == modelo.lower():
            valido = False
    return valido
    


"""
FUNCION n2  ***
Carga de vehículos  15 puntos.
Desarrolle una función que permita cargar una cantidad determinada de vehículos dentro de una matriz.
Cada registro deberá almacenar:
Código.
Marca/modelo.
Precio diario.
Estado.
Cantidad de alquileres.
Día de alquiler.
Durante la carga deberán validarse los datos que correspondan.
Inicialmente:
El estado deberá ser "D".
La cantidad de alquileres deberá ser 0.
El día de alquiler deberá quedar inicializado de acuerdo con el diseño elegido.
No se permitirá registrar códigos repetidos ni vehículos con la misma marca y modelo.
"""

def limpiar_pantalla():
    # Si el sistema es Windows ('nt'), usa 'cls'. Si es Linux o Mac, usa 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')


def cargarVehiculos(matriz_vehiculos, cantidad):
    for i in range(cantidad):
        # CODIGO
        codigo = int(input("Ingrese el codigo del vehiculo: "))
        while validarCodigo(codigo, matriz_vehiculos) == False:
            print("Error! se ingreso un codigo invalido, vuelva a ingresarlo")
            codigo = int(input("Ingrese el codigo del vehiculo: "))

        # MARCA Y MODELO
        marca_modelo = input("Ingrese la marca y modelo del vehiculo: ")
        while validarModelo(matriz_vehiculos, marca_modelo) == False:
            print("Error! esa marca y modelo ya existe, vuelva a ingresarla")
            marca_modelo = input("Ingrese la marca y modelo del vehiculo: ")

        # PRECIO
        precio = int(input("Ingrese el precio del vehiculo: "))
        while precio <= 0:
            print("Error! se ingreso un precio invalido, vuelva a ingresar, por favor")
            precio = int(input("Ingrese el precio del vehiculo: "))

        # GUARDAR
        matriz_vehiculos.append([codigo, marca_modelo, precio, "D", 0, 0])


matriz_vehiculos = []
cargarVehiculos(matriz_vehiculos, 2)
print(matriz_vehiculos)

limpiar_pantalla()


"""
FUNCION n3  ***
Búsqueda de vehículo – 10 puntos
Desarrolle una función que permita localizar un vehículo utilizando su código identificador.
La función deberá implementar una búsqueda secuencial. Deberá permitir determinar:
Si el vehículo existe. En qué posición de la matriz se encuentra.
La función deberá retornar la información necesaria para que otras funciones puedan utilizar el resultado.
"""


def buscarVehiculo(matriz_vehiculos, codigo):
    pass


"""
FUNCION n4  ***
Alquiler de vehículo – 10 puntos
Desarrolle una función que permita registrar el alquiler de un vehículo. La función deberá contemplar:
- Validación de existencia.
- Control del estado del vehículo.
- Validación del día de alquiler.
- Actualización del estado.
- Registro del día de alquiler.
- Incremento de la cantidad de alquileres.
La función deberá evitar que se alquile un vehículo que actualmente se encuentre en estado "A".
"""


def alquiler_de_Vehiculos(matriz_vehiculos, codigo, dia):
    pass


"""
FUNCION n5  ***
5. Cálculo del importe de devolución  10 puntos
Desarrolle una función que reciba la información necesaria y determine el importe que deberá pagar el cliente.
Deberá aplicar las siguientes reglas:
Mismo día → importe $0.
Hasta 5 días → precio diario × cantidad de días.
Más de 5 días → los primeros 5 días se cobran normalmente y los días adicionales poseen un recargo del 30 %.
La función deberá retornar el importe calculado.
"""


def calculo_devolucion(precio_diario, dias):
    pass


"""
FUNCION n6  ***
6. Ordenamiento  5 puntos
Desarrolle una función que permita ordenar los vehículos según la cantidad de veces que fueron alquilados, de mayor a menor.
El algoritmo de ordenamiento deberá implementarse manualmente.
No podrá utilizar:
sort()
sorted()
Deberá utilizar alguno de los algoritmos de ordenamiento trabajados durante la cursada.
"""


def ordenar_vehiculos(matriz_vehiculos):
    pass
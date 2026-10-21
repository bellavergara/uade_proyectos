"""
FUNCION n1  ***

1. Validación del código  10 puntos
Desarrolle una función que permita validar el código de un vehículo.
La función deberá verificar que:
El código sea un número comprendido entre 10000 y 99999.
El código no se encuentre repetido dentro de la matriz de vehículos.
La función deberá permitir determinar si el código ingresado puede ser utilizado.
"""


# crear una funcion de validacion cuando el usuario ingresa el codigo
codigo_usuario = int(input("ingrese el codigo usario "))

def validar_modelo()
def validacion_codigo(codigo)

    
pass 
""" 
Al iniciar el sistema, la empresa deberá indicar la cantidad de vehículos que desea administrar. 
Para cada vehículo se deberá ingresar toda la información necesaria. 
El código identificador deberá ser un número de cinco cifras, comprendido entre 10000 y 99999. 
No podrán existir dos vehículos con el mismo código. 
Tampoco se permitirá registrar dos vehículos con la misma combinación de marca y modelo. 
En caso de ingresar un dato inválido, deberá solicitarse nuevamente hasta que cumpla con las condiciones establecidas. 
Inicialmente, todos los vehículos deberán encontrarse disponibles y la cantidad de alquileres deberá comenzar en cero. 

"""
def validarCodigo(codigo, matriz_vehiculos):
    pass



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


def cargarVehiculos(matriz_vehiculos, cantidad):
    pass


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
##========TPO: PARTE 1 = SISTEMA DE GESTIÓN DE ALQUILER DE VEHÍCULOS. 
import os

##=======Se crea una función que vaya limpiando la terminal por cada ejecución que realice.
def limpiar_pantalla():
    # Si el sistema es Windows ('nt'), usa 'cls'. Si es Linux o Mac, usa 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')
    
##=======PRIMERA FUNCIÓN (son dos separadas): VALIDACIÓN DEL CÓDIGO Y MODELO.
#Se crean dos funciones separadas para que realicen validaciones.

#==>Ésta función debe validar si el código ingresado no está repetido en la matriz y esta dentro del rango. 
#Devuelve True si el código es válido sino devuelve False en caso que sea inválido.
def validarCodigo(codigo, matriz_vehiculos):
    valido = True
    if codigo < 10000 or codigo > 99999:
        valido = False
    else:
        for i in range(len(matriz_vehiculos)):
            if matriz_vehiculos[i][0] == codigo:
                valido = False
    return valido

#Se le da valor True a la variable valido para que, si ingresa al Else porque respeta la primera restricción de estar 
#entre 10.000 y 99.999, realice la verificación si se repite o no. En caso que entre al If, entonces cambia a False.

#==>Ésta función debe validar que la marca/modelo ingresada no esté repetida dentro de la matriz.
def validarModelo(matriz, modelo): 
    valido = True
    for i in range(len(matriz)):
        if matriz[i][1].lower() == modelo.lower():
            valido = False
    return valido

#Se le da valor True a la variable valido para que, en caso de no encontrar repeticiones, devuelva la función True. 
#Con .lower() obligamos a cambiarlos todo a minúscula para que la comparación sea más certera porque sucedía que si escribiamos ToyotaCorola y toyotacorola lo tomaban como válido cuando en realidad son los mismo modelos y marca.

##SEGUNDA FUNCIÓN: CARGA DE VEHÍCULOS
#Esta función debe realizar la carga de vehículos en una lista matricial que contenga todos los datos necesarios.
#Debe recibir como parámetro la cantidad que quieren que contenga el registro de vehículos.
def cargarVehiculos(cantidad):
    matriz = []
    for i in range(cantidad):
        print(f'=====>>Registro del {i+1}° VEHÍCULO:')
        codigo_ingresado = int(input("Ingrese el código del vehículo a registrar (el rango comprende entre 10.000 a 99.999): "))
        while not validarCodigo(codigo_ingresado, matriz):
            print("Error!El código ingresado debe estar entre 10.000 y 99.999 y no puede repetirse! Intente nuevamente!")
            codigo_ingresado = int(input("Ingrese el código del vehículo a registrar (el rango comprende entre 10.000 a 99.999): "))
        marca_ingresado = input("Ingrese la marca y modelo juntos del vehículo a registrar sin espacios (Ej: ToyotaCorola): ")
        while not validarModelo(matriz, marca_ingresado):
            print("ERROR!Ha ingresado una marca y/o modelo que ya fue ingresado, no se puede repetir. Intente nuevamente!")
            marca_ingresado = input("Ingrese la marca y modelo juntos del vehículo a registrar sin espacios (Ej: ToyotaCorola): ")
        precio_alquiler = float(input("Ingrese el precio de alquiler del vehículo a registrar: "))
        while precio_alquiler <= 0:
            print("Error!Debe ingresar un valor mayor a cero. Intente nuevamente!")
            precio_alquiler = float(input("Ingrese el precio de alquiler del vehículo a registrar: "))
        matriz.append([codigo_ingresado,marca_ingresado,precio_alquiler,"D", 0,0])
        print(f'Se ha registrado con éxitos al vehículo n° {i+1}!')
        #[codigo, marca/modelo, precio, estado, cantidad alquileres, dia de alquiler]
    return matriz


#PROGRAMA PRINCIPAL

cantidad_registrar = int(input("Ingrese la cantidad de vehiculos que desea registrar en el sistemas: "))
while cantidad_registrar <= 0:
    print("Error!La cantidad debe ser igual o mayor a 1. Intente nuevamente!")
    cantidad_registrar = int(input("Ingrese la cantidad de vehiculos que desea registrar en el sistemas: "))

print(cargarVehiculos(cantidad_registrar))


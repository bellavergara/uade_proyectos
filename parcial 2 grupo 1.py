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



##=======TERCERA FUNCIÓN: BÚSQUEDA DE VEHÍCULO
#Esta función busca un vehículo por su código (búsqueda secuencial).
#Devuelve la posición (fila) de la matriz donde se encuentra, o -1 si no existe.

def buscarVehiculo(codigo, matriz_vehiculos):
    posicion = -1
    for i in range(len(matriz_vehiculos)):
        if matriz_vehiculos[i][0] == codigo:
            posicion = i
    return posicion



# FUNCION 4: alquiler_de_Vehiculos(matriz_vehiculos)

# 1. Crear la función alquiler_de_Vehiculos, que recibe: matriz_vehiculos
# 2. Pedir por teclado el código del vehículo que quiere alquilar el cliente
# 3. Buscar el vehículo con buscarVehiculo y guardar el resultado en "pos"
# 4. Si pos es -1: informar que el código no existe
# 5. Si no, si el estado (columna 3) es "A": informar que ya está alquilado
# 6. Si no (está disponible):
#    a. Pedir el día de alquiler
#    b. Mientras el día sea menor a 1 o mayor a 25: avisar el error y volver a pedirlo
#    c. Cambiar el estado a "A" (columna 3)
#    d. Guardar el día de alquiler (columna 5)
#    e. Sumar 1 a la cantidad de alquileres (columna 4)
#    f. Informar que el alquiler se registró



##=======CUARTA FUNCIÓN: ALQUILER DE VEHÍCULOS
#Esta función registra el alquiler de un vehículo disponible.
#Valida que el código exista, que el vehículo no esté alquilado y que el día esté entre 1 y 25.
def alquiler_de_Vehiculos(matriz_vehiculos):
    codigo = int(input("Ingrese el código del vehículo que desea alquilar: "))
    pos = buscarVehiculo(codigo, matriz_vehiculos)

    if pos == -1:
        print("Error! El código ingresado no existe.")
    elif matriz_vehiculos[pos][3] == "A":
        print("El vehículo se encuentra alquilado, no se puede realizar una nueva operación sobre él.")
    else:
        dia = int(input("Ingrese el día de alquiler (entre 1 y 25): "))
        while dia < 1 or dia > 25:
            print("Error! El día debe estar entre 1 y 25. Intente nuevamente!")
            dia = int(input("Ingrese el día de alquiler (entre 1 y 25): "))

        matriz_vehiculos[pos][3] = "A"
        matriz_vehiculos[pos][5] = dia
        matriz_vehiculos[pos][4] = matriz_vehiculos[pos][4] + 1
        print("Alquiler registrado con éxito!")





# FUNCION 5: calculo_devolucion(precio, dia_alquiler, dia_devolucion)

# 1. Crear la función calculo_devolucion, que recibe: precio (diario), dia_alquiler y dia_devolucion
# 2. Calcular los días utilizados: dias = dia_devolucion - dia_alquiler
# 3. Si dias es 0 (mismo día): el importe es 0
# 4. Si no, si dias es menor o igual a 5: importe = precio * dias
# 5. Si no (más de 5 días):
#    los primeros 5 días se cobran normal: precio * 5
#    los días extra (dias - 5) llevan 30% de recargo: (dias - 5) * precio * 1.30
#    importe = suma de ambos
# 6. Devolver el importe


##=======QUINTA FUNCIÓN: CÁLCULO DEL IMPORTE DE DEVOLUCIÓN
#Esta función calcula cuánto debe pagar el cliente según los días utilizados.
#Mismo día: $0. Hasta 5 días: precio x días. Más de 5 días: los días extra tienen 30% de recargo.

def calculo_devolucion(precio, dia_alquiler, dia_devolucion):
    dias = dia_devolucion - dia_alquiler

    if dias == 0:
        importe = 0
    elif dias <= 5:
        importe = precio * dias
    else:
        importe = precio * 5 + (dias - 5) * precio * 1.30

    return importe

print(calculo_devolucion(100, 10, 10))
print(calculo_devolucion(100, 10, 13))
print(calculo_devolucion(100, 10, 15))
print(calculo_devolucion(100, 10, 17))



# FUNCION 6: ordenar_vehiculos(matriz_vehiculos)

# 1. Crear la función ordenar_vehiculos, que recibe: matriz_vehiculos
# 2. Recorrer con for i desde la primera fila hasta la anteúltima
# 3. Suponer que la fila con mayor cantidad de alquileres es la i: pos_mayor = i
# 4. Recorrer con for j las filas que quedan después de i
# 5. Si la cantidad de alquileres (columna 4) de la fila j es mayor que la de pos_mayor,
#    guardar j en pos_mayor
# 6. Al terminar el for j, intercambiar la fila i con la fila pos_mayor
# 7. Al terminar el for i, la matriz queda ordenada de mayor a menor


##=======SEXTA FUNCIÓN: ORDENAMIENTO DE VEHÍCULOS
#Ordena la matriz de mayor a menor según la cantidad de veces alquilado (método de Selección).
def ordenar_vehiculos(matriz_vehiculos):
    for i in range(len(matriz_vehiculos) - 1):
        pos_mayor = i
        for j in range(i + 1, len(matriz_vehiculos)):
            if matriz_vehiculos[j][4] > matriz_vehiculos[pos_mayor][4]:
                pos_mayor = j
        aux = matriz_vehiculos[i]
        matriz_vehiculos[i] = matriz_vehiculos[pos_mayor]
        matriz_vehiculos[pos_mayor] = aux



# CIERRE DEL SISTEMA: cierre_sistema(matriz_vehiculos)

# 1. Crear la función cierre_sistema, que recibe: matriz_vehiculos
# 2. Llamar a ordenar_vehiculos para dejar la matriz de mayor a menor
# 3. Crear los contadores: total_alquileres, alquilados y disponibles, todos en 0
# 4. Recorrer la matriz con un for
# 5. En cada fila: según el estado sumar 1 a alquilados o a disponibles,
#    sumar la cantidad de alquileres al total e imprimir la línea del vehículo
# 6. Al terminar el for, imprimir los totales




##=======CIERRE DEL SISTEMA
#Muestra el informe final con los vehículos ordenados por cantidad de alquileres y un resumen.
def cierre_sistema(matriz_vehiculos):
    ordenar_vehiculos(matriz_vehiculos)

    total_alquileres = 0
    alquilados = 0
    disponibles = 0

    print("========== INFORME DE CIERRE DEL SISTEMA ==========")
    for i in range(len(matriz_vehiculos)):
        codigo = matriz_vehiculos[i][0]
        marca_modelo = matriz_vehiculos[i][1]
        estado = matriz_vehiculos[i][3]
        cantidad = matriz_vehiculos[i][4]

        if estado == "A":
            estado_texto = "Alquilado"
            alquilados = alquilados + 1
        else:
            estado_texto = "Disponible"
            disponibles = disponibles + 1

        print(f"{i+1}° | Código: {codigo} | {marca_modelo} | Alquileres: {cantidad} | Estado: {estado_texto}")
        total_alquileres = total_alquileres + cantidad

    print("----------------------------------------------------------")
    print(f"Total de alquileres realizados: {total_alquileres}")
    print(f"Vehículos alquilados actualmente: {alquilados}")
    print(f"Vehículos disponibles: {disponibles}")




#PROGRAMA PRINCIPAL

cantidad_registrar = int(input("Ingrese la cantidad de vehiculos que desea registrar en el sistemas: "))
while cantidad_registrar <= 0:
    print("Error!La cantidad debe ser igual o mayor a 1. Intente nuevamente!")
    cantidad_registrar = int(input("Ingrese la cantidad de vehiculos que desea registrar en el sistemas: "))

print(cargarVehiculos(cantidad_registrar))


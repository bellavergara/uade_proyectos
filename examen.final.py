##========TPO: PARTE 1 = SISTEMA DE GESTIÓN DE ALQUILER DE VEHÍCULOS.
import os

##=======Se crea una función que vaya limpiando la terminal por cada ejecución que realice.
def limpiar_pantalla():
    # Si el sistema es Windows ('nt'), usa 'cls'. Si es Linux o Mac, usa 'clear'.
    os.system('cls' if os.name == 'nt' else 'clear')

##=======Se crea una función que pausa el programa hasta que el usuario presione Enter.
#Sirve para que se alcance a leer el resultado de cada operación antes de limpiar la pantalla.
def presionarEnter(mensaje):
    input(mensaje)

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
#Debe recibir como parámetro la matriz donde se cargan los vehículos y la cantidad que quieren agregar al registro.
#Como recibe la matriz ya existente, los códigos y modelos nuevos se validan también contra los vehículos cargados anteriormente.
def cargarVehiculos(matriz, cantidad):
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
def buscarVehiculo(matriz, codigo):
    posicion = -1
    for i in range(len(matriz)):
        if matriz[i][0] == codigo:
            posicion = i
    return posicion


##CUARTA FUNCIÓN: ALQUILER DE VEHÍCULOS
#Permite registrar el alquiler de un vehículo. Devuelve True si se alquiló con éxito, sino devuelve False con su correspondiente mensaje.
#Se hace que devuelva True o False para que, al llamarlo en el programa principal, de acuerdo a lo que me devuelva pueda sumar los registros en un contador y después lo pueda mostrar en el cierre o consulta del sistema.
def alquilarVehiculo(matriz,codigo):
    alquilado = False
    busquedaCodigo = buscarVehiculo(matriz, codigo)
    if busquedaCodigo == -1:
        print(f'El vehículo con el código {codigo} no se encuentra registrado!')
    elif matriz[busquedaCodigo][3] == "A":
        print(f'El vehículo con el código {codigo} se encuentra actualmente ALQUILADO')
    else:
        dia_alquilar = int(input("Ingrese el día de alquiler del vehículo (debe ser entre 1 a 25 días): "))
        while dia_alquilar < 1 or dia_alquilar > 25:
            print("Error!Los días de alquiler debe comprenderse entre 1 a 25. Intente nuevamente!")
            dia_alquilar = int(input("Ingrese el día de alquiler del vehículo (debe ser entre 1 a 25 días): "))
        matriz[busquedaCodigo][5] = dia_alquilar
        matriz[busquedaCodigo][3] = "A"
        matriz[busquedaCodigo][4] += 1
        alquilado = True
        print(f'Se ha realizado el ALQUILER DEL VEHÍCULO con éxito:\nModelo/Marca: {matriz[busquedaCodigo][1]}\nCantidad de días a alquilar: {dia_alquilar}\nPrecio por día alquilado: {matriz[busquedaCodigo][2]}')
    return alquilado


##=======QUINTA FUNCIÓN: CÁLCULO DEL IMPORTE DE DEVOLUCIÓN
#Esta función calcula cuánto debe pagar el cliente según los días utilizados.
#Mismo día: $0. Hasta 5 días: precio x días. Más de 5 días: los días extra tienen 30% de recargo.
def calcularImporte(precio, dias):
    if dias == 0:
        importe = 0
    else:
        if dias <= 5:
            importe = precio * dias
        else:
            importe = (precio * 5) + ((dias - 5) * precio * 1.30)
    return importe

#==>Ésta función pide el día de devolución y valida que no sea anterior al día de alquiler ni mayor a 25.
def pedirDiaDevolucion(dia_alquiler):
    dia = int(input(f"Ingrese el día de devolución (entre {dia_alquiler} y 25): "))
    while dia < dia_alquiler or dia > 25:
        print(f"Error! El día de devolución debe estar entre {dia_alquiler} y 25. Intente nuevamente!")
        dia = int(input(f"Ingrese el día de devolución (entre {dia_alquiler} y 25): "))
    return dia

#==>Ésta función debe registrar la devolución de un vehículo a partir de su código.
#Devuelve el importe cobrado (0 si no se realizó la devolución) para poder acumular lo recaudado en el resumen final.

def devolverVehiculo(matriz_vehiculos):
    importe = 0
    codigo = int(input("Ingrese el código del vehículo a devolver: "))
    posicion = buscarVehiculo(matriz_vehiculos, codigo)

    if posicion == -1:
        print("El código ingresado no existe.")
    elif matriz_vehiculos[posicion][3] == "D":
        print("El vehículo no se encuentra alquilado, no hay nada que devolver.")
    else:
        dia_devolucion = pedirDiaDevolucion(matriz_vehiculos[posicion][5])
        dias = dia_devolucion - matriz_vehiculos[posicion][5]
        importe = calcularImporte(matriz_vehiculos[posicion][2], dias)
        print("Importe a pagar: $", importe)
        matriz_vehiculos[posicion][3] = "D"
        matriz_vehiculos[posicion][5] = 0
        print("Devolución registrada con éxito!")
    return importe

#Se usa buscarVehiculo para localizar el vehículo. Si devuelve -1 el código no existe, y si está en "D" no hay nada que devolver.
#Los días utilizados se calculan restando el día de alquiler (columna 5) al día de devolución.
#El importe se obtiene llamando a calcularImporte con el precio diario (columna 2) y los días utilizados.
#Al finalizar, el vehículo vuelve a estado "D" y el día de alquiler a 0. El día se reinicia después de calcular los días para no perder el dato.
#La cantidad de alquileres (columna 4) no se modifica, porque debe conservar lo acumulado.


##SEXTA FUNCIÓN: ORDENAMIENTO DE LA MATRIZ DE REGISTRO
#Ordena la matriz de mayor a menor según la cantidad de veces que fue alquilado cada vehículo (método de Selección).
def ordenarVehiculos(matriz):
    for i in range(len(matriz) - 1):
        pos_mayor = i
        for j in range(i + 1, len(matriz)):
            if matriz[j][4] > matriz[pos_mayor][4]:
                pos_mayor = j
        aux = matriz[i]
        matriz[i] = matriz[pos_mayor]
        matriz[pos_mayor] = aux

##SEPTIMA FUNCIÓN: CONSULTA DE INFORMACIÓN
#Las consultas pasaron a ser opciones del menú principal, así que cada una es una función separada, con lo que se muestra en cada opción.

#==>Muestra los vehículos que están disponibles.
def mostrarDisponibles(matriz):
    print(">>>>>VEHÍCULOS DISPONIBLES")
    cantidad = 0
    for i in range(len(matriz)):
        if matriz[i][3] == "D":
            cantidad += 1
            print(f'Código: {matriz[i][0]}//Marca: {matriz[i][1]}//Precio por día alquilado: ${matriz[i][2]}//Cantidad de veces alquilada: {matriz[i][4]}')
    if cantidad != 0:
        print(f'Hay unos {cantidad} vehículos disponibles para elegir')
    else:
        print("No hay vehículos disponibles en estos momentos!")

#==>Muestra los vehículos que están alquilados actualmente.
def mostrarAlquilados(matriz):
    print(">>>>>VEHÍCULOS ACTUALMENTE ALQUILADOS")
    cantidad = 0
    for i in range(len(matriz)):
        if matriz[i][3] == "A":
            cantidad += 1
            print(f'Código: {matriz[i][0]}//Marca: {matriz[i][1]}')
    if cantidad != 0:
        print(f'Hay {cantidad} vehículos que estan actualmente alquilados')
    else:
        print("No hay vehículos alquilados en estos momentos!")

#==>Muestra cuántas veces fue alquilado cada vehículo.
def mostrarCantidadAlquileres(matriz):
    print(">>>>>CANTIDAD DE VECES QUE LOS VEHÍCULOS FUERON ALQUILADOS")
    for i in range(len(matriz)):
        print(f'**Vehículo n°{i+1}:\nCódigo vehículo: {matriz[i][0]}//Modelo:  {matriz[i][1]}//Cantidad de veces alquilado:  {matriz[i][4]} ')

#==>Muestra toda la información de los vehículos registrados.
def mostrarInformacionGeneral(matriz):
    print(">>>>>INFORMACIÓN GENERAL DE LOS VEHÍCULOS REGISTRADOS")
    for i in range(len(matriz)):
        print(f'Vehículo n° {i+1}:\nCódigo: {matriz[i][0]}//Marca: {matriz[i][1]}//Precio por día alquilado: ${matriz[i][2]}//Estado: {matriz[i][3]}//Cantidad de veces alquilada: {matriz[i][4]}')


##OCTAVA FUNCIÓN: CIERRE DEL SISTEMA
#Muestra el informe final con los vehículos ordenados por cantidad de alquileres y un resumen.
def cierre_sistema(matriz_vehiculos):
    ordenarVehiculos(matriz_vehiculos)

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

##=======MENÚ PRINCIPAL (único menú del sistema)
#==>Ésta función debe mostrar el menú principal y llamar a la operación elegida.
#Devuelve el total recaudado por las devoluciones realizadas.
def menuPrincipal(matriz_vehiculos):
    total_recaudado = 0
    opcion = -1
    while opcion != 0:
        limpiar_pantalla()
        print("=====>> MENÚ PRINCIPAL:")
        print("1. Cargar vehículos")
        print("2. Alquilar un vehículo")
        print("3. Devolver un vehículo")
        print("4. Consultar vehículos disponibles")
        print("5. Consultar vehículos actualmente alquilados")
        print("6. Consultar cantidad de veces que los vehículos fueron alquilados")
        print("7. Consultar información general de los vehículos registrados")
        print("0. Cerrar el sistema")
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            cantidad_registrar = int(input("Ingrese la cantidad de vehiculos que desea registrar en el sistemas: "))
            while cantidad_registrar <= 0:
                print("Error!La cantidad debe ser igual o mayor a 1. Intente nuevamente!")
                cantidad_registrar = int(input("Ingrese la cantidad de vehiculos que desea registrar en el sistemas: "))
            cargarVehiculos(matriz_vehiculos, cantidad_registrar)
        elif opcion == 2:
            codigo = int(input("Ingrese el código del vehículo a alquilar: "))
            alquilarVehiculo(matriz_vehiculos, codigo)
        elif opcion == 3:
            total_recaudado = total_recaudado + devolverVehiculo(matriz_vehiculos)
        elif opcion == 4:
            mostrarDisponibles(matriz_vehiculos)
        elif opcion == 5:
            mostrarAlquilados(matriz_vehiculos)
        elif opcion == 6:
            mostrarCantidadAlquileres(matriz_vehiculos)
        elif opcion == 7:
            mostrarInformacionGeneral(matriz_vehiculos)
        elif opcion != 0:
            print("Opción inválida. Intente nuevamente!")
        if opcion != 0:
            presionarEnter("\nPresione Enter para volver al menú principal...")
    return total_recaudado

#El total recaudado se acumula dentro del menú con lo que devuelve devolverVehiculo, así no es una variable global.
#El menú se repite hasta que se elija 0 (cerrar el sistema), sin usar while True ni break.
#Después de cada operación se espera un Enter y se limpia la pantalla para volver a mostrar el menú.


##=======FUNCIÓN DE INICIO
#Abre el menú principal (donde se cargan los vehículos) y al salir muestra el informe de cierre.
def iniciarSistema():
    matrizRegistro = []
    total_recaudado = menuPrincipal(matrizRegistro)
    limpiar_pantalla()
    cierre_sistema(matrizRegistro)
    print(f"Total recaudado por devoluciones: ${total_recaudado}")
    presionarEnter("\nPresione Enter para cerrar el sistema...")


iniciarSistema()
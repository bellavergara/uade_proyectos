# Ejercicios de clase 4
# Ejercicio de clase.
#contador_numero  = int(input("Ingrese un numero distinto de 0 pero entero "))
#suma = 0 
#promedio = 0


"""
Ejercico 1
 #Primer y Último Valor: Ingresar números por teclado. Mostrar el 
#primer y el  último valor ingresado. Finalizar
#con -1.
"""
""" 
primero = 0
ultimo = 0

numero = int(input("Ingrese un numero- finalice c/ -1: "))
if numero != -1 :
    primero = numero

while numero != -1 : 
    numero = int(input("Ingrese un numero- finalice c/ -1: "))
    if numero != -1 :
        ultimo = numero

print (f'El primer numero ingresado es:{primero}')
print (f'El ultimo numero ingresado es:{ultimo}')

""" 

# Ejercicio 1 
""" 
primer_numero = 0
ultimo_numero = 0
primera_vez = True



num_usuario =  int(input("Ingrese un numero- finalice c/ -1: "))
while (num_usuario != -1):
    if primera_vez == True :
        primer_numero = num_usuario
        primera_vez = False
    else :
        ultimo_numero = num_usuario

    num_usuario =  int(input("Ingrese un numero- finalice c/ -1: "))

print (f'El primer numero ingresado es:{primer_numero}')
print (f'El ultimo numero ingresado es:{ultimo_numero}')
""" 


""" 
6) Tabla de Multiplicar del 4 (y del usuario):
Mostrar la tabla de multiplicar (del 1 al 12) del número 4.
 ¿Cómo adaptaría el algoritmo para que el usuario elija qué tabla mostrar?
"""

""" 
tabla_usuario = int(input("Ingrese el numero que desea para mostra la tabla: "))

for i in range (1, 13) :
   resultado = tabla_usuario * i 
   print(f'{tabla_usuario}x{i} = {resultado}')
   """ 

""" Suma Par Acotada:Ingresar números enteros hasta que la sumatoria de los números pares ingresados supere 100.
Informar cuántos números totales se ingresaron.



suma = 0
contador = 0 
while suma <= 100 : 
    numero_usuario = int(input("Ingrese numeros enteros:"))
    contador += 1
    if numero_usuario %2 == 0 :
       suma =  suma + numero_usuario 

print(f'la cantidad de numeros ingresados son: {contador}')
print (f'la suma de los numeros pares es: {suma}')
        
"""

"""
10) Factorial de N:Calcular el factorial de un número dado N.
 Se deben rechazar e informar entradas inválidas (números menores que 0).
"""


# Factorial de n => n*(n-1) para todo n>0
"""  
factorial = 1
num_usuario = int(input("Ingrese un numero positivo: "))
if num_usuario < 0 :
     print ("El numero ingresado es invalido")
else:
    while num_usuario > 0 :
        factorial = num_usuario * factorial
        num_usuario = num_usuario - 1

    print(f'El factorial del numero ingresado es: {factorial}')

 """
"""
12) Sucesión de Fibonacci:Leer N e imprimir los primeros N términos de la Sucesión de Fibonacci 
(0, 1, 1, 2, 3, 5, 8...), como así también informar su sumatoria total

"""

num_fibo1 = 0
num_fibo2 = 1
sumaTotal = 0 

num_usuario = int(input("Ingrese un numero positivo :"))
if  num_usuario >= 0 :
    while num_usuario > 0:
        sumaTotal = num_fibo1 + sumaTotal
        print(num_fibo1)

        auxiliar = num_fibo1 + num_fibo2 
        num_fibo1 = num_fibo2
        num_fibo2 = auxiliar

        num_usuario = num_usuario -1 

    print (f'la suma total es:{sumaTotal}')
else : 
    print("Error, debe ingresar un numero positivo")
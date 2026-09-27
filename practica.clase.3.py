#Ejercicio1

numero_usuario = int(input("ingrese un numero entero, por favor:"))
numero_entero = 5


if numero_usuario > numero_entero :
    print (numero_usuario)
else:
    print("El numero que ingreso es menor a 5")

# ejercicio 2

#1Escribir un programa que solicite al usuario ingresar la calificacion numerica de un estudiante 
#numero entero entre 0 y 100
#2. El programa debe imprimir un mensaje que indique la calificacion coorrespondinete segun:
# Entre 90 y 100 A-EXcelente ""
# Entre 80 y 89 "B - muy bueno""
#Entre 70 y 79 "C-Aprobado"
#entre 60 y 69 "D- pasable""
#menor que 60" F"-No aprobado"


nota_usuario = int(("Ingrese su calificacio, por favor entre 0 y 100:"));
calificacion_A = "Calificacion Excelente"
calificacion_B = "Muy bueno"
calificacion_C = "Aprobado"
calificacion_D = "Pasable"
calificacion_F = "No aprobado"

if nota_usuario >= 90 and nota_usuario<= 100 :
    print (calificacion_A)
elif nota_usuario >= 80 and nota_usuario<= 89 :
    print (calificacion_B)

elif nota_usuario >= 70 and nota_usuario<= 79:
    print (calificacion_C)
elif nota_usuario >= 60 and nota_usuario<= 69:
        print (calificacion_D)

else :
     print (calificacion_F)

    
#Ingresar 2 números enteros e indicar si son iguales o distintos.
numero_entero_1 = int(input("ingrese el primer numero entero"))
numero_entero_2 = int (input("ingrese el segundo numero entero"))
if numero_entero_1 == numero_entero :
        print ("Ambos numeros ingresados son iguales")

else:
     print ("Los numeros ingresados son distintos entre si")


# Ingresar un número entero e imprimir un mensaje indicando si es par o impar

numero_usuario = int(input("Ingrese un numero entero :"))
numeroPar = 0
numeroInpar = 0
if numero_usuario == numeroPar :
     print ("El numero ingresado es un numero par")
else:
     print ("El numero ingresado es un numero inpar")
    

#3) Desarrollar un programa que solicite un número de mes 
# y escriba el nombre del mes en letras (ej: 11 “Noviembre”).
#  Se debe verificar que sea un número de mes válido, mostrando el error y solicitando 
#nuevamente el ingreso.

mesUsuario = int(input("Ingrese un numero del mes (del 1 al 12)"));
while mesUsuario < 1 or mesUsuario > 12:
     mesUsuario = int (input("Numero invalido,Ingrese un numero valido(del 1 al 12)"));
if mesUsuario > 1 :
    print ("El mes ingresado es Enero")
elif mesUsuario == 2 :
     print ("El mes ingresado es Febrero")
elif mesUsuario == 3:
        print ("El mes ingresado es Marzo")
elif mesUsuario == 4:
    print ("El mes ingresado es Abril")
elif mesUsuario == 5:
     print("El mes ingresado es Mayo")
elif mesUsuario  == 6 :
    print ("El mes ingresado es Junio")
elif mesUsuario  == 7 :
    print ("El mes ingresado es Julio")
elif mesUsuario  == 8 :
    print ("El mes ingresado es Agosto")

elif mesUsuario  == 9 :
    print ("El mes ingresado es Septiembre")

elif mesUsuario  == 10 :
    print ("El mes ingresado es Octubre")

elif mesUsuario  == 11 :
    print ("El mes ingresado es Noviembre")

elif mesUsuario  == 12 :
    print ("El mes ingresado es Diciembre")
    




#4 En el congreso se vota una ley. Desarrollar un programa que 
#permita ingresar la cantidad de votos a favor y la cantidad en contra,
#  e informar el porcentaje obtenido en cada caso, y si la misma fue aprobada o no


votoUsuario = int(input("Ingrese su voto: Positivo o negativo"));

votosPositivos = 0 
VotosNegativos = 0
sumaDeVotosPositivos = 0 
sumadeVotosNegativos = 0

#Practica para examen 
# ejercicio + Pseint + Diagrama de flujo + preguntas teoricas
""" 
ingresar un numero positivo. rechazar el numero y volverlo a ingresar
en caso de ser negativo. Luego se solicita imprimir un mensaje indicando si ducho numero
es oblondo o no . Se dice que un numero es oblongo cuando se obtiene como resultado de multiplicar
dos numeros enteros consecutivos.
"""
"""
ejemplos:
2 es oblongo por que resulta de multiplicar 1 * 2 
6 es oblongo por que resulta de multiplicar 2 * 3
20 es oblongo por que resulta de multiplicar 4 * 5
24 no es oblongo por que ningun producto de 2 enteros consecutivos da 24. 
"""

num_usuario = int(input("Ingrese un numero positivo, por favor:"))
while  num_usuario <= 0 :
    print ("Error! el numero ingresado debe ser un numero positivo")
    num_usuario = int(input("Ingrese un numero positivo, por favor:"))


a = 1
b= 2
oblongo = (a * b)
#if num_usuario < oblongo


"""
ejercicio 2 
Un pastelero sabe que cada chocotorta requiere 500 gramos de galletitas de chocolates,
400 gramos de dulce de leche y 180 gramos de queso crema. Desarrollar un programa
para leer la cantidad de kilos en cada ingrediente e informar cuantas chocotortas
se pueden preparar y cuntas sobran de cada ingrediente
 """

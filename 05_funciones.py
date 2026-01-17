
import os 
def funcion1():
    print("esta es la funcion 1")

def funcion2():
   os.system("cls")

def funcion3():
    print("esta es la funcion 2")

def main():
    funcion1()
    funcion2()
    funcion3()  

if __name__ == "__main__":
    main()


#con esto se controla lo que se quiere ejecutar 

"""PRACTICA 2 
Crear un programa que permita realizar la soperaciones basicas +, -, *, /
utilizando un funciones para cada funcion y un menu principal para desplegar 
y elegir que operacion reutilizaremos """

import os

def funcionSumar():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print("Resultado:", a + b)

def funcionRestar():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print("Resultado:", a - b)

def funcionMultiplicar():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    print("Resultado:", a * b)

def funcionDividir():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("No se puede dividir entre cero")

def main():
    print("MENU")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        funcionSumar()
    elif opcion == "2":
        funcionRestar()
    elif opcion == "3":
        funcionMultiplicar()
    elif opcion == "4":
        funcionDividir()
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

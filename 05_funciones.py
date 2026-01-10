
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

def funcionSumar():
    print ("1.sumar")

def main():
    funcionSumar()

def funcionRestar():
    print ("2.restar")

def funcionMultiplicar():
    print ("3.multiplicar")

def funcionDividir():
    print ("4.dividir")

    def main():
        funcionSumar()
        funcionRestar()
        funcionMultiplicar()
        funcionDividir()

if __name__ == "__main__":
    main( )
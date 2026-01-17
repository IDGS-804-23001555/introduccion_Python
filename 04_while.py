x=0
tem=""
while x<10:
    tem=tem+str(x)+"+"
    x=x+2
print("la suma de los numeros pares menores a 10 es: ")
print (tem)


#PRACTICA 1 
""" operaciond de multiplicacion de a x b utilizando sumas
a=3
b=4
salida: 3+3+3+3+12"""

a = 3
b = 4

resultado = 0
i = 0

while i < b:
    resultado = resultado + a
    print(a, end="")
    
    if i < b - 1:
        print("+", end="")
    
    i = i + 1

print("=", resultado)
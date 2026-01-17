"""listas es parecio cuando se trbaja en arreglos con java
una lista es una secuencia de elementos, se crea con [] """

lista = ["Dario", 33, 9,5,true, "German", 20, 8]

print (lista)
print (lista [:])
print(lista[2])
print(lista[-1])
print(lista[0:3])
print(lista[3:])


lista1.append("Vargas")
print(lista1)

lista1.insert([2, "nadia"])
print(lista1)

lista1.extend(["uno", 1.1, false])
print(lista1)

lista1.remove(33)
print(lista1)
lista1.pop(0)
print(lista1)   

lista2=["tres,cuatro"]
lista3=lista1+lista2
print(lista3)   

print (lista2*4)
lista4=[1,2,3,4]
lista4.sort ()
print(lista4)   
"""Las tuplas son inmutadas se declaran con ( )"""

tupla=("uno","dos","tres")
print(tupla)

tuplasVariosDatos=(12,true,23.5, "el gato", 12+4j)
print(tuplasVariosDatos)

tuplasConTuplas=(1,2,3,4,(1,2,3))
print(tuplasConTuplas)

print(tuplasConTuplas[3])
print(tuplasConTuplas[-2])
print(tuplasConTuplas[0,2])

a,b,c = tupla
print(a,b,c)

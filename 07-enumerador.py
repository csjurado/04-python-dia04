lista = ['a','b','c']
indice = 0
for item in lista:
    print(indice,item)
    indice += 1
print('-------------------------------------------OTRA FORMA -------------------------------------------')
for indice,item in enumerate(lista):
    print(indice ,item)
print('-------------------------------------------OTRA FORMA -------------------------------------------')
for item in enumerate(lista):
    print(item)
print('-------------------------------------------OTRA FORMA -------------------------------------------')
#Transformar una lista a tuples
mis_tuples = list(enumerate(lista))
print(mis_tuples)
print(mis_tuples[1][0])
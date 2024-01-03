lista = ['a','b','c']
for letra in lista:
    numero_letra = lista.index(letra) +1
    print(f"{numero_letra} Letra : {letra}")
#--------------------------------------------------------------------------------------------------------------
lista1 = ['Pablo', 'Laura', 'Fede', 'Carlos','Julia']
for nombre in lista1:
    if nombre.startswith('L'):
        print(f"El nombre empieza con 'L' y es {nombre}")
    else:
        print(f'Nombre que no comienza con "L" es {nombre}')
#--------------------------------------------------------------------------------------------------------------
numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

#--------------------------------------------------------------------------------------------------------------

for num in [[1,2],[3,4],[5,6], 7]:
    print(num)

#--------------------------------------------------------------------------------------------------------------

dic = { 'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item in dic:
# for item in dic.values():
    print(item)

#--------------------------------------------------------------------------------------------------------------
for a,b in dic.items():
# for item in dic.values():
    print(a,b)

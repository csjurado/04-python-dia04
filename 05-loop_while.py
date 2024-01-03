monedas = 5
while(monedas > 0):
    print(f"Te quedan {monedas}")
    monedas -=1

else:
    print("No tengo mas monedas")

#------------------------------------------------------------------------------------------------------------------------
respuesta = 's'
while (respuesta == 's'):
    respuesta = input('quieres seguir ? (s/n) : \n')
else:
    print('Gracias')

#------------------------------------------------------------------------------------------------------------------------
nombre = input(' Tu nombre es : ')
for letra in nombre:
    if letra == 'r':
        break
    print(letra)
#------------------------------------------------------------------------------------------------------------------------
nombre = input(' Tu nombre es : ')
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)
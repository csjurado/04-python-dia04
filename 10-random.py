# 1er Metodo
from  random import *
aleatorio = randint(1, 50)
print(aleatorio)

# 2do Metodo
#Un valor decimal
aleatorio1 = uniform(1,5)
aleatorio1 = round(aleatorio1,5)
print(aleatorio1)

# 3er metodo
# Numero decinal aleatorio entre 0 y 1
aleatorio2 = random()
print(aleatorio2)

# 4to metodo
colores = ['azul','rojo', 'blanco','negro','amarillo','plomo']
print(choice(colores))

# 5 to Metodo
numeros = list(range(5,50,5))
print(numeros)
shuffle(numeros)
print(numeros)
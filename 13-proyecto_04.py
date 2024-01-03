from  random import *
print("Bienvenido al juego del numero secreto")
nombre = input("Ingresa tu nombre : ")
intentos = 8
num_ale = randint(1, 100)
print(num_ale)
while(intentos >= 1):
    print(f"He pensado un numero entre el 1 y el 100 y tienes {intentos} intentos  para divinar")
    num_1 = int (input(f"{nombre} ingresa cual crees que es el numero : "))
    if (num_1 > 100 or num_1 < 0):
        print(f"Error el {num_1} debe estar entre 0 y 100")
        intentos -= 1
    elif (num_1 > num_ale):
        print(" El numero que escogiste es MAYOR al numero pensado")
        intentos -= 1
    elif (num_1 < num_ale):
        print(" El numero que escogiste es MENOR al numero pensado")
        intentos -= 1
    elif (num_1 == num_ale):
        print(f"Perfecto has acertado el numero es {num_ale}")
        intentos = 0
else:
    print("No tienes mas intentos ")


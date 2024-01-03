x = True
y = False
if y:
    print('Es correcto')
else:
    print('Es falso')
#--------------------------------------------------------------------------------------------------------------
mascota = 'perro'
if mascota == 'gato':
    print('Tienes un gato')
elif (mascota== 'pez'):
    print('Tienes un pez')
elif (mascota == 'perro'):
    print('Tienes un perro')
else:
    print('No se que animal tienes')

#--------------------------------------------------------------------------------------------------------------
edad = 16
calificacion = 9
if edad < 18:
    print('Eres menor de edad')
    if calificacion >=7:
        print('Estas aprobado')
    else:
        print('Estas reprobado')
else:
    print('Eres mayor de edad')
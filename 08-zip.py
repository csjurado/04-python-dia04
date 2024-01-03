nombres = ['Carlos','Santiago','Gabriela']
edades = [12,77,55]
ciudades = ['Lima','Madrid','Mexico']

combinados = list(zip(nombres,edades,ciudades))
# print(combinados)
for nombres,edades,ciudades in combinados:
    print(f"{nombres} tiene {edades} anios y vive en {ciudades}")
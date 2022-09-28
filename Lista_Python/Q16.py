#Implemente um código que apresente a quantidade de números ímpares na seguinte lista definida: numeros = [13, 20, 55, 60, 70, 7, 14, 33].

contador = 0
numeros = (13, 20, 55, 60, 70, 7, 14, 33)
for numero in numeros:
    if numero %2 == 0:
        contador = contador+1
print('A quantidade de números impares é: {}'.format(contador))
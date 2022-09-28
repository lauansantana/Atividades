#Questao 7
'''Faça um  algoritmo  que  leia  um nº inteiro  e mostre  uma  mensagem  indicando  se este número é par ou ímpar, e se é positivo ou negativo.'''


numero = int(input('Informe um número: \n'))

if numero%2==0 and numero>=0:
    print('Número par positivo.')

if numero%2==0 and numero<0:
    print('Número par negativo.')

if numero%2==1 and numero>=0:
    print('Número ímpar positivo.')

if numero%2==1 and numero<0:
    print('Número ímpar negativo.')
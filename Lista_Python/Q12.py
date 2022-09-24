#Questao 12
#Faça um programa que recebe 10 númerose que calcule e mostre a quantidade dos números entre 30e 90.

n = 0
for numeros in range(0,10):
    numero = int(input('Informe um número: '))
    if numero >=30 and numero <=90:
        n = n+1
print('A quantidade de números entre 30 e 90 sao: ', n)

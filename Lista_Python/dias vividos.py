#Questao 4
'''Faça um algoritmo que leia a idade de uma pessoa expressa em anos e mostre-a expressa em dias e também em horas.
-Exemplo:
Usuário informa Idade=20 Programa imprime: Você já viveu 7300 dias. Isso significa 175200 horas.'''


idade = int(input('Informe a sua idade: '))
dias = idade*365
horas = dias*24

print('Você já viveu {} dias. Isso significa {} horas.'.format(dias, horas))
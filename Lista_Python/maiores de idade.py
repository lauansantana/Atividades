#Questao 9
#Faça  um  programa  que  leia  a  idade  de  10  pessoas  e  informe  quantas  pessoas são maiores de idade.

maior = 0
for idades in range(0,10):
    idade = int(input('Informe a idade: '))
    if idade >=18:
        maior = maior+1
print('A quantidde de pessoas maior de idade é: ', maior)
#Faça  um  programa  que  leia  a  idade  de  10  pessoas  e  informe  quantas  pessoas  são maiores de idade.
contador = 0
for idades in range(0,10):
    idade = int(input('Informe a idade: '))
    if idade >=18:
        contador = contador+1
print('A quantidade de pessoas maiores de idade é: {}'.format(contador))

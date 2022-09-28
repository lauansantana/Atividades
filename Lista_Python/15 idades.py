#Faça um código que lê a idade de 15 pessoas e mostre a quantidade de pessoas que possui a idade entre 20 e 30 anos.

contador = 0
for idades in range(0,15):
    idade = int(input('Informe a sua idade: '))
    if idade <= 30 and idade >=20:
        contador = contador+1
print("Quantidade de pessoas que possui a idade entre 20 e 30: {}".format(contador))

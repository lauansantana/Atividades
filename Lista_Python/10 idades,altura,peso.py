#Questao 13
#Faça um programa que receba 10 idades, alturas e pesos e que mostre:
# ●A idade média do grupo.
# ●A  quantidade  de  pessoas  com  peso  superior  a  90kg  e  altura  inferior  a 1,70.
# ●A  percentagem  de  pessoas  com  idade  entre  10  e  30  anos  com  altura superior a 1,80.

peso_superior = 0
altura_inferior = 0
idade_media = 0
porcentagem = 0

for dados in range(0,10):

    idade = float(input('Informe a sua idade: '))
    altura = float(input('Informe a sua altura: '))
    peso = int(input('Informe o seu peso: '))

    if idade > 0:
        idade_media = idade_media+idade

    if altura < 1.70:
        altura_inferior = altura_inferior+1

    if peso > 90:
        peso_superior = peso_superior+1

    if idade >= 10 and idade <=30 and altura > 1.80:
        porcentagem = porcentagem+1

print('A idade média do grupo é: {}'.format(idade_media/10))
print('Quantidade de pessoas com peso superior a 90kg: {}'.format(peso_superior))
print('Quantidade de pessoas com altura inferior a 1,70: {}'.format(altura_inferior))
print('A percentagem de pessoas com idade entre 10 e 30 anos com altura superior a 1,80 é: {}%'.format(porcentagem*10))

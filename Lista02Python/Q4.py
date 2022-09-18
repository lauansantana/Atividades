#Questao4
'''Um vendedor necessita de um algoritmo que calcule o preço total devido por um cliente.  O  algoritmo  deve  receber  o  código  de  um  produto  e  a  quantidade comprada e calcular o preço total, usando a tabela abaixo:
Código do Produto | Preço unitário
1001                5,32
1324                6,45
6548                2,37
0987                5,32
7623                6,45'''

total=0

codigo = (input('Digite o código do produto:\n [1001]\n [1324]\n [6548]\n [0987]\n [7623]\n'))
unidade = int(input('Informe a quantidade comprada: '))


if codigo == '1001':      #entre aspas para transformar o número em str
    total = unidade*5.32

if codigo == '1324':
    total =  unidade*6.45

if codigo == '6548':
    total = unidade*2.37

if codigo == '0987':
    total = unidade*5.32

if codigo == '7623':
    total = unidade*7623

else:
    print('Entrada Inválida.')

print('Valor total: {}R$'.format(total))

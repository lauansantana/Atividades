#Questao1
'''Elaborar  um  algoritmo  que  lê  3  valores  a,b,c  e  os  escreve.  A  seguir,  encontre  o maior dos 3 valores e o escreva com a mensagem : "É o maior ". '''


a = int(input('Informe o valor de A: '))
b = int(input('Informe o valor de B: '))
c = int(input('Informe o valor de C: '))

if a>b and a>c:
    print('A é o maior.')

elif b>a and b>c:
    print('B é o maior.')
    
else:
    print('C é o maior.')
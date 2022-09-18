#Questao 2
'''Implemente  um  programa  capaz  de  solicitar  para  o  usuário  o  seu  nome  e  a  sua idade.  
Após  isso,  deve  imprimir  na  tela  o  nome  do  usuário  e  o  ano  do  seu nascimento.
-Exemplo: 
  Usuário digita: Nome=João e Idade=20
  Programa imprime: João nasceu no ano de 2002.'''


nome = input('Olá, informe o seu nome: ')
idade = int(input('Informe a sua idade: '))
ano = 2022-idade

print("{} nasceu no ano de {}.".format(nome, ano))
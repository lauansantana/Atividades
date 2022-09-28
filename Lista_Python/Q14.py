#Implemente um código capaz de ler as notas de um aluno (AV1 e AV2) e informar se ele está ou  não  aprovado  na  disciplina.  Para  isso,  considere:  Média  >=  6  pontos  =  APROVADO.  Média entre 4 e 5,9 = FINAL e Média menor que 4 pontos = REPROVADO. Para cada uma das situações, imprima uma mensagem na tela para que o aluno fique ciente.

av1 = float(input('Informe a nota da AV1: '))
av2 = float(input('Informe a nota da AV2: '))

soma = (av1+av2)/2

if soma >= 6:
    print('APROVADO.')
elif soma <= 5.9 and soma >=4:
    print('FINAL.')
elif soma <4:
    print('REPROVADO.')
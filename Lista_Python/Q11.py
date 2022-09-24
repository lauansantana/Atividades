#Questao 11
#Faça  um  programa  que  verifique e  mostre os númerosentre 1000 e 2000 que, quando divididos por 11, produzem resto igual a 5.

for n in range(1000, 2000):
    if n%11 == 5:
        print(n)
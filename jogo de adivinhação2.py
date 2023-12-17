import random

valor_aleatorio=random.randint(1,10)
acertou=False
print('Vou sortear um número e desafio você a adivinha-lo!')
while acertou==False:
    chute=int(input('Chute um número de 1 a 10: '))

    if chute>valor_aleatorio:
        print('Chutou um número acima do sorteado!')
    elif chute<valor_aleatorio:
        print('Chutou um número abaixo do sorteado!')
    elif chute==valor_aleatorio:
        acertou=True
        print('Acertou!!!')
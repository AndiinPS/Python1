import random
valor_aleatorio=random.randint(0,10)
acertou=False
tentativas=0
print('Vou sortear um número e desafio você a adivinha-lo!')
while acertou==False:
    chute=int(input('Chute um número de 1 a 10: '))
    tentativas+=1
    if chute==valor_aleatorio:
        acertou=True
    else:
        if chute<valor_aleatorio:
            print('Chute alto...')
            print('Tente novamente...')
        elif chute>valor_aleatorio:
            print('Chute baixo...')
            print('Tente novamente...')

print('Parabéns! Você acertou após {} tentativas'.format(tentativas))
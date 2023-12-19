import random
from time import sleep
player=str(input('Escolha pedra ,papel ou tesoura:'))
jogo=['pedra','papel','tesoura']
computador=random.choice(jogo)
print(' 1, 2, 3 e já!')
sleep(1)
if player == computador:
    print('{} x {} Empate!'.format(player,computador))
elif(player=='pedra' and computador=='tesoura') or (player=='papel' and computador=='pedra') or (player=='tesoura' and computador=='papel'):
    print('{} x {} Venceu!'.format(player,computador))
else:
    print('{} x {} Perdeu'.format(player,computador))



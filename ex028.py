from random import randint
from time import sleep
computador=randint(0, 5)
print('-=-'*20)
print('  \033[36mVou selecionar um número entre 0 e 5. Tente advinhar...\033[m')
print('-=-'*20)
player=int(input('Escolha um número :'))
print('Processando...')
sleep(2)
if player==computador:
    print('Parabéns, você venceu!')
else:
    print('O número era {} e não o {}'.format(computador,player))
    print('Tente novamente, perdeu!')


from random import randint
vitoria=0
while True:
    player=int(input('Digite um valor:'))
    cpu=randint(0,10)
    total= player+cpu
    tipo=' '
    while tipo not in 'PI':
        tipo=input('Impar ou par? [I/P]').strip().upper()[0]
    print('Você jogou {} e o computador {}. Total de {}'.format(player,cpu,total))
    if tipo =='P':
        if total%2==0:
            print('Vitoria...')
            vitoria+=1
        else:
            print('Derrota...')
            break
    elif tipo =='I':
        if total %2==1:
            print('Vitoria...')
            vitoria+=1
        else:
            print('Derrota...')
            break
print('Game Over! Suas vitorias foram {} vezes'.format(vitoria))
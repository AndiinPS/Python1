print('{:^30}'.format('CAIXA ELETRÔNICO'))
valor=int(input('Digite o valor do saque R$: '))
total=valor
nota=50
total_notas=0
while True:
    if total>=nota:
        total-=nota
        total_notas+=1
    else:
        if total_notas>0:
            print('Total de {} notas de R${}'.format(total_notas,nota))
        if nota==50:
            nota=20
        elif nota==20:
            nota=10
        elif nota==10:
            nota=2
        total_notas=0
        if total==0:
            break
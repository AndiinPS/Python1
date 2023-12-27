n1=int(input('Digite o 1º valor:'))
n2=int(input('Digite o 2º valor:'))
selecione=0
while selecione!=5:
    print('''    Menu
[1] soma
[2] multiplica
[3] maior número
[4] inserir números
[5] fechar programa...''')
    selecione=int(input('Selecione uma opção:'))
    if selecione==1:
        somar=n1+n2
        print('A soma de {} + {} = {}'.format(n1,n2,somar))
    elif selecione==2:
        multiplicação=n1*n2
        print('A multiplicação de {} x {} = {}'.format(n1,n2,multiplicação))
    elif selecione==3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print('Entre {} e {} o maior valor é {}'.format(n1,n2,maior))
    elif selecione==4:
        print('Defina novos valores:')
        n1=int(input('Digite o 1º valor:'))
        n2=int(input('Digite o 2º valor:'))
    elif selecione==5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida, tente novamente')
print('Obrigado , volte sempre.')
        
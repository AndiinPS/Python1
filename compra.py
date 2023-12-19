compra=float(input('Qual o valor da compra:'))
print('''Formas de pagamento:
[1] á vista em dinheiro ou cheque com (10% de desconto)
[2] cartão de crédito á vista (5% de desconto)
[3] cartão de crédito parcelado em até 2 vezes (sem acrescimo)
[4] cartão de crédito parcelado em 3 vezes ou mais (20% de juros)''')
formas_pagamento=0
while formas_pagamento not in [1,2,3,4]:
    formas_pagamento=int(input('Escolha a sua opção de pagamento :'))
    if formas_pagamento==1:
        valor_final=compra-(compra*10/100)
    elif formas_pagamento==2:
        valor_final=compra-(compra*5/100)
    elif formas_pagamento==3:
        valor_final=compra
        parcela=compra/2
        print('Sua compra parcelada em 2x de R${:.2f} sem juros'.format(parcela))
    elif formas_pagamento==4:
        parcela=0
        while parcela<3:
            parcela=int(input('Quantas vezes? (Minimo 3 vezes):'))
            if parcela <3:
                print('Escolha de 3 vezes ou mais para essa opção')
        if parcela>=3:
            valor_final=compra+(compra*20/100)
            total_parcela=valor_final/parcela
            print('Sua compra parcelada em {}x de R${:.2f} com juros'.format(parcela,total_parcela))
        
    else:
        print('Opção inválida. Por favor, escolha entre 1 e 4.')
if formas_pagamento in [1,2,3,4]:
    print('Sua compra no valor de R${:.2f} vai custar R$ {:.2f} no final '.format(compra,valor_final))
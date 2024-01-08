total=acima_mil=menor_preço=contador=0
barato=' '
while True:
    produto=str(input('Qual produto: '))
    valor=float(input('Valor R$: '))
    contador+=1
    total+=valor
    if valor>1000:
        acima_mil+=1
    if contador==1 or valor<menor_preço:
        menor_preço=valor
        barato=produto
    resposta=' '
    while resposta not in "SN":
        resposta=str(input('Acrescentar mais produtos ao carrinho [S/N]? ')).strip().upper()[0]
    if resposta=='N':
        break
print('''Compra finalizada
{:.2f} foi o total da sua compra
E temos {} produtos que custa mais de R$ 1.000
O produto mais barato é {} que custa {:.2f}'''.format(total,acima_mil,barato,menor_preço))
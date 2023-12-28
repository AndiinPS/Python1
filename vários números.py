soma = quant = media = maior = menor = 0
resposta = 'S'
while resposta in 'Ss':
    num = int(input("Digite um número: "))
    soma += num
    quant += 1

    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resposta = input('Quer continuar? [S/N]').strip().upper()[0]

media = soma / quant
print('Você digitou {} números e a média foi {:.2f}'.format(quant,media))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))


print('{:^30}'.format('CAIXA ELETRÔNICO'))
valor = int(input('Digite o valor do saque R$: '))

# Verifica se o valor é sacável
if valor <= 0 or valor % 2 != 0:
    print("Valor inválido para saque. Por favor, digite um valor positivo e múltiplo de 2.")
else:
    total = valor
    notas = [100, 50, 20, 10, 5, 2]
    total_notas = 0
    i = 0

    while total > 0:
        nota = notas[i]
        if total >= nota:
            total -= nota
            total_notas += 1
        else:
            if total_notas > 0:
                print(f'Total de {total_notas} notas de R${nota}')
            total_notas = 0
            i += 1


from random import randint

print('{:^30}'.format('CAIXA ELETRÔNICO'))
valor = int(input('Digite o valor do saque R$: '))

# Verifica se o valor é sacável
if valor <= 0:
    print("Valor inválido para saque. Por favor, digite um valor positivo.")
else:
    total = valor
    notas = [100, 50, 20, 10, 5, 2]
    distribuicao_notas = {}
    impossivel_sacar = False

    for nota in notas:
        if total >= nota:
            quantidade_notas = total // nota
            total -= quantidade_notas * nota
            distribuicao_notas[nota] = quantidade_notas

    # Verifica se o valor restante é sacável
    if total > 0:
        print("Não é possível realizar o saque do valor solicitado com as notas disponíveis.")
        impossivel_sacar = True

    if not impossivel_sacar:
        for nota, quantidade in distribuicao_notas.items():
            if quantidade > 0:
                print(f'Total de {quantidade} notas de R${nota}')

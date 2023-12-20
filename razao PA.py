# Pedindo o primeiro termo e a razão da PA
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

# Inicializando uma lista para armazenar os termos da PA
termos = []

# Calculando e armazenando os 10 primeiros termos da PA na lista
for n in range(1, 11):
    termo_n = primeiro_termo + (n - 1) * razao
    termos.append(termo_n)

# Mostrando os 10 primeiros termos da PA
print('Os 10 primeiros termos da Progressão Aritmética são:')
for termo in termos:
    print(termo, end=' ')

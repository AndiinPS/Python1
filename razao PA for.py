print('  10 TERMOS DE UMA PA')
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = primeiro + (10 - 1) * razão
for n in range(primeiro, décimo + razão, razão):
    print('{}'.format(n), end=' > ')
print('Fim')



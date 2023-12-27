print('    10 TERMOS DE UMA PA')
primeiro=int(input('Digite o primeiro termo:'))
razão=int(input('Digite a razão:'))
termo=primeiro
contador=1
while contador<=10:
    print('{} > '.format(termo), end='')
    termo+=razão
    contador+=1
print('Fim')
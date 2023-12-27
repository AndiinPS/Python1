numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1
print('Calculando {}! = '.format(numero), end='')

for c in range(numero, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c

print(fatorial)

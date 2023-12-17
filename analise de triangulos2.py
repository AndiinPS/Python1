print('-=-'*10)
print('   \033[43mAnalisador de Triângulos2\033[m')
print('-=-'*10)
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode ser formado um triângulo!', end='')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Não pode ser formado um triângulo')

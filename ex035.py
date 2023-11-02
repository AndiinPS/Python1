print('-=-'*10)
print('   \033[43mAnalisador de Triângulos\033[m')
print('-=-'*10)
r1=float(input('Digite o cumprimento da primeria reta:'))
r2=float(input('Digite o comprimento da segunda reta:'))
r3=float(input('Digite o comprimento da terceira reta:'))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('Pode ser formado um triângulo!')
else:
    print('Não pode ser formado um triângulo')
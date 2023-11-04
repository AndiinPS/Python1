5from time import sleep
print('///'*20)
print('                \033[1;31;43mComparando números inteiros \033[m')
print('###'*20)
n1=int(input('Digite um número?:'))
n2=int(input('Digite outro número:'))
print('Comparando números ...')
sleep(3)
if n1>n2:
    print('O primeiro valor {} é maior!'.format(n1))
elif n2>n1:
    print('O segundo valor {} é maior!'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais {} , {}!'.format(n1,n2))
print('Analise concluida.')

from time import sleep
print('~~~~' * 15)
print('                     \033[7;41m Bases de Conversão \033[m')
print('---' * 20)
número = int(input('Digite um número inteiro:'))
conversão = int(input('''Escolha uma base de converção:
[ 1 ] binário
[ 2 ] octal
[ 3 ] hexadecimal
:'''))
print('Convertendo ...')
sleep(3)
if conversão == 1:
    print('{} convertido para BINÁRIO é {}'.format(número,bin(número)[2:]))
elif conversão == 2:
    print('{} convertido para OCTAL é {}'.format(número,oct(número)[2:]))
elif conversão == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(número,hex(número)[2:]))
else:
    print('Opção inválida. Escolha 1 para binário, 2 para octal ou 3 para hexadecimal.')

from time import sleep
from datetime import date
print('-_-'*20)
print('\033[7;32m               Sistema de Alistamento Militar              \033[m')
print('___'*20)
ano=int(input('Digite seu ano de nascimento:'))
idade=abs(ano-date.today().year)
m=(idade-18)
print('Analisando...')
sleep(3)
if idade<18:
    print('Você tem {} anos, falta {} anos para o seu Alistamento Militar!'.format(idade,abs(m)))
elif idade==18:
    print('Você tem {} anos e devera participar do processo de Alistamento Militar!'.format(idade))
elif idade>18:
    print('Você tem {} anos e já se passaram {} anos para o seu Alistamento Militar!'.format(idade,m))
print('FiM')

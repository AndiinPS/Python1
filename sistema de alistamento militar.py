from time import sleep
from datetime import date
print('-_-'*20)
print('               \033[7;32mSistema de Alistamento Militar\033[m')
print('___'*20)
ano_nascimento=int(input('Digite seu ano de nascimento:'))
ano_atual=date.today().year
idade=ano_atual-ano_nascimento
print('Analisando...')
sleep(2)
print('Quem nasceu em {} tem {} anos em {}'.format(ano_nascimento,idade,ano_atual))
if idade==18:
    print('Você tem {} anos e devera participar do processo de Alistamento Militar!'.format(idade))
elif idade<18:
    saldo=18-idade
    print('Você tem {} anos, falta {} anos para o seu Alistamento Militar!'.format(idade,saldo))
    ano=ano_atual+saldo
    print('Seu alistamento será em {},'.format(ano))
elif idade>18:
    saldo=idade-18
    print('Você tem {} anos e já se passaram {} anos para o seu Alistamento Militar!'.format(idade,saldo))
    ano=ano_atual-saldo
    print('Seu alistamento foi em {}'.format(ano))
print('FiM')

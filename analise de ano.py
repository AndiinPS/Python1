from datetime import date
print('---'*20)
print('                   \033[46mAnalisador de ano\033[m')
print('---'*20)
a=int(input('Digite um ano para analisar? Digite 0 para analisar o ano atual:'))
if a==0:
    a=date.today().year
if  a%4==0 and a%100!=0 or a%400==0:
    print('O ano {} é bissexto!'.format(a))
else:
    print('O ano {} não é bissexto!'.format(a))
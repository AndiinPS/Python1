from time import sleep
print('...'*20)
print('                  \033[46mAnalise de número\033[m')
print('...'*20)
numero=int(input('Digite um número:'))
u=numero//1%10
d=numero//10%10
c=numero//100%10
m=numero//1000%10
print('Analisando o número {}'.format(numero))
sleep(2)
print('Unidade:{}'.format((u)))
print('Dezena:{}'.format(d))
print('centena:{}'.format(c))
print('Milhar:{}'.format(m))

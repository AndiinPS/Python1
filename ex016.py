from math import trunc
from time import sleep
print('+++'*20)
print('               \033[40m Parte inteira de um número\033[m')
print('---'*20)
n=float(input(' Digite um número:'))
print('Calculando ...')
sleep(2)
print('O número digitado foi {} e a sua parte inteira é {}.'.format(n,trunc(n)))

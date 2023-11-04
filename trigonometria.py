from math import sqrt
from time import sleep
print('<->'*20)
print('            \033[44m Calculo de catetos e hipotenusa\033[m')
print('-^-'*20)
ca=float(input('Comprimento cateto adjacente:'))
co=float(input('Comprimento cateto oposto:'))
h=(co**2+ca**2)
print('Calculando ...')
sleep(2)
print('E o comprimento da sua hipotenusa é {:.2f} '.format(sqrt(h)))

import math
from time import sleep
print('...'*20)
print('                 \033[40m Seno Cosseno e Tangente\033[m')
print('...'*20)
a=float(input('Digite o valor do ângulo:'))
s=math.sin(math.radians(a))
c=math.cos(math.radians(a))
t=math.tan(math.radians(a))
print('Calculando o ângulo .....')
sleep(2)
print('O ângulo de {} tem o seno de {:.2f}'.format(a,s))
print('O ângulo de {} tem o cossene de {:.2f}'.format(a,c))
print('O ângulo de {} tem a tangente de {:.2f}'.format(a,t))


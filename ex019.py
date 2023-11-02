import random
print('~~~~'*15)
print('                       \033[35m Soteio\033[m')
print('___'*20)
a=input('Digite o nome do primeiro participante:')
b=input('Digite o nome do segundo participante:')
c=input('Digite o nome do terceiro participante:')
d=input('Digite o nome do quarto participante:')
list=[a,b,c,d]
print('Os paticipantes são: {} , {} , {} e {}.'.format(a,b,c,d))
print('O vencedor foi {}'.format(random.choice(list)))

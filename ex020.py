import random
print('###'*20)
print('          \033[35mSorteio para apresentação dos trabalhos\033[m')
print('###'*20)
a1 = input('nome do primeiro aluno:')
b2 = input('Nome do segundo aluno:')
c3 = input('Nome do terceiro aluno:')
d4 = input('Nome do quarto aluno:')
list = [a1 , b2 , c3 , d4]
random.shuffle(list)
print('A ordem de apresentação será:')
print(list)


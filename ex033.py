print('_-_'*20)
print('                \033[35mMaior e menor número\033[m')
print('-_-'*20)
n1=int(input('Digite um número:'))
n2=int(input('Digite outro número:'))
n3=int(input('Digite só mais um número:'))
list=[n1,n2,n3]
print('O número maior é:\033[31m{}\033[m'.format(max(list)))
print('O menor número é:\033[34m{}\033[m'.format(min(list)))

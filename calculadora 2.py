print('~~~'*20)
print('                 \033[4;35;40mCALCULADORA \033[m')
print('~~~'*20)
numero=int(input('Digite um número:'))
for i in range(10 ,-1,-1):
    resultado=numero*i
    print('{} x {} = {}'.format(numero,i,resultado))
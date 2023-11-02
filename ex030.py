print('~~~'*20)
print('                 \033[4;35;40mJogo do IMPA ou PAR\033[m')
print('~~~'*20)
n=int(input('Digite um número:'))
if n%2==0:
    print('Esse número é \033[32mPAR!\033[m!')
else:
    print('Esse número é \033[33mIMPAR!\033[m')

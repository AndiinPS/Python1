print('>>>'*20)
print('                       \033[7;33mUber Driver\033[m')
print('<<<'*20)
d=int(input('Qual é a distância tem seu trajéto?'))
if d<=200:
    vc=d*0.50
    print('O valor da sua viagem é de R${:.2f}'.format(vc))
else:
    d>200
    vl=d*0.45
    print('O valor da sua viagem é de R${:.2f}'.format(vl))
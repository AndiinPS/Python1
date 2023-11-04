print('~~~'*20)
print('                 \033[4;35;40mCALCULO DE NOTAS\033[m')
print('~~~'*20)
p1=float(input('Nota primeira prova:'))
p2=float(input('Nota segunda prova:'))
m=(p1+p2)/2
print('Anderson tirou: {} na primeira prova e {} na segunda'.format(p1,p2),end=' ')
print('e teve como nota média:',m)

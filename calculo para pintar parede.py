print('~~~'*20)
print('                 \033[4;35;40mCALCULO DE TINTA\033[m')
print('~~~'*20)
alt=float(input('Digite a altura da parede:'))
lar=float(input('Digite a largura da parede:'))
are=lar*alt
tin=are/2
print(' A parede tem a dimensão de {}x{} e sua área é de {}m² e a quantidade necessária para pintar é de {}litros de tinta!'.format(lar,alt,are,tin))

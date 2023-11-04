print('___'*20)
print('               \033[45mDepartamento de trânsito\033[m')
print('___'*20)
v=int(input('Quantos KM/H seu veículo estava?'))
if v<=80:
    print('Tenha uma viagem!')
    print('Dentro da velocidade estabelicida da via de \033[32m80\033[mkm/h')
else:
    va = v - 80
    m = va * 7.00
    print('Seu veículo foi multado, velocidade \033[31m{}\033[mkm/h acima da velocidade estabelecida da via de \033[32m80\033[mkm/h!'.format(v))
    print('O valor da sua multa é de R$\033[32m{:.2f}'.format(m))
print('~~~'*20)
print('                 \033[4;35;40mREAL PARA DÓLAR\033[m')
print('~~~'*20)
s=float(input('Valor na carteira:R$'))
d=s/4.73
print(' Anderson tem R${} reais em sua carteira e consegue comparar ${:.2f} dólar com o valor que disponhe em sua carteira. '.format(s,d))

print('-=-'*17)
print('          \033[7;40mCalculo de aumento salárial\033[m')
print('-=-'*17)
s=float(input('Digite seu salário para calculo do seu aumento R$:'))
if s<=1250:
    sn=s+(s*15/100)
else:
    sn=s+(s*10/100)
print('Seu salário de R$\033[31m{:.2f}\033[m com o aumento passou para R$\033[32m{:.2f}'.format(s,sn))

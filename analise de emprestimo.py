from time import sleep
print('---'*20)
print('              \033[4;35m Analise de empréstimo bancário \033[m')
print('___'*20)
valor=float(input('Qual o valor desejado: R$'))
salário=float(input('Qual valor da sua renda mensal: R$'))
anos=int(input('Quantos anos ira ser pago o valor?'))
prestação=valor/(anos*12)
mínimo=salário*30/100
print('Calculando ...')
sleep(2)
print('Valor de R${:.2f} a ser pago em {} anos, a parcela é de R${:.2f}'.format(valor,anos,prestação))
if prestação <= mínimo:
    print(' O seu empréstimo foi APROVADO!')
else:
    print('O seu foi empréstimo NEGADO!')





from time import sleep
print('¬¬'*20)
print('        \033[43m Localiza aluguel de carro\033[m')
print('¬¬'*20)
km=float(input('Quantos km percorreu?'))
dia=int(input('Quantos dias com o carro?'))
pgt=(dia*60)+(km*0.15)
print('Calculando custos ...')
sleep(2)
print('Valor a pagar pelo aluguél R${:.2f}'.format(pgt))

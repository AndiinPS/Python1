print('~~~'*20)
print('                 \033[4;35;40mCUPOM DE DESCONTO\033[m')
print('~~~'*20)
produto=float(input('Valor do produto:'))
cupom_desconto=produto*(1-0.05)
print('Valor R$ {:.2f} ao aplicar o cupom de 5% de desconto R$ {:.2f}'.format(produto,cupom_desconto))
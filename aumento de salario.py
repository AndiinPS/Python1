print('~~~'*20)
print('                 \033[4;35;40mAUMENTO SALARIO\033[m')
print('~~~'*20)
s=float(input(' Salario base: R$'))
a=s*(1+0.15)
print(' Anderson recebia R${:.2f} e com o novo aumento de 15% passou a ter o salario base de R${:.2f}'.format(s,a))
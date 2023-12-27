soma=0
contagem=0
for c in range(1,7):
    numero=int(input('Digite o valor {}:'.format(c)))
    if numero%2==0:
        soma+=numero
        contagem+=1
    
    
print('A soma dos {} números digitados que são par é: {}'.format(contagem,soma))

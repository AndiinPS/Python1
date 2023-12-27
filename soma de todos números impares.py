soma = 0
contagem=0
for numero in range(1, 501,2):
    if numero % 3 == 0:
        soma +=numero
        contagem +=1
print('A soma dos {} números ímpares múltiplos de três no intervalo é {}'.format(contagem,soma))
    
        



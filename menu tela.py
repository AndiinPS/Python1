def ler_valores():
    valores=[]
    for i in range(1,3):
        valor=int(input('Digite o {}º valor:'.format(i)))
        valores.append(valor)
    return valores

def soma(valores):
    return sum(valores)

def multiplica(valores):
    resultado=1
    for valor in valores:
        resultado *=valor
    return resultado

def maior(valores):
    return max(valores)

valores=ler_valores()

selecione=0

while selecione!=5:
    print(''' Menu:
[1] somar
[2] multiplicar
[3] maior
[4] digitar novos valores
[5] fechar programa ''')
    selecione=int(input('Escolha a opção no menu:'))
    if selecione==1:
        print('Resultado da soma:', soma(valores))
    elif selecione==2:
        print('Resultado da multiplicação:', multiplica(valores))
    elif selecione==3:
        print('Maior valor:', maior(valores))
    elif selecione==4:
        valores=ler_valores()
    elif selecione==5:
        print('Fechando o programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')

print()

from time import sleep
numero=int(input('Digite um número:'))
if numero>0:
    fatorial=1
    for item in range(1,numero+1):
        fatorial=fatorial*item
print('calculando ...')        
sleep(2)
print('O fatorial do número {} é {}!'.format(numero,fatorial))


numero = int(input('Digite quantos elementos da sequência de Fibonacci você quer ver: '))
t1=0
t2=1
print('{} > {}'.format(t1,t2), end='')
contador=3
while contador <= numero:
    t3=t1+t2
    print(' > {}'.format(t3), end='')
    t1=t2
    t2=t3
    contador+=1
print(' > Fim')

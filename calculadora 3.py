while True:
    numero=int(input('Digite um número: '))
    if numero<0:
       break
    for i in range(10 ,-1,-1):
        print(f'{numero} x {i} = {numero*i}')
    
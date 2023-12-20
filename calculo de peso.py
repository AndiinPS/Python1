peso_maior=0
peso_menor=float('inf')
for i in range(0,5):
    peso=float(input('Digite o peso da {}ª pessoa (kg): '.format(i+1)))
    if peso>peso_maior:
        peso_maior=peso
    if peso<peso_menor:
        peso_menor=peso
print('''O maior peso foi {}kg e 
o menor peso foi {}kg'''.format(peso_maior,peso_menor))
    
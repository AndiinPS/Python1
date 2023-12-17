peso=float(input('Digite seu peso (kg):'))
altura=float(input('Digite sua altura (m):'))
indice=peso/(altura**2)
print(f'Sua altura {altura:.2f} e peso {peso:.2f}, seu imc é {indice:.1f}', end=' ')
if indice<18.5:
    print('Abaixo do peso')
elif 18.5 <=indice <25:
    print('Peso ideal')
elif 25<=indice <30:
    print('Sobrepeso')
elif 30 <= indice <40:
    print('Obesidade')
else:
    print('Obesidade móbida')
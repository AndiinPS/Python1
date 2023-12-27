def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

try:
    num = int(input('Digite quantos elementos da sequência de Fibonacci você quer ver: '))
    fibonacci(num)
except ValueError:
    print('Por favor, insira um número inteiro válido.')

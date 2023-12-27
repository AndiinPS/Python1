def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence[:n]


numero = int(input('Digite um número inteiro para a sequência de Fibonacci: '))


resultado = fibonacci(numero)
print('Os primeiros {} elementos da sequência de Fibonacci são: {}'.format(numero,resultado))

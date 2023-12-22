
def ok_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Solicita o número ao usuário
num = int(input('Digite um número: '))

# Verifica se o número é primo e exibe o resultado
if ok_primo(num):
    print('{} é um número primo.'.format(num))
else:
    print('{} não é um número primo.'.format(num))

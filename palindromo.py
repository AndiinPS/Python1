def verifica_palindromo(frase):
    # Remover espaços em branco e transformar em minúsculas
    frase = frase.replace(" ", "").lower()
    
    # Verificar se a frase é igual à sua versão invertida
    return frase == frase[::-1]


fase_teste = input('Digite a frase:')
if verifica_palindromo(fase_teste):
    print(f"A fase '{fase_teste}' é um palíndromo!")
else:
    print(f"A fase '{fase_teste}' não é um palíndromo.")

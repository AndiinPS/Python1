idade_media = 0
idade_homem = 0
idade_mulheres = 0
nome_homem = ""

for i in range(4):
    nome, idade, sexo = input('{}ª pessoa digite seu nome, idade e sexo (separados por espaço): '.format(i+1)).split()
    idade = int(idade)
    idade_media += idade
    
    if sexo.lower() == 'masculino' or sexo.lower() == 'm':
        if idade > idade_homem:
            idade_homem = idade
            nome_homem = nome
    
    if sexo.lower() == 'feminino' or sexo.lower() == 'f':
        if idade < 20:
            idade_mulheres += 1

idades = idade_media / 4

print('''A média de idade do grupo é de {}, o homem mais velho se chama {} e tem {} anos.
 Há {} mulher(es) com menos de 20 anos.'''.format(idades, nome_homem, idade_homem, idade_mulheres))

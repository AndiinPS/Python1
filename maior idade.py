from datetime import date
ano_atual=date.today().year
maior_idade=21
maiores=0
menores=0
for pessoas in range(1,8):
    ano_nascimento=int(input('Digite o ano de nascimento da {}ª pessoa:'.format(pessoas)))
    idade=ano_atual-ano_nascimento
    if idade >=maior_idade:
        maiores+=1
    else:
        menores+=1
print('''{} pessoas são maiores de idade e
{} pessoas ainda são menores de idade.'''.format(maiores,menores))
    
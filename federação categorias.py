from datetime import date

data_nascimento=int(input("Digite o ano de nascimento do atleta:"))
ano_atual=date.today().year
idade=ano_atual-data_nascimento
print('O atleta tem {} anos'.format(idade))
if idade<=9:
    print('Esse atleta está na categoria mirim')
elif idade<=14:
    print('Esse atleta está na categoria infantil')
elif idade<=19:
    print('Esse atleta está na categoria junior')
elif idade<=25:
    print('Esse atleta está na categoria sênior')
else:
    print('Esse atleta está na categoria master')
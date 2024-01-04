total18=total_maculino=total_mulheres_20=0
while True:
    idade=int(input('Idade:'))
    genero=' '
    while genero not in 'FM':
        genero=input('Genero [F/M]:').strip().upper()[0]
    if idade>=18:
        total18+=1
    if genero=='M':
        total_maculino+=1
    if genero=='F' and idade<20:
        total_mulheres_20+=1

    resposta=' '
    while resposta not in 'SN':
        resposta=input('Continuar cadastro [S/N]?').strip().upper()[0]
    if resposta=='N':
        break
print('''Total de pessoas com mais de 18 anos:{}
Ao todo temos {} homens cadastrados
E {} mulheres com menos de 20 anos de idade'''.format(total18,total_maculino,total_mulheres_20))
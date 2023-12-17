print('~~~'*20)
print('                 \033[4;35;40mCALCULO DE NOTAS 2\033[m')
print('~~~'*20)
p1=float(input('Nota primeira prova:'))
p2=float(input('Nota segunda prova:'))
media=(p1+p2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(p1,p2,media))
if media<5.0:
    print('Reprovado')
elif media>=5.0 and media <= 6.9:
    print('Recuperação')
elif media>=7.0:
    print('Aprovado')    

pessoa=input('Qual o genero do seu sexo [M/F]?').strip().upper()[0]
while pessoa not in 'MmFf':
    pessoa=input('Dados inválidos, favor repetir novamente:').strip().upper()
print('Informação {} registrada com sucesso'.format(pessoa))




    
                 

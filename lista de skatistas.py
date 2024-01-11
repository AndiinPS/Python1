from time import sleep
contador=0
atletas=('Nyjah Huston','Sora Shirai','Aurelien Giraud','Gustavo Ribeiro','Ginwoo Onodera','Kairi Netsuke','Yuto Horigome','Richard Tury','Kelvin Hoefler','Toa Sasaki','Jagger Eaton','Vincent Milou','Cordano Russell','Alex Midler','Giovanni Vianna','Chris Joslin','Yukito Aoki','Matias Dell Olio','Ryan Decenzo',
'Braden Hoban')

print('Lista com os 20 skatistas mundiais 2024:')
for r,atleta in enumerate(atletas,start=1):
    print('{}º {}'.format(r,atleta))

print('---'*30)
sleep(2)

print('Os 5 primeiros da lista mundial:')
for contador in range(5):
    print('{}º {}'.format(contador+1,atletas[contador]))

print('---'*30)
sleep(2)

print('Os 4 ultimos colocados da lista mundial:')
for contador in range(16,20):
    print('{}º {}'.format(contador+1,atletas[contador]))

print('---'*30)
sleep(2)

print('Lista em ordem alfabetica:')
print('{}'.format(sorted(atletas)))

print('---'*30)
sleep(2)


print('Na {}º posição da lista temos {}'.format(8,atletas[7]))

print('---'*30)


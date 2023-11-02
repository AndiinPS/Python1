from time import sleep
print('´´´'*20)
print('\033[1;30;44m             Termometro de ºC para ºF                      \033[m')
print('___'*20)
tc=float(input(' Digite a temperatura ºC:'))
print('\033[31mCalculando\033[m...')
sleep(2)
print('A Temperatura de {}ºC corresponde a {}ºF!'.format(tc,tc*1.8+32))


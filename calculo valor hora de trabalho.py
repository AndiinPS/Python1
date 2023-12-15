from time import sleep
salario_base=int(input('Qual é seu salário mensal?'))
horas_trabalhadas_mes=int(input('Quantas horas trabalha por mês?'))
valor_hora=(salario_base)/(horas_trabalhadas_mes)
print('Calculando ...')
sleep(2)
print('Valor por hora trabalhado R${:.2f}'.format(valor_hora))




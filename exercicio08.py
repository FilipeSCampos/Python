#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganha = int(input('quanto voce ganha por hora?: '))
horas = float(input('quantas horas voce trabalha?: '))

salariodiario = (ganha * horas)
print(salariodiario)

salariomensal = (salariodiario * 30)
print(salariomensal)
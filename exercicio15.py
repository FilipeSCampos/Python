#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.

salariohora = int(input('Quanto você ganha por hora?'))

horasnomes = int(input("quantas horas voce trabalha no mes?"))

salariomes = (salariohora * horasnomes)

impostoderenda = (11/100) * salariomes
inss = (8/100) * salariomes
sindicato = (5/100) * salariomes

salarioliquido = salariomes - (impostoderenda + inss + sindicato)

print(f"O seu salario mensal é: {salariomes}")
print(f"O desconto do imposto de renda  é: {impostoderenda}")
print(f"O desconto do inss é: {inss}")
print(f"o desconto do sindicato é:{sindicato}")
print(f"O seu salario liquido é: {salarioliquido}")
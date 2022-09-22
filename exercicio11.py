#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
#  e lhe contraram para desenvolver o programa que calculará os reajustes
#Faça um programa que recebe o salário de um colaborador 
# e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input('Qual o seu salario?:'))

aumento20 = (20/100 * salario)

aumento15 = (15/100 * salario)

aumento10 = (10/100 * salario)

aumento5 = (5/100 * salario)

novosalario20 = (salario  + (20/100 * salario))

novosalario15 = (salario + (15/100 * salario))

novosalario10 = (salario +(10/100 * salario))

novosalario5 = (salario + (5/100 * salario))

if salario <= 280:
    print(f'o seu aumento salarial foi de 20%, seu salario antes da correção: {salario}'
        f'seu salario corrigido é: {novosalario20} e o valor de aumento é de: {aumento20}')
elif salario > 280 and salario <= 700:
    print(f'o seu aumento salarial foi de 15%, seu salario antes da correção: {salario}'
        f'seu salario corrigido é: {novosalario15} e o valor de aumento é de: {aumento15}')
elif salario > 700 and salario <= 1500:
    print(f'o seu aumento salarial foi de 10%, seu salario antes da correção: {salario}'
        f'seu salario corrigido é: {novosalario10} e o valor de aumento é de: {aumento10}')
elif salario > 1500:
    print(f'o seu aumento salarial foi de 5%, seu salario antes da correção: {salario}'
        f'seu salario corrigido é: {novosalario5} e o valor de aumento é de: {aumento5}')
#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.


dia = int(input('insira o dia: '))

mes = int(input('insira o mes: '))

ano = int(input('insira o ano: '))

valida = False

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes ==10 or mes==12):
    if (dia <= 31):
        valida = True
elif (mes ==4 or mes ==6 or mes==9 or mes== 11):
    if(dia <= 30):
        valida = True
#teste pra ver se fevereiro vai ter 28 ou 29 se for bissexto

elif mes ==2:
    if(ano % 4 == 0):
        if(dia<=29):
            valida = True
        elif(dia<=28):
            valida = True
if (valida):
    print('Data valida')
else:
    print('Data invalida')
#Faça um Programa que peça um número correspondente a um determinado ano
#e em seguida informe se este ano é ou não bissexto.

ano = int(input('insira um ano: '))
#pra ser bissexto tem que possuir 366 dias
#porem um ano bissexto so vem a cada 4 anos
#se um ano for divisivel por 4 e nao tiver resto entao ele é bissexto

if (ano % 4) == 0:
    print(f'é bissexto')
else:
    print(f'Não é bissexto')

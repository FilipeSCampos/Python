#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
x = [0,0,0,0]

import statistics

for i in range (4):
    if(i == 0):
        x[i]= float(input('Valor da primeira nota: '))
    elif(i == 1):
        x[i] = float(input('Valor da segunda nota: '))
    elif(i == 2):
        x[i]= float(input('Valor da terceira nota: '))
    elif(i ==3):
        x[i] =float(input('Valor da quarta nota: '))
#funcao mean da biblioteca statistics me da a media exata 
#nesse caso de tudo que ta dentro da lista x
print(f'Sua media foi {statistics.mean(x)}')



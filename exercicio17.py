#Faça um programa para uma loja de tintas
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
#ou em galões de 3,6 litros, que custam R$ 25,00.
#informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math 
tamanho = int(input("Quantos metros quadrados?"))

litros = (tamanho/6) * 1.1
latas = math.ceil(litros/18)
valorlatas = latas * 80
galoes = math.ceil(litros/3.6)
valorgaloes = galoes * 25

mixlatas = round(litros /18)
mixgaloes = round((litros - mixlatas * 18)/ 3.6)

if ((litros - (mixlatas * 18) % 3.6 != 0)):
    mixgaloes += 1
    total_mix = (mixlatas * 80) + (mixgaloes * 25)

print(f'se for comprar so latas de 18 litros ira precisar de {latas} latas(s) e ira custar R$ {valorlatas}')
print(f'se for comprar so galoes de 3,6 litros ira precisa de {galoes} galao(oes) e ira custar R$ {valorgaloes}')
print(f'Se deseja mesclar latas e galoes para dar o que precisar realmente sera necessario {mixlatas} latas'
f'0 e {mixgaloes} galoes e ira custar R$ {total_mix:.2f}') 

#Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes

lado1 = int(input('Valor do primeiro lado: '))

lado2 = int(input('Valor do segundo lado: '))

lado3 = int(input('Valor do terceiro lado: ' ))

#l1 + l2 > l3
#l1 + l3 > l2
#l2 + l3 > l1

#verificaçao de triangulo

if lado1 + lado2 < lado3 or lado1 + lado3 < lado2 or lado3 + lado2 < lado1:
    print('Não é um triangulo')
elif lado1 == 0 or lado2 == 0 or lado3 == 0:
    print('Não é um triangulo')
else:
    print('É um triangulo')

#classificaçao de triangulo

if lado1 == lado2 and lado1 == lado3:
    print('equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('isoceles')
else:
    print('escaleno')


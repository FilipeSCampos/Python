#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('qual o preço do primeiro produto?: '))

produto2 = float(input('qual o preço do segundo produto?: '))

produto3 = float(input('qual o preço do terceiro produto?: '))

if produto1 > produto2 and produto1 > produto3:
    print('Não compra o 1 que é o mais caro')
elif produto2 > produto1 and produto2 > produto3:
    print('Não compra o 2 que é o mais caro')
elif produto3 > produto1 and produto3 > produto2:
    print('Não compra o 3 que é o mais caro')

if produto1 < produto2 and produto1 < produto3:
    print('Compra o produto 1 é o mais barato de todos')
elif produto2 < produto1 and produto2 < produto3:
    print('Compra o produto 2 é o mais barato de todos')
elif produto3 < produto1 and produto3 < produto2:
    print('Compra o produto 3 é o mais barato de todos')





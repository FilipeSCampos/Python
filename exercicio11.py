#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

primeiro = int(input('insira o primeiro numero: '))
segundo = int(input('insira o segundo numero: '))
terceiro = float(input('insira o terceiro numero: '))

a = ((2 * primeiro) * (1/2 * segundo))
b = ((3 * primeiro) + terceiro)
c = (terceiro ** 3)

print(a)
print(b)
print(c)
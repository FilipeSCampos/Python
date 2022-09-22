#Faça um Programa que leia três números e mostre o maior deles.

a = float(input('insira o primeiro numero'))

b = float(input('insira o segundo numero'))

c = float(input('insira o terceiro numero'))

if a > b and a > c:
    print(f'a é o maior de todos{a}')
elif b > a and b > c:
    print(f'b é o maior de todos{b}')
elif c > a and c > b:
    print(f'c é o maior de todos{c}')
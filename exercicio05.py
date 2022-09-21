#Faça um Programa que converta metros para centímetros.
from re import X


def escala(x):
    print(x * 100)
x = int(input('ensira um numero em metros:'))

print(f'em centimetros sao:'), escala(x)
#Faça um Programa que leia três números e mostre-os em ordem decrescente.
#de um jeito mais elegante usando lista

n1 = float(input('Insira o primeiro numero: '))

n2 = float(input('Insira o segundo numero: '))

n3 = float(input('Insira o terceiro numero: '))

lista = [n1,n2,n3]

lista.sort(reverse=True)
print(lista)
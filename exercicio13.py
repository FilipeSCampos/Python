#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

#numero vai virar string pq eu nao sei como fazer dicionario relacionando inteiro com string
numero = input('Insira um numero de 1 á 7: ')

#dicionario
semana = {'1':'Domingo','2':'Segunda-Feira','3':'Terça-Feira','4':'Quarta-Feira','5':'Quinta-Feira','6':'Sexta-feira','7':'Sabado'}

print(semana[numero])
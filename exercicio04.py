#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ['a','e','i','o','u']

letra = input('degite uma letra: ')

if letra in vogal:
    print('é vogal')
else:
    print('é consoante')
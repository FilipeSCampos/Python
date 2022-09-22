#Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem
#  "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso

turno = input('Em qual turno voçê estuda? M para matutino V para Vespertino ou N para Noturno: ')

if turno == 'M' or turno == 'm':
    print('Bom dia!')
elif turno == 'V' or turno == 'v':
    print('Boa Tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa noite!')
else:
    print('Valor invalido')
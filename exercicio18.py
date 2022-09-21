#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = int(input('qual o tamanho do seu arquivo? em MB:'))

velocidade = int(input('qual a velocidade em Mbps?: '))

tempo = tamanho/ (velocidade/8)

print(f'O tempo necessario sera de: {tempo}')
#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, 
# e calcule a sua média.
#  A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
#mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

#pensando em um semestre estudantil com 2 bimestres e cada bimestre com 2 notas


nota1 = float(input('Qual a sua primeira nota do primeiro bimestre?: '))
nota2 = float(input('Qual a sua segunda nota do primeiro bimestre?: '))

media1 = (nota1 + nota2)/ 2

nota3 = float(input('Qual sua primeira nota do segundo bimestre?: '))
nota4 = float(input('Qual a sua segunda nota do segundo bimestre?: '))

media2 = (nota3 + nota4)/2

mediasemestre = (media1 + media2)/2

if mediasemestre >= 6.0 and mediasemestre <= 10.0 :
    print(f'APROVADO COM NOTA: {mediasemestre}')
elif mediasemestre >= 0 and mediasemestre < 6.0:
    print(f'REPROVADO COM NOTA: {mediasemestre}')
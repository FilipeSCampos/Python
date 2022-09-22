#Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Qual a sua primeira nota? '))

nota2 = float(input('Qual a sua segunda nota?: '))

media = (nota1 + nota2)/ 2

if media == 10:
    print(f'Aprovado com Distinção e sua media foi: {media}')
elif media >= 7 and media < 10:
    print(f'Aprovado e sua media foi: {media}')
else:
    print(f'reprovado e sua media foi: {media}')
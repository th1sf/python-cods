#Escreva um programa que leia 6 notas diferentes e faça a média do aluno

#leitura de dados

nota_1 = float(input('Digite primeira nota: '))
nota_2 = float(input('Digite segunda nota: '))
nota_3 = float(input('Digite terceira nota: '))
nota_4 = float(input('Digite quarta nota: '))
nota_5 = float(input('Digite quinta nota: '))
nota_6 = float(input('Digite sexta nota: '))

#calculo

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5 + nota_6) / 6

#resultado

print(f'Sua média é {media}')

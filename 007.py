#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.

#Leitura de dados

salario = float(input('Digite seu salario: '))

#Calculo

reajuste = (salario * 0.6) + salario
#reajuste = salario * 1.6

#Resultado

print(f'O salário de {salario:.2f} com o reajuste de 60% será de: {reajuste:.2f}')
#print(f'O salario final é {salario * 1.6})
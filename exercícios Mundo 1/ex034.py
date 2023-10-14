#    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o seu salário?: '))

if salario <= 1250:
    aumento = (salario * 0.15) + salario
    print('O seu novo salário é: {:.2f}'.format(aumento))
else:
    aumento = (salario * 0.10) + salario
    print('O seu novo salário é: {:.2f}'.format(aumento))

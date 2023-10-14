# Escreva um programa que leia 'dois números' inteiros e compare-os. Mostrando na tela uma mensagem:
# -O primeiro número é maior     -O segundo número é maior    -Não existe valor maior, os dois são iguais.

print('Insira dois números inteiros:')
print('*'*50)

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

if num1 > num2:
    print('O PRIMEIRO número é maior')
elif num1 < num2:
    print('O SEGUNDO número é maior')
elif num1 == num2:
    print('Não existe número maior, os dois SÃO IGUAIS')

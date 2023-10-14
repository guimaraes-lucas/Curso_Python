"""
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o 'valor da casa', o
'salário' do comprador e em quantos anos ele vai pagar.
    A prestação mensal, não pode exceder '30%' do salário ou então o empréstimo será negado.
"""

valor = int(input('Qual o valor da casa?: '))
salario = int(input('Qual o seu salário?: '))
anos = int(input('Em quantos anos você deseja pagar?: '))

parcela = valor / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos), end='')
print(' a prestação será de R${:.2f}'.format(parcela))

if parcela > salario * 0.3:
    print('Desculpe você não pode realizar esse financiamento')
elif parcela <= salario * 0.3:
    print('Parabéns! Você poderá financiar sa casa')

"""
    Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE
PAGAMENTO:
            -Á vista DINHEIRO/CHEQUE: 10% de desconto       -3X OU MAIS no cartão: 20% de juros
            -Á vista no CARTÃO: 5% de desconto
            -Em até 2X NO CARTÃO: preço normal
"""

preco = float(input('Qual o preço do produto?: '))

print('\033[0:32m----------------------Formas de pagamentos disponíveis----------------------\033[m')
print('\033[0:30:44m[ 1 ]\033[m Á vista DINHEIRO/CHEQUE')
print('\033[0:30:44m[ 2 ]\033[m Á vista no CARTÃO')
print('\033[0:30:44m[ 3 ]\033[m 2X no CARTÃO')
print('\033[0:30:44m[ 4 ]\033[m 3X ou mais no CARTÃO')

opcao = int(input('Qual á forma de pagamento?: '))

if opcao == 1:
    desconto = preco - (preco * 0.1)
    print('Forma de pagamento á vista selecionada seu produto vai ficar R${}'.format(desconto))
elif opcao == 2:
    desconto = preco - (preco * 0.05)
    print('Forma de pagamento á vista cartão selecionada seu produto vai ficar R${}'.format(desconto))
elif opcao == 3:
    parcela = preco / 2
    print('Você escolheu o pagamento parcelado em 2x cada parcela vai ficar R${}'.format(parcela))
elif opcao == 4:
    quantasParcelas = int(input('Gostaria de parcelar em quantas vezes?: '))
    novoPreco = preco + (preco * 0.2)
    parcela = novoPreco / quantasParcelas

    print('Você escolheu parcelar em {} vezes com um acréscimo de 20% o novo valor vai ser R${}'.format(quantasParcelas, novoPreco))
    print('As parcelas serão no valor de R${}'.format(parcela))
else:
    print('\033[0:31mOpção inválida\033[m')

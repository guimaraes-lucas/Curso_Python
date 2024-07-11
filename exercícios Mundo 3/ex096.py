"""
    Faça um programa que tenha uma FUNÇÃO chamada ÁREA(), que receba as dimensões de um Terreno retangular (LARGURA e
COMPRIMENTO) e mostre a ÁREA DO TERRENO.
"""


def area(largura, comprimento):
    x = largura * comprimento
    print(f'A área de um terreno {largura}m x {comprimento}m é {x}m². ')

print('-'*30)
print(f'ÁREA DO TERRENO')
print('-'*30)


larg = float(input('Qual a largura do seu terreno? (m) '))
comp = float(input('Qual o comprimento do seu terreno? (m) '))

print(area(larg, comp))

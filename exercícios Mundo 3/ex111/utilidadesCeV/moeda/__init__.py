def aumentar(valor=0, taxa=0, converter=False):
    porcentagem = valor * (taxa / 100)
    total = valor + porcentagem

    if converter:
        return moeda(total)
    else:
        return total


def diminuir(valor=0, taxa=0, converter=False):
    porcentagem = valor * (taxa / 100)
    total = valor - porcentagem

    if converter:
        return moeda(total)
    else:
        return total


def dobro(valor=0, converter=False):
    total = valor * 2

    if converter:
        return moeda(total)
    else:
        return total


def metade(valor=0, converter=False):
    total = valor / 2

    if converter:
        return moeda(total)
    else:
        return total


def moeda(valor=0, moeda='R$'):
    convertido = f'{moeda} {valor:.2f}'.replace('.', ',')
    return convertido


def resumo(valor=0, aumento=0, reducao=0):
    print('-'* 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)

    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')

    print('-' * 40)

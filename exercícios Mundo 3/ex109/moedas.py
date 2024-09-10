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

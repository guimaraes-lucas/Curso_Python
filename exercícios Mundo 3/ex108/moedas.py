def aumentar(valor=0, taxa=0):
    porcentagem = valor * (taxa / 100)
    total = valor + porcentagem
    return total


def diminuir(valor=0, taxa=0):
    porcentagem = valor * (taxa / 100)
    total = valor - porcentagem
    return total


def dobro(valor=0):
    total = valor * 2
    return total


def metade(valor=0):
    total = valor / 2
    return total


def moeda(valor=0, moeda='R$'):
    convertido = f'{moeda} {valor:.2f}'.replace('.', ',')
    return convertido

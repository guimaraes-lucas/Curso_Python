def aumentar(valor, taxa):
    porcentagem = valor * (taxa / 100)
    total = valor + porcentagem
    return total


def diminuir(valor, taxa):
    porcentagem = valor * (taxa / 100)
    total = valor - porcentagem
    return total


def dobro(valor):
    total = valor * 2
    return total


def metade(valor):
    total = valor / 2
    return total

"""
    Crie um programa que tenha uma FUNÇÃO FATORIAL() que receba dois parâmetros: o primeiro que indique o NÚMERO a
calcular e o outro chamado SHOW, que será um valor LÓGICO (OPCIONAL) indicando se será mostrado ou não na tela o
processo de cálculo do fatorial.
"""


def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número
    :param num: O número que será calculado
    :param show: Define se o cálculo será mostrado ou só o resultado
    :return: mostra o resultado
    """
    total = 1
    for contador in range(num, 0, -1):
        if show == True:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        total *= contador

    return total


print(fatorial(5, show=True))
print(fatorial(5))
"""
    Crie um programa que tenha a FUNÇÃO LEIAINT(), que vai funcionar de forma semelhante à função INPUT() do Python, só
que fazendo a VALIDAÇÃO para aceitar apenas um valor númerico:
        Ex: leiaInt('Digite um n')
"""


def leiaInt(pergunta):
    resposta = str(input(pergunta))

    while True:
        if resposta.isnumeric():
            print(f'O número digitado foi {resposta}')
            break
        else:
            print('\033[1:31mERRO: Digite um número inteiro válido\033[m')
            resposta = str(input(pergunta))
    return resposta

leiaInt('Digite um número: ')
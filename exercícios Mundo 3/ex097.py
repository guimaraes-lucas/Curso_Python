"""
    Faça um programa que tenha uma FUNÇÃO chamada ESCREVA(), que receba um texto qualquer como PARÂMETRO e mostre uma
mensagem com tamanho adaptável.
"""


def escreva(msg):
    print(f'-'*len(msg))
    print(msg)
    print(f'-'*len(msg))


mensagem = str(input('Escreva uma mensagem: '))
escreva(mensagem)


"""
def escreva(msg):
    tam = len(msg)+4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    
escreva('Gustavo Guanabara')
"""
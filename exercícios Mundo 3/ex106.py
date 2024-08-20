"""
    Faça um MINI-SISTEMA que utilize o INTERACTIVE HELP do PYTHON. O usuário vai digitar o COMANDO e o MANUAL vai
aparecer. Quando o usuário digitar a palavra 'FIM', o programa se ENCERRARÁ.
            OBS: Use CORES
"""
cores = (
    '\033[m',               # Cor 0
    '\033[1;30;41m',        # Cor 1 - Vermelho
    '\033[1;30;42m',        # Cor 2 - Verde
    '\033[1;30;44m',        # Cor 3 - Azul
    '\033[7;40m'            # Cor 4 - Branco
);


def ajuda(termo):
    titulo(f'Acessando o manual do comando \'{termo}\'', 3)

    print(cores[4])
    help(termo)
    print(cores[0])

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(cores[cor],end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(cores[0],end='')


# Programa Principal
titulo('SISTEMA DE AJUDA PyHELP', 2)
while True:
    termo = str(input('Função ou biblioteca > '))
    if termo.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    else:
        print(ajuda(termo))
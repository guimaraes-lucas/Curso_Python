def leiaDinheiro(entrada):
    valor = str(input(entrada)).replace(',', '.').strip()

    while True:
        if valor.isalpha() or valor == '':
            print(f'\033[1:31mERRO: "{valor}" é um valor inválido.\033[m')
            valor = str(input(entrada)).replace(',', '.')
        else:
            return float(valor)


def leiaInt(pergunta):
    while True:
        try:
            resposta = int(input(pergunta))
        except (TypeError, ValueError):
            print('\033[1:31mERRO: Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1:31mPROGRAMA FINALIZADO PELO USUÁRIO\033[m')
            return 0
        else:
            return resposta


def leiaFloat(pergunta):
    while True:
        try:
            resposta = float(input(pergunta))
        except (TypeError, ValueError):
            print('\033[1:31mERRO: Digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1:31mPROGRAMA FINALIZADO PELO USUÁRIO\033[m')
            return 0
        else:
            return resposta

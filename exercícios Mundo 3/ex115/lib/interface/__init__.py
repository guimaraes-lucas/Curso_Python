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


def linha(tamanho=42):
    return '-'*tamanho


def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())


def menu(lista):
    c = 1
    for item in lista:
        print(f'\033[1:33m{c}\033[m - \033[1:34m{item}\033[m')
        c += 1
    print(linha())
    opcao = leiaInt('\033[32mSua opção: \033[m')
    return opcao

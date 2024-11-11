def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'\033[1:31mHouve um ERRO na criação do arquivo\033[m')
    else:
        print(f'\033[1:32mArquivo {nome} criado com sucesso\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'\033[1:31mERRO ao ler o arquivo.')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'\033[1:31mHouve um ERRO na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'\033[1:31mHouve um ERRO ao escrever os dados\033[m')
        else:
            print(f'\033[1:32mNovo registro de {nome} adicionado\033[m')
            a.close()

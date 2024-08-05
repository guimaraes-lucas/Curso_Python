def lin():
    print('-'*30)


lin()
print('Olá Mundo')
lin()


def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)


mensagem('Olá mundo 1!')


def soma(x, y):
    z = x + y
    print(z)


soma(2, 1)
soma(1, 1)
soma(5, 7)


# Desempacotador
def contador(*num):
    print(len(num))


contador(5,2,5,3,44)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1,2,3,4,5,6]
dobra(valores)
print(valores)


help(print)             # Mostra uma explicação do termo em questão
print(print.__doc__)    # Abre a documentação do termo em questão


#Criando DocStrings
def contar(inicio, fim, passo):
    """
    :param inicio: É o início da contagem
    :param fim: É o fim da contagem
    :param passo: É o passo da contagem
    :return: Não tem retorno
    """
    while inicio <= fim:
        print(f'{inicio} ', end='')
        inicio += passo
    print('FIM!')

help(contar)

contar(2,10,2)


# Parâmetros Opcionais
def somar(a,b,c=0):
    s = a+b+c
    print(f'A soma vale {s}')

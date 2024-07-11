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

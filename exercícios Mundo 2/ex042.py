# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# -Equilátero: todos os lados iguais    -Isósceles: dois lados iguais   -Escaleno: todos os lados diferentes.

a = float(input('Digite o tamanho do primeiro lado: '))
b = float(input('Digite o tamanho do segundo lado: '))
c = float(input('Digite o tamanho do terceiro lado: '))

if a < b + c and b < a + c and c < a + b:
    print('É possível criar um triângulo')

    if a == b == c == a:
        print('Esse é um triângulo EQUILÁTERO')
    elif a != b != c != a:
        print('Esse é um triângulo ESCALENO')
    else:
        print('Este é um triângulo ISÓSCELES')
else:
    print('Não é possível formar um triângulo')

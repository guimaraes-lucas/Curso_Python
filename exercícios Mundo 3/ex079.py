"""
    Crie um programa onde o usuário passa digitar vários VALORES NUMÉRICOS e cadastre-os em uma LISTA. Caso o número já
exista lá dentro, ele NÂO SERÁ ADICIONADO. No final, serão exibidos todos os VALORES ÚNICOS digitados, em ORDEM CRESCENTE
"""

lista = []

num = int(input('Digite um número: '))
lista.append(num)

while True:
    continuar = str(input('Deseja continuar? [S/N] '))

    if continuar in 'Ss':
        num = int(input('Digite um número: '))
        if num not in lista:
            lista.append(num)
        else:
            print('Valor já adicionado')
    else:
        lista.sort()
        break

print(lista)

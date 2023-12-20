"""
    Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma LISTA. Depois disso, mostre:
        A) QUANTOS números foram digitados.
        B) A lista de valores, ordenada de forma DECRESCENTE.
        C) Se o valor 5 foi digitado está ou não na LISTA.
"""

lista = []

num = int(input('Digite um número: '))
lista.append(num)

while True:
    continuar = str(input('Deseja continuar? [S/N] '))

    if continuar in 'Ss':
        num = int(input('Digite um número: '))
        lista.append(num)
    else:
        break
lista.sort(reverse=True)

print(f'A lista possui {len(lista)} elementos.')
print(f'A lista em ordem decrescente fica: {lista}')

if 5 in lista:
    print('A lista possui o número 5.')
else:
    print('A lista não possui o número 5')


"""
    lista.append(int(input('Digite um número')))
    continuar = str(input('Quer continuar?: [S/N] ))
    if continuar in 'Nn':
        break
"""
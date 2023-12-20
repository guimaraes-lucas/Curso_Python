"""
    Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma LISTA. Depois disso, crie DUAS LISTAS EXTRAS que vão
conter apenas os valores PARES e os valores ÍMPARES digitados, respectivamente. Ao final, mostre o conteúdo das TRÊS
LISTAS geradas.
"""

lista = []
par = []
impar = []

while True:
    num = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N] '))

    if continuar in 'Ss':
        lista.append(num)
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    else:
        lista.append(num)
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
        break

print(f'A lista completa é: {lista}')
print(f'Os números pares da lista são {par}')
print(f'Os números ímpares da lista são {impar}')


"""
num = []
pares = []
impares = []

while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar?: [S/N] ))
    
    if resp in 'Nn':
    break

for indice, valor in enumerate(num):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 0:
        impares.append(valor)
"""
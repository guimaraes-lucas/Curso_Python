# Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO.

num = int(input('Digite um número: '))
divisiveis = 0

for impar in range(1, num + 1):
    if num % impar == 0:
        print('\033[32m {} \033[m'.format(impar), end=' ')
        divisiveis += 1
    else:
        print('\033[31m {} \033[m'.format(impar), end=' ')

print('\n O número {} foi dividido {} vezes'.format(num, divisiveis))
if divisiveis == 2:
    print(' É um número primo')
else:
    print(' Não é um número primo')

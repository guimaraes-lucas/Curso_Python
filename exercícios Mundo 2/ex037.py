# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a 'base de conversão'
# 1 para binário    2 para octal    3 para hexadecimal
num = int(input('Escolha um número inteiro qualquer: '))

print('Bases de Conversão disponíveis')
print('[ 1 ] Binário')
print('[ 2 ] Octal')
print('[ 3 ] Hexadecimal')

base = int(input('Qual vai ser a base?: '))

if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')

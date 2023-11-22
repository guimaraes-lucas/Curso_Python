"""
    Desenvolva um programa que leia QUATRO VALORES pelo TECLADO e quarde-os em uma TUPLA. No final, mostre:

    A) Quantas vezes apareceu o valor 9                     C) Quais foram os números PARES.
    B) Em que posição foi digitado o primeiro valor 3.
"""

nums = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
        int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))

print(f'Você digitou os valores {nums}')
print(f'O valor 9 apareceu {nums.count(9)} vezes')

if 3 in nums:
    print(f'O valor 3 apareceu na {nums.index(3)+1}° posição')
else:
    print('O valor 3 não apareceu.')

print('Os valores pares digitados foram ', end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')

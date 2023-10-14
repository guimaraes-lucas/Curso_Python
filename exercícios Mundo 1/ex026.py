# Faça um programa que leia uma frase pelo teclado e mostre:
#   => Quantas vezes aparece a letra "A"
#   => Em que posição ela aparece a primeira vez
#   => Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()

qva = frase.upper().count('A')
pa = frase.upper().find('A')
ua = frase.upper().rfind('A')

print('A letra "A" aparece {} vezes'.format(qva))
print('A primeira vez que ela aparece é na {} posição'.format(pa + 1))
print('A última vez que ela aparece é na {} posição'.format(ua + 1))

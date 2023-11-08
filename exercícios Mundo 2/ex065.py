# Crie um programa que leia VÁRIOS NÚMEROS pelo teclado. No final da execução, mostre a MÉDIA ENTRE TODOS os valores e
# qual foi o MAIOR e MENOR valores lidos. O programa deve perguntar ao usuário se ele quer ou não CONTINUAR a digitar
# valores.

resposta = 'S'

contagem = total = maior = menor = 0

while resposta in 'Ss':
    num = int(input('Digite um número: '))

    total += num
    contagem += 1

    if contagem == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < num:
            menor = num

    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

media = total / contagem

print('Você digitou {} números e a média foi de {}'.format(contagem, media))
print('O maior número foi {} e o menor número foi {}'.format(maior, menor))

# Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS. Um de cada vez, para cada valor digitado pelo usuário.
# O programa será INTERROMPIDO quando o número solicitado for NEGATIVO.

while True:
    num = int(input('Digite um valor: '))

    print('-'*30)

    if num < 0:
        break
    else:
        for contagem in range(0, 11):
            print(f'{num} x {contagem} = {num * contagem}')

    print('-' * 30)
    
print('Programa TABUADA encerrado')
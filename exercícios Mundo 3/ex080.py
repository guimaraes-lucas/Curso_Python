"""
    Crie um programa onde o usuário possa digitar cinco VALORES NUMÉRICOS e cadastre-os em uma LISTA, JÁ NA POSIÇÃO
CORRETA de inserção (sem usar o SORT()). No final, mostre a LISTA ORDENADA na tela.
"""

lista = []

for contagem in range(0, 5):
    num = int(input('Insira um valor: '))
    if contagem == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1

print(lista)

"""
    Crie um programa que tenha uma TUPLA com VÁRIAS PALAVRAS (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas VOGAIS.
"""

palavras = ('Amor', 'Sorvete', 'Jogo', 'Paralelepipedo', 'Computador')

"""
for vogais in range(0, len(palavras)):

    print(f'Na palavra {palavras[vogais]}: ')
    print(f'A letra A aparece: {palavras[vogais].upper().count("A")} vezes;')
    print(f'A letra E aparece: {palavras[vogais].upper().count("E")} vezes;')
    print(f'A letra I aparece: {palavras[vogais].upper().count("I")} vezes;')
    print(f'A letra O aparece: {palavras[vogais].upper().count("O")} vezes;')
    print(f'A letra U aparece: {palavras[vogais].upper().count("U")} vezes')
    print('-'*40)
"""

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
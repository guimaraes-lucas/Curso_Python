# Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por EXTENSO.

extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))

    if num < 0 or num > 20:
        break
    else:
        print(f'O número escolhido foi {extenso[num]}')

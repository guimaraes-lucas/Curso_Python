# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome deles e escrevendo o nome escolhido.
import random

a1 = str(input('Qual o primeiro aluno?: '))
a2 = str(input('Qual o segundo aluno?: '))
a3 = str(input('Qual o terceiro aluno?: '))
a4 = str(input('Qual o quarto aluno?: '))

lista = [a1, a2, a3, a4]

print('O aluno escolhido é {}'.format(random.choice(lista)))

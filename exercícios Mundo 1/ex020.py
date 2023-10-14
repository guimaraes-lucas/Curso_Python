# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

a1 = str(input('Qual o aluno?: '))
a2 = str(input('Qual o aluno?: '))
a3 = str(input('Qual o aluno?: '))
a4 = str(input('Qual o aluno?: '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print('A ordem de apresentação é: {}'.format(lista))

"""
    Crie um programa que leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA. No final, mostre
um BOLETIM contendo a MÉDIA de cada um e permita que o usuário possa mostrar as NOTAS de cada aluno individualmente.
"""
classe = []
aluno = []

while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('1° nota: ')))
    aluno.append(float(input('2° nota: ')))
    classe.append(aluno[:])

    aluno.clear()

    continuar = str(input('Deseja adicionar mais alunos? [S/N} '))
    if continuar in 'Nn':
        break

print('-=-'*30)
print('No. Nome      Média')
print('--'*20)

for indice, aluno in enumerate(classe):
    print(f'{indice}   {aluno[0]}     {(aluno[1] + aluno[2])/2}')
print('--'*20)

while True:
    verificar = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if verificar == 999:
        break
    else:
        print(f'Notas do {classe[verificar][0]} são [{classe[verificar][1]}, {classe[verificar][2]}]')
        print('--' * 20)


"""
ficha = list()

while True: 
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('_' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): ')
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
"""
"""
    Faça um programa que leia NOME e MÉDIA de um aluno, quardando também a SITUAÇÃO em um DICIONÁRIO. No final mostre o
conteúdo da estrutura na tela.
"""

aluno = {'nome': str(input('Nome: '))}
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

print('-=-'*30)
print(f'- Nome é igual a {aluno["nome"]}')
print(f'- Média é igual a {aluno["media"]}')
if aluno['media'] >= 7:
    print(f'- Situação é igual a Aprovado')
elif 5 <= aluno['media'] < 7:
    print(f'- Situação é igual a Recuperação')
else:
    print(f'- Situação é igual a Reprovado')

"""
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
    
for keys, values in aluno.items():
    print(f'  - {keys} é igual a {values}')
"""

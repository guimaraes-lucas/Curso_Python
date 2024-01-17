"""
    Faça um programa que leia o NOME e PESO de VÁRIAS PESSOAS, quardando tudo em uma LISTA. No final, mostre:
        A) QUANTAS pessoas foram cadastradas
        B) Uma listagem com as pessoas mais PESADAS
        C) Uma listagem com as pessoas mais LEVES
"""

pessoas = []
dados = []
contagem = 0

while True:
    # Introdução dos dados
    nome = str(input('Digite um nome: '))
    peso = int(input('Digite um peso: '))

    # Adicionando nas listas
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()

    # Verificando os pesos
    if contagem == 0:
        maisPesada = peso
        maisLeve = peso
    else:
        if peso > maisPesada:
            maisPesada = peso
        if peso < maisLeve:
            maisLeve = peso

    contagem += 1
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break

print(f'Os dados foram {pessoas}')
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {maisPesada}Kg')
print(f'O menor peso foi {maisLeve}Kg')

"""
pessoas = []
dados = []
maisPesada = maisLeve = 0

while True:
    dados.append(str(input('Digite um nome: ')))
    dados.append(int(input('Digite um peso: ')))
    
    if len(pessoas) == 0:
        maisPesada = maisLeve = dados[1]
    else:
        if dados[1] > maisPesada:
            maisPesada = dados[1]
        if dados[1] < maisLeve:
            maisLeve = dados[1]
            
    pessoas.append(dados[:])
    dados.clear()
    
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
 
print(f'Os dados foram {pessoas}')
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')

print(f'O maior peso foi {maisPesada}Kg. ', end='')
for peso in pessoas:
    if peso[1] == maisPesada:
        print(f'{peso[0]}')
        
print(f'O menor peso foi {maisLeve}Kg. ', end='')
for peso in pessoas:
    if peso[1] == maisLeve:
        print(f'{peso[0]}')
"""

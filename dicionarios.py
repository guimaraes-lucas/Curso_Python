dados = {'nome':'pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'Masculino'     # Adicionar elementos
del dados['idade']              # Deleta o elemento

filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}

print(filme.values())       # Imprime somente os valores
print(filme.keys())         # Imprime somente as chaves
print(filme.items())        # Imprime ambos

for keys, values in filme.items():
    print(f'O {keys} é {values}')

locadora = [
    {'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'},
    {'titulo':'Avengers', 'ano':2012, 'diretor':'Joss Whedon'},
    {'titulo':'Matrix', 'ano':1999, 'diretor':'Wachowski'}
]

print(locadora[0]['ano'])
print(locadora[2]['titulo'])

pessoas = {'nome':'Lucas', 'sexo':'Masculino', 'idade':20}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

estado = {}
brazil = []

for contador in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brazil.append(estado.copy())
print(brazil)
for estados in brazil:
    for chaves, valores in estados.items():
        print(f'O campo {chaves} tem valor {valores}')

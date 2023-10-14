"""
carro.siga()
if carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
elif carro.direita():
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
else:
    carro.siga()
carro.para()
"""

nome = str(input('Qual é o seu nome?: '))

if nome == 'Lucas':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Jose' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Fernanda Jessica Sofia Margot':
    print('Belo nome Feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

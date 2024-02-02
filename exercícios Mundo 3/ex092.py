"""
    Crie um programa que leia NOME. ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os (com IDADE) em um DICIONÁRIO
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ANO DE CONTRATAÇÃO e o SALÁRIO. Calcule e
acrescente, além da IDADE, com quantos anos a pessoa vai se APOSEMTAR.
"""
from datetime import date

cadastro = {}

cadastro['nome'] = str(input('Nome: '))
cadastro['nascimento'] = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - cadastro['nascimento']
cadastro['ctps'] = int(input('Número da Carteira de Trabalho (0 não tem): '))

if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposentadoria'] = (cadastro['contratacao'] - cadastro['nascimento']) + 35

print('-=-'*30)

for chave, valor in cadastro.items():
    print(f'{chave} é: {valor}')

"""
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: ))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=-'*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
"""
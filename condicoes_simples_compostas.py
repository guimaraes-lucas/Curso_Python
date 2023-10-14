tempo = int(input('Quantos anos tem o seu carro?: '))

# Condição composta
if tempo <= 3:
    print('Carro novo')
else:
    print('Seu carro é velho')

print('== FIM ==')

# Condição simples
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('== FIM ==')

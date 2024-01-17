#Parte 1
lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
lanche[3] = 'Picolé'

# Inserir Elementos
lanche.append('Cookie')
lanche.insert(0, 'Cachorro Quente')

# Apagar Elementos
del lanche[3]
lanche.pop(3)
lanche.remove('Pizza')


valores = list(range(4, 11))

valores1 = [8, 2, 5, 4, 9, 3, 0]
len(valores1)
valores1.sort()
valores1.sort(reverse=True)

#Parte 2

pessoas = []
dados = ['Lucas', 20]

pessoas.append(dados[:])
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0][0])
print(pessoas[0][1])
print(pessoas[1][1])
print(pessoas[1])

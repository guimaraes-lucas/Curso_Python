# Fatiamento
frase = str('Curso em Vídeo Python')
print(frase[9])         # Seleciona uma posição do índice
print(frase[9:13])      # Seleciona o intervalo solicitado
print(frase[9:21:2])    # Seleciona o intervalo solicitado e vai alternando com base no terceiro elemento
print(frase[:5])        # Seleciona desde o começo até o intervalo solicitado Ex: 0:5
print(frase[15:])       # Seleciona do número especificado atè o final da string
print(frase[9::3])      # Seleciona do número especificado até o final da string alternando com base no 3° elemento


# Análise
print(len(frase))           # Mostra o comprimentp da string
print(frase.count('o'))     # Mostra quantas vezes o caractere selecionado aparece
print(frase.count('o', 0, 13))  # Mostra quantas vezes o caractere selecionado aparece no intervalo descrito
print(frase.find('deo'))    # Encontra a posição dos caracteres selecionados
print('Curso' in frase)     # Diz se o caractere selecionado existe na string

# Transformação
print(frase.replace('Python', 'Android'))   # Altera os caracteres da string
print(frase.upper())        # Deixa a string maiúscula
print(frase.lower())        # Deixa a string minúscula
print(frase.capitalize())   # Deixa somente o primeiro caractere maiúsculo
print(frase.title())        # Deixa o primeiro caractere de cada palavra maiúsula
print(frase.strip())        # Limpa os espaços em branco do começo e final da string
print(frase.rstrip())       # Limpa es espaços em branco à direita da string
print(frase.lstrip())       # Limpa es espaços em branco à esquerda da string

# Divisão
print(frase.split())        # Cria uma divisão baseada nos espaços da string

# Junção
print('-'.join(frase))      # Junta as strings em uma só

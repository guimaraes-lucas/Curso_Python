# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.

num = int(input('Digite um número: '))

for tabuada in range(0, 11):
    multi = num * tabuada
    print('{} x {} = {}'.format(num, tabuada, multi))

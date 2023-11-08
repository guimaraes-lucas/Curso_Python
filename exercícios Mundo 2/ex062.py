# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Qual a razão?: '))

contagem = 0

while contagem < 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contagem += 1
print('PAUSA')

cont = int(input('Quantos termos deseja adicionar?: '))

while cont != 0:
    for x in range(0, cont):
        print('{} -> '.format(termo), end='')
        termo += razao
        contagem += 1
    print('PAUSA')
    cont = int(input('Quantos termos deseja adicionar?: '))

print('')
print('Ao total foram {} termos'.format(contagem))
print('Programa finalizado')

"""
    Crie um programa onde o usuário digite uma EXPRESSÃO qualquer que use PARÊNTESES. Seu aplicativo deverá analisar se
a expressão passada está com os parênteses abertos e fechados na ORDEM CORRETA.
"""

expressao = str(input('Digite uma expressão: ')).strip()

print(f'A expressão digitada foi {expressao}')

if expressao.count('(') == expressao.count(')'):
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida')


"""
expr = str(input('Digite a expressão: '))
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')

"""
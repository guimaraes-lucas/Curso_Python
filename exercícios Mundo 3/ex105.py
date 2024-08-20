"""
    Faça um programa que tenha uma FUNÇÃO NOTAS() que pode receber várias notas de alunos e vai retornar um DICIONÁRIO
com as seguintes informações:
        -> Quantidade de notas      -> A maior nota         -> A situação (opcional)
        -> A menor nota             -> A média da turma     * Adicione também as DOCSTRINGS
"""


def notas(*num, situacao=False):
    """
    -> Função para analisar as notas de uma turma
    :param num: Notas dos Alunos
    :param situacao: Se a turma foi aprovada ou não
    :return: Retorna as estatísticas da turma
    """

    nota = {'Total': 0, 'Maior': 0, 'Menor': 0, 'Média': 0,}
    total = maior = menor = 0

    for soma in num:
        total += soma
    nota["Total"] = total
    nota["Média"] = total / len(num)

    if situacao:
        if nota["Média"] >= 6:
            nota["Situação"] = 'Aprovado'
        else:
            nota["Situação"] = 'Reprovado'

    for m in num:
        if m > maior:
            maior = m
    nota["Maior"] = maior

    for m in num:
        if menor == 0:
            menor = m
        if m < menor:
            menor = m
    nota["Menor"] = menor
    return nota


resp1 = notas(5,3,2,2)
resp2 = notas(4,2,1,1, situacao=True)
resp3 = notas(10,10,10,10, situacao=True)

print(resp1)
print(resp2)
print(resp3)
help(notas)
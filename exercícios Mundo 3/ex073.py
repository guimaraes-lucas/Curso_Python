"""
    Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados na Tabela do CAMPEONATO BRASILEIRO DE FUTEBOL, na ordem de
colocação. Depois mostre:

    A) Os 5 PRIMEIROS               C) Times em ORDEM ALFABÉTICA.
    B) Os ÚLTIMOS 4 colocados       D) Em que posição está o time do CORINTHIANS
"""

times = ('Palmeiras', 'Botafogp', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Flamengo', 'Athlético-PR',
         'Fluminense', 'Cuiabá', 'São Paulo', 'Corinthians', 'Fortaleza', 'Internacipnal', 'Santos',
         'Vasco da Gama', 'Cruzeiro', 'Bahia', 'Goiás', 'Coritiba', 'América-MG')

print('-=-'*20)
print(f'Lista de times do Brasileirão: {times}')
print('-=-'*20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-'*20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=-'*20)
print(f'Times em Ordem Alfabética: {sorted(times)}')
print('-=-'*20)
print(f'O Corinthians está na {times.index("Corinthians")+1}° posição')

"""
    Dentro do pacote utilidadesCeV que criamos no DESAFIO 111, temos um MÓDULO chamado DADO. Crie uma função chamada
LEAIDINHEIRO() que seja capaz de funcionar como a função INPUT(), mas com uma VALIDAÇÃO DE DADOS para aceitar apenas
valores que sejam MONETÁRIOS.
"""

from utilidadesCeV import dados
from utilidadesCeV import moeda

valor = dados.leiaDinheiro('Digite o valor: R$ ') 
moeda.resumo(valor, 80, 20)
 
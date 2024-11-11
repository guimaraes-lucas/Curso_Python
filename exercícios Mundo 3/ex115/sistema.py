"""
    Crie um pequeno SISTEMA MODULARIZADO que permita cadastrar pessoas pelo seu NOME e IDADE em um arquivo de texto
simples.
    O sistema só vai ter 2 OPÇÕES: CADASTRAR uma nova pessoa e LISTAR todas as pessoas cadastradas.
"""
from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'cadastroPessoas.txt'


if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
        cabecalho('SISTEMA DE CADASTRO')
        resposta = menu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Fechar sistema'])
        if resposta == 1:
            sleep(1)
            cabecalho('PESSOAS CADASTRADAS')
            lerArquivo(arquivo)
        elif resposta == 2:
            sleep(1)
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaInt('Idade: ')
            cadastrar(arquivo, nome, idade)
        elif resposta == 3:
            cabecalho('\033[1:35mSaindo do sistema... Até logo!\033[m')
            sleep(1)
            break
        else:
            print('\033[1:31mEssa opção não existe\033[m')
            sleep(2)

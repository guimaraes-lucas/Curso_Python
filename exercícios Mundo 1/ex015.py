"""
 Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado
 """

d = int(input('Por quantos dias o carro foi alugado?: '))
km = float(input('Quantos quilômetros foram percorridos?: '))
t = (d * 60) + (km * 0.15)

print('O carro foi alugado por {} dias e percorreu {}km, o valor total é {:.2f}R$'.format(d, km, t))

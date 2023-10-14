"""
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre seu status, de acordo com
a tabela abaixo:
        -Abaixo de 18.5: Abaixo do peso     -30 até 40: Obesidade
        -Entre 18.5 e 25: Peso ideal        -Acima de 40: Obesidade mórbida
        -25 até 30: Sobrepeso
"""

peso = float(input('Qual o seu peso?: (KG) '))
altura = float(input('Qual a sua altura?: (M) '))

imc = peso / (altura ** 2)
print('O imc dessa pessoa é {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc <= 25:
    print('Você está no PESO IDEAL')
elif 25 < imc <= 30:
    print('Você está com SOBREPESO')
elif 30 < imc <= 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA')

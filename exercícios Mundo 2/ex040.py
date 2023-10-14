# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# -Média abaixo de 5.0: Reprovado   -Média entre 5.0 e 6.9: Recuperação     -Média 7.0 ou superior: Aprovado

print('='*20)
print('Calculadora da Média')
print('='*20)

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Sua média foi {}. Parabéns você foi Aprovado!!!'.format(media))
elif 5 <= media <= 6.9:
    print('Sua média foi {}, Você está de Recuperação'.format(media))
elif media < 5:
    print('Sua média foi {}. Infelizmente você foi Reprovado!'.format(media))

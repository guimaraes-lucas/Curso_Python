def leiaDinheiro(entrada):
    valor = str(input(entrada)).replace(',', '.').strip()

    while True:
        if valor.isalpha() or valor == '':
            print(f'\033[1:31mERRO: "{valor}" é um valor inválido.\033[m')
            valor = str(input(entrada)).replace(',', '.')
        else:
            return float(valor)
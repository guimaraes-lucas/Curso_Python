# import biblioteca => Importa toda a biblioteca
# from biblioteca import livro => Importa somente um item da biblioteca

# ================= MATH ===================
# ceil => Arredonda pra cima
# floor => Arredonda para baixo
# trunc -> Elimina os números após a vírgula
# pow => Têm a mesma função do **
# sqrt => Calcula a raiz quadrada
# factorial => Calcula o fatorial

# ============================= PRÁTICA ========================================
#import math
from math import sqrt, ceil
num = int(input('Escolha um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))

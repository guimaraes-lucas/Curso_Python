# \033[style : text : background m

"""
        Style               Text                Background
    0 = None            30 = Branco         40 = Branco
    1 = Bold            31 = Vermelho       41 = Vermelho
    4 = Underline       32 = Verde          42 = Verde
    7 = Negative        33 = Amarelo        43 = Amarelo
                        34 = Azul           44 = Azul
                        35 = Magenta        45 = Magenta
                        36 = Ciano          46 = Ciano
                        37 = Cinza          47 = Cinza
"""


print('\033[1:30:41mOlá Mundo!\033[m')
print('\033[4:33:46mOlá Mundo!\033[m')
print('\033[1:35:43mOlá Mundo!\033[m')
print('\033[30:42mOlá Mundo!\033[m')
print('\033[mOlá Mundo!\033[m')
print('\033[7:30mOlá Mundo!\033[m')

"""
    Crie um programa onde o usuário possa digitar SETE VALORES NÚMERICOS e cadastre-os em uma LISTA ÚNICA que mantenha
separados os valores PARES e ÍMPARES. No final, mostre os valores pares e ímpares em ordem CRESCENTE.
"""

nums = [[], []]

for pos in range(1, 8):
    num = int(input(f'Digite o {pos}° número: '))

    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)

nums[0].sort()
nums[1].sort()

print(f'Os números pares foram {nums[0]}')
print(f'Os números ímpares foram {nums[1]}')

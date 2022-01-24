import math
import random

max = 200
min = 0

for i in range(1,10):
    conta = (max + min) /2
    conta = math.trunc(conta)
    resp = input(f"Voce tem {conta} anos? (digite mais menos ou sim)\n-> ")

    if resp == 'sim':
        print("boa")
        break
    elif resp == 'mais':
        min = conta
    elif resp == 'menos':
        max = conta
    else:
        print("Digite uma resposta valida!")
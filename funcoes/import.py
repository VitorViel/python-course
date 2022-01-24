import math
import random
from random import choice

#sqrt(x) mostra a raiz qadrada do numero
#ceil(x) arredonda para mais o valor do numero para um numero inteiro
#trunc(x) arredonda para menos o valor do numero para um numero inteiro
#factorial(x) mostra o numero fatorado
#choice(x) escolhe um valor aleatorio da minha str ou list

print(math.sqrt(9))

#impar ou par

escolha = str(input("Impar ou par? (Digite impar ou par!)\n ->")).lower()

if escolha == 'impar' or escolha == 'par':
    valor1 = int(input(f"Muito bem! você escolheu {escolha}! Agora digite o primeiro valor escolhido\n-> "))
    valor2 = random.randint(0,10)
    resultado = valor1 + valor2
    print(f"Você escolheu {valor1}, eu escolho {valor2}, a soma é {resultado}. Portanto...")

    if escolha == 'impar':
        if resultado % 2 == 0:
            print("Voce perdeu! kkkk achei fácil")
        else:
            print("Voce ganhou... parabens :(")

    elif escolha == 'par':
        if resultado % 2 == 0:
            print("Voce ganhou... parabens :(")
        else:
            print("Voce perdeu! kkkk achei fácil")

    else:
            print("Digite uma das opções disponiveis")

else:
    print("Digite uma das 2 opções!")

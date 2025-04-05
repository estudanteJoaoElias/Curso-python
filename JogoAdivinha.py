
import random

def jogo_adivinhacao():
    # Gera o número secreto
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    print(f"Você tem {max_tentativas} tentativas para acertar.")

    while tentativas < max_tentativas:
        # Solicita um palpite ao jogador
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativa(s).")
            break

    if tentativas == max_tentativas and palpite != numero_secreto:
        print(f"Você usou todas as suas {max_tentativas} tentativas.")
        print(f"O número secreto era {numero_secreto}.")
    print("Fim do jogo!")

# Inicia o jogo
jogo_adivinhacao()

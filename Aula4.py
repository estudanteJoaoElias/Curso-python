
#Exercicio 1, 2
num1 = float(input("Digite um numero: ")) #Para somar apenas numeros inteiros trocar float por int
num2 = float(input("Digite outro numero: "))

print(f"Soma:", num1 + num2)
print(f"Subtração:", num1 - num2)
print(f"Divisão:", num1 /num2)
print(f"Multiplicação:",num1 * num2)

#Exercicio 3
nome = input("Digite seu nome: ")
print(f"Boas vindas", nome)

#Exercicio 4
frase = "Aprender python é divertido"

print ((frase +"\n") *3)
print(len(frase))

#Exercicio 5
idade = int(input("Digite sua idade: "))

if idade >= 18 :
    print("Voce é maior de idade")
else:
    print("Voce é menor de idade")

#Exercicio sobre listas 1
lista = [10, 20, 30, 40]
soma = sum(lista)
print(f"A soma da lista é: {soma}")

#Exercicio 2
nomes = ['Joao', 'Carlos', 'Pedro', 'Mateus']
print(nomes)
nomes.insert(2, 'leonardo')
print(nomes)

#Exercicio 3
frutas = ['uva', 'pera', 'maça', 'laranja']
print(frutas)
frutas.pop()
print(frutas)

#Desafio
import random

# Gerar um número aleatório entre 1 e 20
numero_secreto = random.randint(1, 20)
tentativa = 0

print("Bem-vindo ao jogo! Tente adivinhar o número entre 1 e 20.")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativa += 1
    if palpite < numero_secreto:
        print("O número é maior!")
    elif palpite > numero_secreto:
        print("O número é menor!")
    else:
        print(f"Parabéns! Você acertou o número em {tentativa} tentativa(s).")
        break



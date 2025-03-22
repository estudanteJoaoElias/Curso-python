def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def dividir(n1, n2):
    if n2 == 0:
        return "Erro! Divisão por zero."
    return n1 / n2

def multiplicar(n1, n2):
    return n1 * n2

print("Selecione a operação:")
print("1. Somar")
print("2. Subtrair")
print("3. Dividir")
print("4. Multiplicar")

while True:
    try:
        opcao = int(input("Digite o número da operação desejada: "))
        if opcao in (1, 2, 3, 4):
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número.")

while True:
    try:
        num2 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Entrada inválida. Digite um número.")

if opcao == 1:
    resultado = somar(num1, num2)
    operacao = "+"
elif opcao == 2:
    resultado = subtrair(num1, num2)
    operacao = "-"
elif opcao == 3:
    resultado = dividir(num1, num2)
    operacao = "/"
elif opcao == 4:
    resultado = multiplicar(num1, num2)
    operacao = "*"

if isinstance(resultado, str):  # Verifica se ocorreu um erro (divisão por zero)
    print(resultado)
else:
    print(f"{num1} {operacao} {num2} = {resultado}")
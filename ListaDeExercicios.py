#Imprimir Tipos de Variáveis
inteiros = 1
print(type(inteiros))

floats = 10.5
print(type(floats))

strings = "Joao"
print(type(strings))

booleans = True
print(type(booleans))

#Conversão de Tipos
numero = "10"
numero = int(numero)
print("converter numero inteiro", numero)
print(type(numero))

decimal = 20.25
decimal = str(decimal)
print("converter numero decimal", decimal)
print(type(decimal))

#Operações com Inteiros e Floats
numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))
print(numero1+numero2)
print(numero1-numero2)
print(numero1*numero2)
print(numero1/numero2)
print(numero1 % numero2)

#Manipulação de Strings
frase = input("Digite uma frase: ")
fraseMaiuscula = frase.upper()
fraseMinuscula = frase.lower()
frasePri = frase.capitalize()

print(frasePri)
print(fraseMinuscula)
print(fraseMaiuscula)

#Booleanos e Operadores Lógicos
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro numero: "))

if n1 >0 :
    print(f"O numero {n1} é positivo.")
elif n1 < 0:
    print(f"O numero {n1} é negativo")
else:
    print("Entao o numero é zero")

if n2 >0 :
    print(f"O numero {n2} é positivo.")
elif n2 < 0:
    print(f"O numero {n2} é negativo")
else:
    print("Entao o numero é zero")

#Entrada de Dados
Nome = input("Digite seu nome: ")
Idade = int(input("Digite sua idade:"))

print(f"Nome: {Nome}\nIdade: {Idade}")

#Contagem de caracteres
caracteres = input("Digite uma palavra: ")
print(len(caracteres))

#Lista de frutas
List = []

for i in range(5):
    fruta = input(f"digite o nome da fruta {i+1}:")
    List.append(fruta)

print("lista de frutas", List)

#Manipulação de Listas
del List[1]
print("lista de frutas removendo o indice 1:",List)

#Criação de tupla
tupla = (1, 2, 3, 4, 5)

for numero in tupla :
    print(numero)

#Criação dicionario
dicionario = {
    "Joao": 25,
    "marcos": 30,
    "carlos": 22
}
print("dicionario antes das alteraçoes:", dicionario)
#Adicionar ao dicionario existente
dicionario['marcelo'] = 28
print("Adicionando ao dicionario existente:", dicionario)

#excluindpo do dicionario existente
del dicionario['marcos']
print("removendo do dicionario existente:", dicionario)

for chave, valor in dicionario.items():
    print(f'Nome: `{chave}, idade:{valor}')

#Criação de set
set= {1,2,'Joao',3, 4}

for campo in set:
    print(campo)


#Operadores de Comparação
nu1 = float(input("Digite o primeiro numero:"))
nu2 = float(input("digite o segundo numero: "))

if nu1 == nu2 :
    print("os numeros sao iguais")
else:
    print("os numeros sao diferentes")
    if nu1 > nu2:
        print("O primeiro numero é maior que o segundo")
    else:
        print("O primeiro numero é menor que o segundo")

#Operadores de atribuição
n = 10
print(n)
n += 5 #soma ao valor de 10 mais 5
print(n)
n -= 5 #Subtrai ao valor de 10 menos 5
print(n)
n *= 5 #multiplica o valor de 10 vezes 5
print(n)
n /= 5 #divide o valor de 10 por 5
print(n)
n %= 3 #calcula o modulo de 10 por 3
print(n)

#Operador de identidade
a = [1,2,3]
b = a
c = [1,2,3]

print(a is b)
print(a is c)

lista = [1,2,3,4,5]

elemento = int(input("DIgite um numero para verificar se está na lista: "))

if elemento in lista:
    print(f"O numero {elemento} está na na lista")
else:
    print(f"O numero {elemento} nao está na lista")

















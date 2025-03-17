# Inicializar uma lista para armazenar as frutas
frutas = []

# Receber as frutas pelo teclado
for i in range(5):
    fruta = input(f"Digite o nome da fruta {i+1}: ")
    frutas.append(fruta)

# Imprimir a lista de frutas
print("Lista de frutas:", frutas)
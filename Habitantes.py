Habitantes = int(input("Digite o numero de habitantes de sua cidade: "))

if Habitantes >= 100000000:
  print("Megacidade")

elif Habitantes > 100000:
    print("Cidade Grande")

else:
    print("cidade pequena")
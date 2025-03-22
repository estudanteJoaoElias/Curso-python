#usando for, range
idades = []

for i in range (5):
    idade = int(input(f"digite a idade {i + 1}: ")) #f permite que insira variaveis ou expressoes dentro de uma string
    idades.append(idade) #adiciona idade no final da lista

media = sum(idades) / 5

print (media)

#usando o while
idades = []
i = 0

while len(idades) < 5:
  idade = int(input(f"Digite idade{i+1}: "))
  idades.append(idade)
  i = i+1

media = sum(idades) / 5

print(media)




#versao usando funçoes sum e lem
idade = [25,30,22,28,35]
idadeMedia = sum(idade)/len(idade)
print(idadeMedia)





#versao otimizada em uma linha apenas
print(sum([25,30,22,28,35]) / 5)





#Aplicando manualmente
listaIdades = [25,30,22,28,35]
somaIdades = 0
quantidadeIdades= 0

for indice, idade in enumerate(listaIdades):
    print(f"indice {indice} {idade}")
    somaIdades += idade
    quantidadeIdades +=1
print(somaIdades,quantidadeIdades)
print("idade média é:", somaIdades/quantidadeIdades)

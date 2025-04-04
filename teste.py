def velocidade (espaço, tempo):
    v = espaço / tempo
    return v

fatorMultiplicacao = 2
print(velocidade(100,10) * fatorMultiplicacao)

def dados (nome, idade=None):
    print(f"nome: {nome}")
    if (idade is not None):
        print(f"idade: {idade}")
    else:
        print("idade nao informada!")

dados ("marcelo", 20)
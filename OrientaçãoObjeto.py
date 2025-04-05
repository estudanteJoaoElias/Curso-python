class Pessoa:
  def __init__(self,nome,idade):
    self.nome = nome
    self.idade = idade

  def comprimentar(self):
      return f"Olá meu nome é {self.nome}"


pessoa01 = Pessoa("Joao", 20)
print(pessoa01.nome, pessoa01.idade)
print(pessoa01.comprimentar())

pessoa02 = Pessoa("Leoanardo", 30)
print(pessoa02.nome, pessoa02.idade)
print(pessoa02.comprimentar())

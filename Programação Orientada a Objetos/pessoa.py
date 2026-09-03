#Exercicio 1 (Orientação a Objetos)

class Pessoa:

    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


pessoa1 = Pessoa("Ana", 27)
pessoa2 = Pessoa("Pedro", 40)

pessoa1.apresentar()
pessoa2.apresentar()
# Exercicio 3 (Orientação a Objetos)

class Veiculo:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_dados(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}")


class Carro(Veiculo):

    pass


class Moto(Veiculo):

    pass


carro2 = Carro("Honda", "City", 2016)

moto0 = Moto("BMW", "1200", 2026)

carro2.exibir_dados()
moto0.exibir_dados()
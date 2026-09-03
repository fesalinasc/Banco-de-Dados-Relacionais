#Exercicio 2 (Orientação a Objetos)

class Carro:

    def __init__(self):
        self.__combustivel = 0 

    def abastecer (self, litros):
        self.__combustivel += litros

    def dirigir (self, distancia):
        litros_gastos = distancia/10
        self.__combustivel -= litros_gastos

    def ver_combustivel(self):
        print(f"Combustivel restante: {self.__combustivel} litros")


carro1 = Carro()
carro1.abastecer(20)
carro1.dirigir(50)
carro1.ver_combustivel()
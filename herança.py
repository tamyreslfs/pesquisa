class Veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        # Classe base que representa um veículo genérico.
        # Possui atributos comuns a todos os veículos.

class Carro(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, portas):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.portas = portas
        # Classe que representa um carro específico.
        # Herda da classe Veiculo e adiciona um atributo específico para carros.

class Moto(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindradas):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindradas = cilindradas
        # Classe que representa uma motocicleta específica.
        # Herda da classe Veiculo e adiciona um atributo específico para motos.

carro = Carro("Carro", "ABC123", "Ford", "Focus", 2020, 4)
moto = Moto("Motocicleta", "DEF456", "Honda", "CBR500", 2021, 500)

print(carro.tipo)         # Saída: Carro
print(carro.marca)        # Saída: Ford
print(carro.portas)       # Saída: 4

print(moto.tipo)          # Saída: Motocicleta
print(moto.marca)         # Saída: Honda
print(moto.cilindradas)   # Saída: 500

class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario

    def set_salario(self, novo_salario):
        if novo_salario > 0:
            self.__salario = novo_salario

# Criando um objeto da classe Funcionario
funcionario1 = Funcionario("João", 2500)

# Acessando os atributos através dos métodos get
print(funcionario1.get_nome())     # Saída: João
print(funcionario1.get_salario())  # Saída: 2500

# Tentando acessar diretamente o atributo encapsulado
print(funcionario1.__nome)  # Isso causará um erro

# Tentando modificar diretamente o atributo encapsulado
funcionario1.__salario = 3000  # Isso não irá modificar o atributo encapsulado

# Modificando o salário através do método set_salario
funcionario1.set_salario(3000)
print(funcionario1.get_salario())  # Saída: 3000

class ArtigoEsportivo:
    def calcular_preco_venda(self):
        pass
        # Método base que será implementado pelas subclasses.


class BolaDeFutebol(ArtigoEsportivo):
    def calcular_preco_venda(self):
        return 50.0
        # Implementação específica para a classe BolaDeFutebol.


class CamisaSelecao(ArtigoEsportivo):
    def calcular_preco_venda(self):
        return 100.0
        # Implementação específica para a classe CamisaSelecao.


def calcular_preco_total(artigos):
    total = 0.0
    for artigo in artigos:
        total += artigo.calcular_preco_venda()
        # Chama o método calcular_preco_venda() para cada objeto artigo,
        # independentemente da sua classe específica.
        # O polimorfismo garante que a implementação correta seja chamada
        # com base na classe do objeto.

    return total


bola = BolaDeFutebol()
camisa = CamisaSelecao()

artigos = [bola, camisa]

preco_total = calcular_preco_total(artigos)
print(f'O preço total dos artigos é: R${preco_total}')

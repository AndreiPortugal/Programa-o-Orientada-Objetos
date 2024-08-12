class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcularPrecoFinal(self):
        return self.preco

    def __str__(self):
        return f'{self.nome}: R${self.calcularPrecoFinal():.2f}'

class ProdutoNormal(Produto):
    def calcularPrecoFinal(self):
        return self.preco # Sem desconto

class ProdutoPromocional(Produto):
    def calcularPrecoFinal(self):
        return self.preco * 0.8  # Desconto de 20%

class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f'Produto {produto} adicionado ao carrinho.')

    def calcular_total(self):
        total = sum(produto.calcularPrecoFinal() for produto in self.produtos)
        return total

    def listar_produtos(self):
        print("Produtos no carrinho:")
        for produto in self.produtos:
            print(produto)

    def exibir_total(self):
        total = self.calcular_total()
        print(f'Total a pagar: R${total:.2f}')

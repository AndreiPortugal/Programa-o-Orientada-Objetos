from carrinhoCompras import ProdutoNormal, ProdutoPromocional, Carrinho

# Criando produtos
produto1 = ProdutoNormal("Relógio", 300.00)
produto2 = ProdutoPromocional("Notebook Gamer", 15000.00)
produto3 = ProdutoPromocional("Smartphone", 2000.00)

# Criando o carrinho
carrinho = Carrinho()

# Adicionando produtos ao carrinho
carrinho.adicionar_produto(produto1)
carrinho.adicionar_produto(produto2)
carrinho.adicionar_produto(produto3)

# Listando os produtos e exibindo o total
carrinho.listar_produtos()
carrinho.exibir_total()

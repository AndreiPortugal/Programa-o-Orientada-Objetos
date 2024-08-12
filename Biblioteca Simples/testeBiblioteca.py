from bibliotecaSimples import Livro, Biblioteca

# Criando alguns livros
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("Grande Sertão: Veredas", "João Guimarães Rosa")
livro3 = Livro("O Alquimista", "Paulo Coelho")

# Criando a biblioteca
biblioteca = Biblioteca()

# Adicionando livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Listando todos os livros na biblioteca
biblioteca.listar_livros()

# Buscando um livro por título
biblioteca.buscar_livro("Grande Sertão: Veredas")

# Removendo um livro da biblioteca
biblioteca.remover_livro("Dom Casmurro")

# Tentando buscar um livro removido
biblioteca.buscar_livro("Dom Casmurro")

# Listando novamente os livros na biblioteca
biblioteca.listar_livros()

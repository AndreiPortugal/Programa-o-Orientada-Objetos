class Livro:
    def __init__(self, título, autor):
        self.título = título
        self.autor = autor

    def __str__(self):
        return f'"{self.título}" by {self.autor}'
    
class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro {livro} adicionado à biblioteca.')

    def remover_livro(self, título):
        for livro in self.livros:
            if livro.título == título:
                self.livros.remove(livro)
                print(f'Livro {livro} removido com sucesso.')
                return
        print(f'Livro com o título "{título}" não encontrado')

    def buscar_livro(self, título):
        for livro in self.livros:
            if livro.título == título:
                print(f'Livro encontrado: {livro}')
                return livro
        print(f'Livro com o título "{título}" não encontrado.')
        return None
    
    def listar_livros(self):
        if not self.livros:
            print("A biblioteca está vazia.")
        else:
            print("Livros disponíveis: ")
            for livro in self.livros:
                print(livro)
    
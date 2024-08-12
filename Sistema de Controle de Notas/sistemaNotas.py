class Pessoa:
    def __init__(self, nome, identificacao):
        self.nome = nome
        self.identificacao = identificacao

    def __str__(self):
        return f'{self.nome} (ID: {self.identificacao})'

class Aluno(Pessoa):
    def __init__(self, nome, identificacao, matricula):
        super().__init__(nome, identificacao)
        self.matricula = matricula

    def __str__(self):
        return f'Aluno: {self.nome} (Matrícula: {self.matricula}, ID: {self.identificacao})'

class Professor(Pessoa):
    def __init__(self, nome, identificacao, departamento):
        super().__init__(nome, identificacao)
        self.departamento = departamento

    def __str__(self):
        return f'Professor: {self.nome} (Departamento: {self.departamento}, ID: {self.identificacao})'

class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
        self.professores = []
        self.notas = {}

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f' {aluno} adicionado à disciplina {self.nome}.')

    def adicionar_professor(self, professor):
        self.professores.append(professor)
        print(f' {professor} adicionado à disciplina {self.nome}.')

    def registrar_nota(self, aluno, nota):
        if aluno in self.alunos:
            self.notas[aluno] = nota
            print(f'Nota {nota} registrada para o aluno {aluno} na disciplina {self.nome}.')
        else:
            print(f'O aluno {aluno} não está matriculado nesta disciplina {self.nome}.')

    def listar_alunos(self):
        print(f'Alunos na disciplina {self.nome}:')
        for aluno in self.alunos:
            print(aluno)

    def listar_professores(self):
        print(f'Professores na disciplina {self.nome}:')
        for professor in self.professores:
            print(professor)

    def exibir_notas(self):
        print(f'Notas na disciplina {self.nome}:')
        for aluno, nota in self.notas.items():
            print(f'{aluno}: {nota}') 
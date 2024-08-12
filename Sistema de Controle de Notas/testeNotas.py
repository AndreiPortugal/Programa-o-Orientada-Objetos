from sistemaNotas import Aluno, Professor, Disciplina

# Criando novos alunos e professores
aluno1 = Aluno("Maurício Maria", "001", "A123")
aluno2 = Aluno("Gabriel Costa", "002", "A124")
aluno3 = Aluno("Lauana Samara", "003", "A125")
professor1 = Professor("Dr. Carlos", "P001", "Cálculo I")
professor2 = Professor("Dra. Ana", "P002", "Física I")


# Criando duas disciplinas
disciplina_calculo = Disciplina("Cálculo I")
disciplina_fisica = Disciplina("Física I")

# Adicionando alunos e professores às disciplinas
disciplina_calculo.adicionar_aluno(aluno1)
disciplina_calculo.adicionar_aluno(aluno2)
disciplina_calculo.adicionar_professor(professor1)

disciplina_fisica.adicionar_aluno(aluno2)
disciplina_fisica.adicionar_aluno(aluno3)
disciplina_fisica.adicionar_professor(professor2)

# Registrando notas para as disciplinas
disciplina_calculo.registrar_nota(aluno1, 8.5)
disciplina_calculo.registrar_nota(aluno2, 7.0)

disciplina_fisica.registrar_nota(aluno2, 9.0)
disciplina_fisica.registrar_nota(aluno3, 6.5)

# Listando informações para cada disciplina
print("\nInformações da Disciplina Cálculo I:")
disciplina_calculo.listar_alunos()
disciplina_calculo.listar_professores()
disciplina_calculo.exibir_notas()

print("\nInformações da Disciplina Física I:")
disciplina_fisica.listar_alunos()
disciplina_fisica.listar_professores()
disciplina_fisica.exibir_notas()
# RELACIONAMENTO DE HERANÇA entre Atividade e as subclasses Tarefa, Projeto, Trabalho e Prova:
# As classes Tarefa, Projeto, Trabalho e Prova herdam as propriedades e métodos da classe Atividade.

# Classe Aluno
class Aluno:
    def __init__(self, nome, idade, turma, curso, tipo_grade, matricula):
        self.__nome = nome
        self.__idade = idade
        self.__turma = turma
        self.__curso = curso
        self.__tipo_grade = tipo_grade
        self.__matricula = matricula

    def exibir_dados(self):
        print(f'''Nome: {self.__nome}
Idade: {self.__idade}
Turma: {self.__turma}
Curso: {self.__curso}
Tipo de Grade: {self.__tipo_grade}
Matrícula: {self.__matricula}''')


# Classe base Atividade
class Atividade:
    def __init__(self, titulo, descricao, data_entrega):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_entrega = data_entrega

    def exibir_atividade(self):
        return (f"Título: {self.__titulo}\n"
                f"Descrição: {self.__descricao}\n"
                f"Data de Entrega: {self.__data_entrega}")


# Subclasse Tarefa com novo atributo `disciplina`
class Tarefa(Atividade):
    def __init__(self, titulo, descricao, data_entrega, disciplina):
        super().__init__(titulo, descricao, data_entrega)
        self.__disciplina = disciplina

    def exibir_atividade(self):
        return (super().exibir_atividade() +
                f"\nDisciplina: {self.__disciplina}")


# Subclasse Projeto com novos atributos `tipo_projeto`, `professor_orientador`, e `data_inicio`
class Projeto(Atividade):
    def __init__(self, titulo, descricao, data_entrega, tipo_projeto, professor_orientador, data_inicio):
        super().__init__(titulo, descricao, data_entrega)
        self.__tipo_projeto = tipo_projeto
        self.__professor_orientador = professor_orientador
        self.__data_inicio = data_inicio

    def exibir_atividade(self):
        return (super().exibir_atividade() +
                f"\nTipo de Projeto: {self.__tipo_projeto}\n"
                f"Professor Orientador: {self.__professor_orientador}\n"
                f"Data de Início: {self.__data_inicio}")


# Subclasse Trabalho com novo atributo `disciplina`
class Trabalho(Atividade):
    def __init__(self, titulo, descricao, data_entrega, disciplina):
        super().__init__(titulo, descricao, data_entrega)
        self.__disciplina = disciplina

    def exibir_atividade(self):
        return (super().exibir_atividade() +
                f"\nDisciplina: {self.__disciplina}")


# Subclasse Prova com novos atributos `disciplina`, `horario`, e `tentativa`
class Prova(Atividade):
    def __init__(self, titulo, descricao, data_entrega, disciplina, horario, tentativa):
        super().__init__(titulo, descricao, data_entrega)
        self.__disciplina = disciplina
        self.__horario = horario
        self.__tentativa = tentativa

    def exibir_atividade(self):
        return (super().exibir_atividade() +
                f"\nDisciplina: {self.__disciplina}\n"
                f"Horário: {self.__horario}\n"
                f"Tentativa: {self.__tentativa}")

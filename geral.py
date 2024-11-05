#Alunos: João Gabriel, Calebe Melo, Renan Almeida, Yann Aguiar
#Turma: 2°A Informática



# RELACIONAMENTO DE DEPENDÊNCIA entre Aluno e SistemaDeUsuarios:
# A classe Aluno só pode ser instanciada depois que o login for realizado com sucesso através do SistemaDeUsuarios.
# Isso representa uma relação de dependência, pois a criação de Aluno depende temporariamente de uma ação do SistemaDeUsuarios.

from usuario import SistemaDeUsuarios
from atividade import Aluno
from gerenciador import GerenciadorDeAtividades, Tarefa, Projeto, Trabalho, Prova

def main():
    sistema = SistemaDeUsuarios()
    aluno = None

    while True:
        print("1. Cadastrar")
        print("2. Login")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            matricula = input("Matrícula: ")
            senha = input("Senha: ")
            sistema.cadastrar_usuario(matricula, senha)

        elif escolha == "2":
            matricula = input("Matrícula: ")
            senha = input("Senha: ")
            if sistema.login(matricula, senha):
                print("Login bem-sucedido!")
                
                # RELACIONAMENTO DE DEPENDÊNCIA entre SistemaDeUsuarios e Aluno
                # Criação do aluno depende de um login bem-sucedido
                print("\nCadastro de Aluno")
                nome = input("Nome completo: ")
                idade = input("Idade: ")
                turma = input("Turma: ")
                curso = input("Curso: ")
                tipo_grade = input("Tipo de Grade: ")

                aluno = Aluno(nome, idade, turma, curso, tipo_grade, matricula)
                print("\nDados do Aluno:")
                print(aluno.exibir_dados())
                break  # Sai do loop após login e criação do aluno

        else:
            print("Opção inválida.")

    # RELACIONAMENTO DE AGREGAÇÃO entre GerenciadorDeAtividades e Atividades:
    # A classe GerenciadorDeAtividades contém e gerencia várias instâncias de Tarefa, Projeto, Trabalho e Prova,
    # mas elas podem existir de forma independente de GerenciadorDeAtividades.
    gerenciador = GerenciadorDeAtividades()

    while True:
        print("\nGerenciamento de Atividades")
        print("1. Adicionar Atividade")
        print("2. Exibir Atividades")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            tipo = input("Tipo de Atividade (Tarefa, Projeto, Trabalho, Prova): ")
            titulo = input("Título: ")
            descricao = input("Descrição: ")
            data_entrega = input("Data de Entrega: ")

            # RELACIONAMENTO DE HERANÇA entre Atividade e Tarefa, Projeto, Trabalho e Prova:
            # As classes Tarefa, Projeto, Trabalho e Prova herdam características e comportamentos da classe base Atividade.
            if tipo == "Tarefa":
                disciplina = input("Disciplina: ")
                atividade = Tarefa(titulo, descricao, data_entrega, disciplina)
            elif tipo == "Projeto":
                tipo_projeto = input("Tipo de Projeto: ")
                professor_orientador = input("Professor Orientador: ")
                data_inicio = input("Data de Início: ")
                atividade = Projeto(titulo, descricao, data_entrega, tipo_projeto, professor_orientador, data_inicio)
            elif tipo == "Trabalho":
                disciplina = input("Disciplina: ")
                atividade = Trabalho(titulo, descricao, data_entrega, disciplina)
            elif tipo == "Prova":
                disciplina = input("Disciplina: ")
                horario = input("Horário: ")
                tentativa = input("Tentativa: ")
                atividade = Prova(titulo, descricao, data_entrega, disciplina, horario, tentativa)
            else:
                print("Tipo de atividade inválido.")
                continue

            gerenciador.adicionar_atividade(tipo, atividade)

        elif escolha == "2":
            gerenciador.exibir_atividades()

        elif escolha == "3":
            print("Saindo...")
            break

        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()

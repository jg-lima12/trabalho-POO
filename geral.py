#Alunos: João Gabriel, Calebe Melo, Renan Almeida, Yann Aguiar
#Turma: 2°A Informática



# RELACIONAMENTO DE DEPENDÊNCIA entre Aluno e SistemaDeUsuarios:
# A classe Aluno só pode ser instanciada depois que o login for realizado com sucesso através do SistemaDeUsuarios.
# Isso representa uma relação de dependência, pois a criação de Aluno depende temporariamente de uma ação do SistemaDeUsuarios.

from usuario import SistemaDeUsuarios
from atividade import Aluno
from gerenciador import GerenciadorDeAtividades, Tarefa, Projeto, Trabalho, Prova
from cor import azul, fim
import os
import time

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    sistema = SistemaDeUsuarios()
    aluno = None

    while True:
        limpar_terminal()
        escolha = input(f'''Escolha uma opção:
                        
{azul}[1]Cadastrar
[2]Login{fim}

Resposta: ''')

        if escolha == "1":
            limpar_terminal()
            matricula = input("\nMatrícula: ")
            senha = input("Senha: ")
            sistema.cadastrar_usuario(matricula, senha)

        elif escolha == "2":
            limpar_terminal()
            matricula = input("\nMatrícula: ")
            senha = input("Senha: ")
            if sistema.login(matricula, senha):
                print("Login bem-sucedido!")
                time.sleep(1)
                limpar_terminal()
                
                # RELACIONAMENTO DE DEPENDÊNCIA entre SistemaDeUsuarios e Aluno
                # Criação do aluno depende de um login bem-sucedido
                print(f"\n{azul}Cadastro de Aluno{fim}")
                nome = input("Nome completo: ")
                idade = input("Idade: ")
                turma = input("Turma: ")
                curso = input("Curso: ")
                tipo_grade = input("Tipo de Grade: ")
                limpar_terminal()
                time.sleep(1)

                aluno = Aluno(nome, idade, turma, curso, tipo_grade, matricula)
                print("\nDados do Aluno:")
                print(aluno.exibir_dados())
                break  # Sai do loop após login e criação do aluno

        else:
            print("\nOpção inválida.")

    # RELACIONAMENTO DE AGREGAÇÃO entre GerenciadorDeAtividades e Atividades:
    # A classe GerenciadorDeAtividades contém e gerencia várias instâncias de Tarefa, Projeto, Trabalho e Prova,
    # mas elas podem existir de forma independente de GerenciadorDeAtividades.
    gerenciador = GerenciadorDeAtividades()

    while True:
        print("\nGerenciamento de Atividades")
        print(f"\n{azul}[1]Adicionar Atividade{fim}")
        print(f"{azul}[2]Exibir Atividades{fim}")
        print(f"{azul}[3]Sair{fim}")
        escolha = input("\nEscolha uma opção: ")

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

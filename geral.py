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
    gerenciador = GerenciadorDeAtividades()

    while True:
        limpar_terminal()
        escolha = input(f'''Escolha uma opção:
{azul}[1]Cadastrar   [2]Login{fim}
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
                time.sleep(1.5)
                limpar_terminal()

                print(f"\n{azul}Cadastro de Aluno{fim}")
                nome = input("Nome completo: ")
                idade = input("Idade: ")
                turma = input("Turma: ")
                curso = input("Curso: ")
                tipo_grade = input("Tipo de Grade: ")
                aluno = Aluno(nome, idade, turma, curso, tipo_grade, matricula)

                while True:
                    limpar_terminal()
                    print("\nGerenciamento de Atividades")
                    print(f"{azul}[1]Adicionar Atividade{fim}")
                    print(f"{azul}[2]Exibir Atividades{fim}")
                    print(f"{azul}[3]Sair{fim}")
                    escolha_atividade = input("\nEscolha uma opção: ")

                    if escolha_atividade == "1":
                        limpar_terminal()
                        tipo = int(input(f'''\nTipo de Atividade
{azul}[1]Tarefa   [2]Projeto   [3]Trabalho   [4]Prova{fim}
Resposta: '''))
                        
                        # Mapeamento de números para tipos de atividade
                        tipos_validos = {1: 'Tarefa', 2: 'Projeto', 3: 'Trabalho', 4: 'Prova'}
                        tipo_str = tipos_validos.get(tipo)

                        if tipo_str:  # Se o tipo for válido
                            titulo = input("\nTítulo: ")
                            descricao = input("Descrição: ")
                            data_entrega = input("Data de Entrega: ")

                            if tipo_str == "Tarefa":
                                disciplina = input("Disciplina: ")
                                atividade = Tarefa(titulo, descricao, data_entrega, disciplina)
                            elif tipo_str == "Projeto":
                                tipo_projeto = input("Tipo de Projeto: ")
                                professor_orientador = input("Professor Orientador: ")
                                data_inicio = input("Data de Início: ")
                                atividade = Projeto(titulo, descricao, data_entrega, tipo_projeto, professor_orientador, data_inicio)
                            elif tipo_str == "Trabalho":
                                disciplina = input("Disciplina: ")
                                atividade = Trabalho(titulo, descricao, data_entrega, disciplina)
                            elif tipo_str == "Prova":
                                disciplina = input("Disciplina: ")
                                horario = input("Horário: ")
                                tentativa = input("Tentativa: ")
                                atividade = Prova(titulo, descricao, data_entrega, disciplina, horario, tentativa)

                            gerenciador.adicionar_atividade(tipo_str, atividade)
                            time.sleep(2)
                        else:
                            print("Tipo inválido. Tente novamente.")
                            time.sleep(1.5)

                    elif escolha_atividade == "2":
                        limpar_terminal()
                        print(f"{azul}\nAtividades Cadastradas:{fim}")
                        gerenciador.exibir_atividades()
                        input(f"{azul}\nPressione ENTER para continuar...{fim}")

                    elif escolha_atividade == "3":
                        print("\nSaindo...")
                        time.sleep(1)
                        break
                    else:
                        print("Escolha inválida. Tente novamente.")
                        time.sleep(1.5)
            else:
                input(f"\n{azul}Login falhou. Pressione ENTER para tentar novamente.{fim}")

if __name__ == "__main__":
    main()

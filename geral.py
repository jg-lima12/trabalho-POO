from usuario import SistemaDeUsuarios
from atividade import Aluno, Tarefa, Projeto, Trabalho, Prova
from gerenciador import GerenciadorDeAtividades
from cor import azul, fim
import os
import time

class TipoAtividadeInvalidoException(Exception):
    def __init__(self):
        super().__init__("Tipo de atividade inválido. Escolha entre as opções apresentadas.")

class EntradaNaoNumericaException(Exception):
    def __init__(self):
        super().__init__("Entrada inválida. Digite apenas números para escolher a opção.")

class CampoVazioException(Exception):
    def __init__(self, campo):
        super().__init__(f"O campo '{campo}' não pode estar vazio. Por favor, preencha todas as informações.")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    sistema = SistemaDeUsuarios()
    gerenciador = GerenciadorDeAtividades()

    while True:
        try:
            limpar_terminal()
            escolha = input(f'''\nEscolha uma opção:
{azul}[1]Cadastrar   [2]Login   [3]Sair{fim}
Resposta: ''')

            if not escolha.isdigit():
                raise EntradaNaoNumericaException()

            escolha = int(escolha)

            if escolha == 1:
                limpar_terminal()
                matricula = input("\nMatrícula: ").strip()
                senha = input("Senha: ").strip()
                sistema.cadastrar_usuario(matricula, senha)

            elif escolha == 2:
                limpar_terminal()
                matricula = input("\nMatrícula: ").strip()
                senha = input("Senha: ").strip()
                if sistema.login(matricula, senha):
                    time.sleep(2)
                    limpar_terminal()
                    print(f"\n{azul}Cadastro de Aluno{fim}")
                    nome = input("Nome completo: ").strip()
                    if not nome:
                        raise CampoVazioException("Nome completo")
                    idade = input("Idade: ").strip()
                    turma = input("Turma: ").strip()
                    curso = input("Curso: ").strip()
                    tipo_grade = input("Tipo de Grade: ").strip()
                    aluno = Aluno(nome, idade, turma, curso, tipo_grade, matricula)
                    print("\nDados do Aluno:")
                    aluno.exibir_dados()
                    time.sleep(3)

                    while True:
                        limpar_terminal()
                        print("\nGerenciamento de Atividades")
                        print(f"\n{azul}[1]Adicionar Atividade{fim}")
                        print(f"{azul}[2]Exibir Atividades{fim}")
                        print(f"{azul}[3]Sair{fim}")
                        opcao = input("\nEscolha uma opção: ").strip()

                        if not opcao.isdigit():
                            raise EntradaNaoNumericaException()

                        opcao = int(opcao)

                        if opcao == 1:
                            try:
                                limpar_terminal()
                                tipo = input(f'''\nTipo de Atividade
{azul}[1]Tarefa   [2]Projeto   [3]Trabalho   [4]Prova{fim}
Resposta: ''').strip()

                                if not tipo.isdigit():
                                    raise EntradaNaoNumericaException()

                                tipo = int(tipo)
                                tipos_validos = {1: 'Tarefa', 2: 'Projeto', 3: 'Trabalho', 4: 'Prova'}
                                tipo_str = tipos_validos.get(tipo)

                                if not tipo_str:
                                    raise TipoAtividadeInvalidoException()

                                titulo = input("\nTítulo: ").strip()
                                if not titulo:
                                    raise CampoVazioException("Título")
                                descricao = input("Descrição: ").strip()
                                if not descricao:
                                    raise CampoVazioException("Descrição")
                                data_entrega = input("Data de Entrega: ").strip()
                                if not data_entrega:
                                    raise CampoVazioException("Data de Entrega")

                                if tipo_str == "Tarefa":
                                    disciplina = input("Disciplina: ").strip()
                                    if not disciplina:
                                        raise CampoVazioException("Disciplina")
                                    atividade = Tarefa(titulo, descricao, data_entrega, disciplina)

                                elif tipo_str == "Projeto":
                                    tipo_projeto = input("Tipo de Projeto: ").strip()
                                    professor_orientador = input("Professor Orientador: ").strip()
                                    data_inicio = input("Data de Início: ").strip()
                                    atividade = Projeto(titulo, descricao, data_entrega, tipo_projeto, professor_orientador, data_inicio)

                                elif tipo_str == "Trabalho":
                                    disciplina = input("Disciplina: ").strip()
                                    if not disciplina:
                                        raise CampoVazioException("Disciplina")
                                    atividade = Trabalho(titulo, descricao, data_entrega, disciplina)

                                elif tipo_str == "Prova":
                                    disciplina = input("Disciplina: ").strip()
                                    horario = input("Horário: ").strip()
                                    tentativa = input("Tentativa: ").strip()
                                    atividade = Prova(titulo, descricao, data_entrega, disciplina, horario, tentativa)

                                gerenciador.adicionar_atividade(tipo_str, atividade)

                            except (CampoVazioException, EntradaNaoNumericaException, TipoAtividadeInvalidoException) as e:
                                print(f"\n{azul}Erro: {e}{fim}")
                                time.sleep(2)

                        elif opcao == 2:
                            limpar_terminal()
                            gerenciador.exibir_atividades()
                            input(f'{azul}Pressione ENTER para continuar...{fim}')

                        elif opcao == 3:
                            print("Voltando ao menu principal...")
                            time.sleep(1)
                            break

                        else:
                            print("Escolha inválida. Tente novamente.")
                            time.sleep(2)

            elif escolha == 3:
                print("\nSaindo do sistema...")
                break

            else:
                print("Escolha inválida. Tente novamente.")
                time.sleep(2)

        except (EntradaNaoNumericaException, CampoVazioException) as e:
            print(f"\n{azul}Erro: {e}{fim}")
            time.sleep(2)

if __name__ == "__main__":
    main()

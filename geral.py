from usuario import SistemaDeUsuarios
from atividade import Aluno
from gerenciador import GerenciadorDeAtividades, Tarefa, Projeto, Trabalho, Prova
from cor import azul, fim
import os
import time

# Exceção Personalizada
class EntradaInvalidaError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class ValorNaoPodeSerVazioError(Exception):
    def __init__(self, campo):
        super().__init__(f"O campo '{campo}' não pode ser vazio.")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_entrada(valor, tipo_esperado, campo):
    if not isinstance(valor, tipo_esperado):
        raise EntradaInvalidaError(f"Entrada inválida para o campo '{campo}'. Esperado: {tipo_esperado.__name__}")
    if isinstance(valor, str) and not valor.strip():
        raise ValorNaoPodeSerVazioError(campo)

def main():
    sistema = SistemaDeUsuarios()
    aluno = None

    while True:
        try:
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
                    limpar_terminal()
                    time.sleep(1)
                    
                    print(f"\n{azul}Cadastro de Aluno{fim}")
                    nome = input("Nome completo: ")
                    idade = input("Idade: ")
                    turma = input("Turma: ")
                    curso = input("Curso: ")
                    tipo_grade = input("Tipo de Grade: ")

                    try:
                        # Verificações para garantir a validade dos dados
                        verificar_entrada(nome, str, "Nome completo")
                        verificar_entrada(idade, str, "Idade")
                        verificar_entrada(turma, str, "Turma")
                        verificar_entrada(curso, str, "Curso")
                        verificar_entrada(tipo_grade, str, "Tipo de Grade")
                    except (EntradaInvalidaError, ValorNaoPodeSerVazioError) as e:
                        print(f"Erro: {e}")
                        time.sleep(2)
                        continue
                    
                    aluno = Aluno(nome, idade, turma, curso, tipo_grade, matricula)
                    print("\nDados do Aluno:")
                    print(aluno.exibir_dados())
                    break  # Sai do loop após login e criação do aluno

                else:
                    print("Login falhou. Tente novamente.")
                    time.sleep(2)
            else:
                raise EntradaInvalidaError("Opção inválida no menu principal.")

        except EntradaInvalidaError as e:
            print(f"Erro: {e}")
            time.sleep(2)
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            time.sleep(2)
        finally:
            print("Operação concluída.")

    gerenciador = GerenciadorDeAtividades()

    while True:
        try:
            limpar_terminal()
            print("\nGerenciamento de Atividades")
            print(f"\n{azul}[1]Adicionar Atividade{fim}")
            print(f"{azul}[2]Exibir Atividades{fim}")
            print(f"{azul}[3]Sair{fim}")
            escolha = input("\nEscolha uma opção: ")

            if escolha == "1":
                limpar_terminal()
                tipo = int(input(f'''\tTipo de Atividade

{azul}[1]Tarefa
[2]Projeto
[3]Trabalho
[4]Prova{fim}

Resposta: '''))

                if tipo not in [1, 2, 3, 4]:
                    raise EntradaInvalidaError("Tipo de atividade inválido.")

                titulo = input("Título: ")
                descricao = input("Descrição: ")
                data_entrega = input("Data de Entrega: ")

                try:
                    verificar_entrada(titulo, str, "Título")
                    verificar_entrada(descricao, str, "Descrição")
                    verificar_entrada(data_entrega, str, "Data de Entrega")
                except (EntradaInvalidaError, ValorNaoPodeSerVazioError) as e:
                    print(f"Erro: {e}")
                    time.sleep(2)
                    continue

                if tipo == 1:
                    disciplina = input("Disciplina: ")
                    atividade = Tarefa(titulo, descricao, data_entrega, disciplina)
                elif tipo == 2:
                    tipo_projeto = input("Tipo de Projeto: ")
                    professor_orientador = input("Professor Orientador: ")
                    data_inicio = input("Data de Início: ")
                    atividade = Projeto(titulo, descricao, data_entrega, tipo_projeto, professor_orientador, data_inicio)
                elif tipo == 3:
                    disciplina = input("Disciplina: ")
                    atividade = Trabalho(titulo, descricao, data_entrega, disciplina)
                elif tipo == 4:
                    disciplina = input("Disciplina: ")
                    horario = input("Horário: ")
                    tentativa = input("Tentativa: ")
                    atividade = Prova(titulo, descricao, data_entrega, disciplina, horario, tentativa)

                gerenciador.adicionar_atividade(tipo, atividade)

            elif escolha == "2":
                gerenciador.exibir_atividades()

            elif escolha == "3":
                print("Saindo...")
                break

            else:
                raise EntradaInvalidaError("Opção inválida no gerenciamento de atividades.")

        except EntradaInvalidaError as e:
            print(f"Erro: {e}")
            time.sleep(2)
        except ValorNaoPodeSerVazioError as e:
            print(f"Erro: {e}")
            time.sleep(2)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            time.sleep(2)
        finally:
            print("Operação finalizada.")

if __name__ == "__main__":
    main()

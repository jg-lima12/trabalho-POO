# RELACIONAMENTO DE AGREGAÇÃO entre GerenciadorDeAtividades e Atividade:
# GerenciadorDeAtividades mantém uma lista de atividades que inclui instâncias de Tarefa, Projeto, Trabalho e Prova.
# As atividades existem independentemente do gerenciador, e o gerenciador apenas as organiza e exibe.

from atividade import Tarefa, Projeto, Trabalho, Prova

class GerenciadorDeAtividades:
    def __init__(self):
        self.__atividades = {
            'Tarefa': [],
            'Projeto': [],
            'Trabalho': [],
            'Prova': []
        }

    def adicionar_atividade(self, tipo, atividade):
        if tipo in self.__atividades:
            self.__atividades[tipo].append(atividade)
            print(f"Atividade do tipo {tipo} adicionada com sucesso.")
        else:
            print("Tipo de atividade inválido.")

    def exibir_atividades(self):
        for tipo, lista in self.__atividades.items():
            print(f"{tipo}s:")
            for atividade in lista:
                print(atividade.exibir_atividade())
                print()

# RELACIONAMENTO DE DEPENDÊNCIA entre SistemaDeUsuarios e Aluno:
# O SistemaDeUsuarios é temporariamente necessário para que o aluno faça login, mas não mantém uma relação contínua
# após o login bem-sucedido. Essa relação é apenas uma dependência temporária.

class SistemaDeUsuarios:
    def __init__(self):
        self.__usuarios = {}

    def cadastrar_usuario(self, matricula, senha):
        if matricula in self.__usuarios:
            print("Usuário já cadastrado.")
        else:
            self.__usuarios[matricula] = senha
            print("Usuário cadastrado com sucesso.")

    def login(self, matricula, senha):
        if matricula in self.__usuarios and self.__usuarios[matricula] == senha:
            print("Login realizado com sucesso.")
            return True
        else:
            print("Matrícula ou senha incorretos.")
            return False

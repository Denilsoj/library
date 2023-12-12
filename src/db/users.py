from config.conection import conexao_mariadb
import mysql.connector

# Função para cadastrar um novo usuário
def cadastrar_usuario(cursor):
    try:
        nome_usuario = input("Digite seu nome de usuário: ")
        senha_usuario = input("Digite sua senha: ")

        # Inserir usuário na tabela 'usuarios'
        cursor.execute("INSERT INTO usuarios (nome_usuario, senha_usuario) VALUES (%s, %s)",
                       (nome_usuario, senha_usuario))
        conexao_mariadb.commit()

        print("Usuário cadastrado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar usuário: {err}")

# Função para fazer login
def fazer_login(cursor):
    try:
        nome_usuario = input("Digite seu nome de usuário: ")
        senha_usuario = input("Digite sua senha: ")

        # Verificar se o usuário e a senha correspondem
        cursor.execute("SELECT * FROM usuarios WHERE nome_usuario = %s AND senha_usuario = %s",
                       (nome_usuario, senha_usuario))
        resultado = cursor.fetchone()

        if resultado:
            print("Login bem-sucedido!")
            return nome_usuario
        else:
            print("Nome de usuário ou senha incorretos. Tente novamente.")
            return None
    except mysql.connector.Error as err:
        print(f"Erro ao fazer login: {err}")
        return None

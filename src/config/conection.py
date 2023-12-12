import mysql.connector
from mysql.connector import Error

connection = False

def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            user='root',
            password='1qfs00ff-___sf32fSDFSDfs00',
            host='34.95.177.68',
            database='library'
        )
        print("Conexão ao MariaDB estabelecida com sucesso!")
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro de conexão: {err}")
        return None

def criar_tabela_usuarios(conexao):
    try:
        cursor = conexao.cursor()

        # Criar tabela de usuários
        query = """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_usuario VARCHAR(255) NOT NULL UNIQUE,
            senha_usuario VARCHAR(255) NOT NULL
);
        )
        """
        cursor.execute(query)
        print("Tabela 'usuarios' criada com sucesso.")
        connection = True
    except Error as e:
        print(f"Erro ao criar tabela de usuários: {e}")
    finally:
        if cursor:
            cursor.close()

def criar_tabela_livros(conexao):
    try:
        cursor = conexao.cursor()

        # Criar tabela de usuários
        query = """
        CREATE TABLE IF NOT EXISTS livros (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome_usuario VARCHAR(255) NOT NULL,
            titulo VARCHAR(255) NOT NULL,
            autor VARCHAR(255) NOT NULL,
            editora VARCHAR(255) NOT NULL,
            FOREIGN KEY (nome_usuario) REFERENCES usuarios(nome_usuario) ON DELETE CASCADE
);
        )
        """
        cursor.execute(query)
        print("Tabela 'livros' criada com sucesso.")
    except Error as e:
        print(f"Erro ao criar tabela de livros: {e}")
    finally:
        if cursor:
            cursor.close()

# Conectar ao banco de dados
conexao_mariadb = conectar_bd()

# Criar tabelas
if connection:
    criar_tabela_usuarios(conexao_mariadb)
    criar_tabela_livros(conexao_mariadb)

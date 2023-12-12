import mysql.connector

# Função para conectar ao banco de dados MariaDB
def conectar_bd():
    return mysql.connector.connect(
        user='root',
        password='1qfs00ff-___sf32fSDFSDfs00',
        host='34.95.177.68',
        database='library'
    )

# Função para cadastrar um novo usuário
def cadastrar_usuario(cursor):
    try:
        nome_usuario = input("Digite seu nome de usuário: ")
        senha_usuario = input("Digite sua senha: ")

        # Inserir usuário na tabela 'usuarios'
        cursor.execute("INSERT INTO usuarios (nome_usuario, senha_usuario) VALUES (%s, %s)",
                       (nome_usuario, senha_usuario))
        conexao.commit()

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

# Função para cadastrar um novo livro
def cadastrar_livro(cursor, nome_usuario):
    try:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o nome do autor: ")
        editora = input("Digite o nome da editora: ")

        # Inserir livro na tabela 'livros' associado ao usuário logado
        cursor.execute("INSERT INTO livros (nome_usuario, titulo, autor, editora) VALUES (%s, %s, %s, %s)",
                       (nome_usuario, titulo, autor, editora))
        conexao.commit()

        print("Livro cadastrado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar livro: {err}")

# Função para listar os livros do usuário logado
def listar_livros(cursor, nome_usuario):
    try:
        # Selecionar livros associados ao usuário logado
        cursor.execute("SELECT * FROM livros WHERE nome_usuario = %s", (nome_usuario,))
        livros = cursor.fetchall()

        if livros:
            print("\n======== Lista de Livros Cadastrados =======")
            for livro in livros:
                print(f"ID: {livro[0]}, Título: {livro[2]}, Autor: {livro[3]}, Editora: {livro[4]}")
            print("==============================================")
        else:
            print("Você ainda não cadastrou nenhum livro.")
    except mysql.connector.Error as err:
        print(f"Erro ao listar livros: {err}")

# Função para atualizar informações de um livro
def atualizar_livro(cursor, nome_usuario):
    try:
        # Listar livros antes de atualizar
        listar_livros(cursor, nome_usuario)

        # Solicitar ID do livro a ser atualizado
        id_livro = input("Digite o ID do livro que deseja atualizar: ")

        # Verificar se o livro pertence ao usuário logado
        cursor.execute("SELECT * FROM livros WHERE id = %s AND nome_usuario = %s", (id_livro, nome_usuario))
        livro = cursor.fetchone()

        if livro:
            # Solicitar novas informações para o livro
            novo_nome = input("Digite o novo nome do livro (ou pressione Enter para manter o mesmo): ")
            novo_autor = input("Digite o novo nome do autor (ou pressione Enter para manter o mesmo): ")
            nova_editora = input("Digite a nova editora do livro (ou pressione Enter para manter o mesmo): ")

            # Atualizar o livro na tabela 'livros'
            cursor.execute("UPDATE livros SET titulo = %s, autor = %s, editora = %s WHERE id = %s",
                           (novo_nome, novo_autor, nova_editora, id_livro))
            conexao.commit()

            print("Livro atualizado com sucesso!")
        else:
            print("Você não tem permissão para atualizar este livro ou o ID do livro é inválido.")
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar livro: {err}")

def apagar_livro(cursor, nome_usuario):
    try:
        # Listar livros antes de apagar
        listar_livros(cursor, nome_usuario)

        # Solicitar ID do livro a ser apagado
        id_livro = input("Digite o ID do livro que deseja apagar: ")

        # Verificar se o livro pertence ao usuário logado
        cursor.execute("SELECT * FROM livros WHERE id = %s AND nome_usuario = %s", (id_livro, nome_usuario))
        livro = cursor.fetchone()

        if livro:
            # Apagar o livro da tabela 'livros'
            cursor.execute("DELETE FROM livros WHERE id = %s", (id_livro,))
            conexao.commit()

            print("Livro apagado com sucesso!")
        else:
            print("Você não tem permissão para apagar este livro ou o ID do livro é inválido.")
    except mysql.connector.Error as err:
        print(f"Erro ao apagar livro: {err}")

# Conectar ao banco de dados
conexao = conectar_bd()
cursor = conexao.cursor()

# Menu principal
usuario_logado = None
while True:
    print("\n===== MENU =====")
    print("1. Cadastrar Usuário")
    print("2. Fazer Login")
    print("3. Cadastrar Livro")
    print("4. Listar Livros")
    print("5. Atualizar lvros")
    print("6. Apagar Livros")
    print("5. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        cadastrar_usuario(cursor)
    elif escolha == "2":
        usuario_logado = fazer_login(cursor)
    elif escolha == "3":
        if usuario_logado:
            cadastrar_livro(cursor, usuario_logado)
        else:
            print("Faça login antes de cadastrar um livro.")
    elif escolha == "4":
        if usuario_logado:
            listar_livros(cursor, usuario_logado)
        else:
            print("Faça login antes de listar os livros.")
    elif escolha == "5":
        atualizar_livro(cursor, usuario_logado)
    elif escolha == "6":
        apagar_livro(cursor, usuario_logado)
    elif escolha == 7:
        print("Saindo do programa.")
        break
        
    else:
        print("Opção inválida. Tente novamente.")

# Fechar conexão com o banco de dados
cursor.close()
conexao.close()

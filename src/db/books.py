from config.conection import conexao_mariadb
import mysql.connector

# Função para cadastrar um novo livro
def cadastrar_livro(cursor, nome_usuario):
    while True:
        try:
            # Solicitar informações ao usuário
            titulo = input("Digite o título do livro: ")
            if not titulo:
                raise ValueError("O título do livro não pode estar vazio. Tente novamente.")

            autor = input("Digite o nome do autor: ")
            if not autor:
                raise ValueError("O nome do autor não pode estar vazio. Tente novamente.")

            editora = input("Digite o nome da editora: ")
            if not editora:
                raise ValueError("O nome da editora não pode estar vazio. Tente novamente.")

            # Inserir livro na tabela 'livros' associado ao usuário logado
            cursor.execute("INSERT INTO livros (nome_usuario, titulo, autor, editora) VALUES (%s, %s, %s, %s)",
                           (nome_usuario, titulo, autor, editora))
            conexao_mariadb.commit()

            print("Livro cadastrado com sucesso!")
            break  

        except ValueError as ve:
            print(f"Erro ao cadastrar livro: {ve}")
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
            # Exibir informações do livro antes de atualizar
            print(f"\nInformações do livro a ser atualizado:")
            print(f"ID: {livro[0]}")
            print(f"Título: {livro[1]}")
            print(f"Autor: {livro[2]}")
            print(f"Editora: {livro[3]}\n")

            # Solicitar novas informações para o livro
            novo_nome = input("Digite o novo nome do livro (ou pressione Enter para manter o mesmo): ")
            novo_autor = input("Digite o novo nome do autor (ou pressione Enter para manter o mesmo): ")
            nova_editora = input("Digite a nova editora do livro (ou pressione Enter para manter o mesmo): ")

            # Verificar se os novos valores não são vazios antes de atualizar
            if not novo_nome:
                novo_nome = livro[1]
            if not novo_autor:
                novo_autor = livro[2]
            if not nova_editora:
                nova_editora = livro[3]

            # Atualizar o livro na tabela 'livros'
            cursor.execute("UPDATE livros SET titulo = %s, autor = %s, editora = %s WHERE id = %s",
                           (novo_nome, novo_autor, nova_editora, id_livro))
            conexao_mariadb.commit()

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
            conexao_mariadb.commit()

            print("Livro apagado com sucesso!")
        else:
            print("Você não tem permissão para apagar este livro ou o ID do livro é inválido.")
    except mysql.connector.Error as err:
        print(f"Erro ao apagar livro: {err}")
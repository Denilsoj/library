from config.conection import conexao_mariadb
from db.users import cadastrar_usuario, fazer_login
from db.books import cadastrar_livro, listar_livros, atualizar_livro, apagar_livro
from utils.clearTerminal import limpar_terminal


cursor = conexao_mariadb.cursor()
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
    print("7. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        cadastrar_usuario(cursor)
        limpar_terminal()
    elif escolha == "2":
        usuario_logado = fazer_login(cursor)
        limpar_terminal()
    elif escolha == "3":
        if usuario_logado:
            cadastrar_livro(cursor, usuario_logado)
            limpar_terminal()
        else:
            print("Faça login antes de cadastrar um livro.")
            limpar_terminal()
    elif escolha == "4":
        if usuario_logado:
            listar_livros(cursor, usuario_logado)
        else:
            print("Faça login antes de listar os livros.")
            limpar_terminal()
    elif escolha == "5":
        atualizar_livro(cursor, usuario_logado)
        limpar_terminal()
    elif escolha == "6":
        apagar_livro(cursor, usuario_logado)
        limpar_terminal()
    elif escolha == "7":
        print("Saindo do programa.")
        limpar_terminal()
        break
        
    else:
        print("Opção inválida. Tente novamente.")

# Fechar conexão com o banco de dados
cursor.close()
conexao_mariadb.close()

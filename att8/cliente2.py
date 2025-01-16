import argparse
import users_wrapper as usuarios
import requests

def main():
    parser = argparse.ArgumentParser(description="CRUD de usuários da JSON Placeholder")
    subparsers = parser.add_subparsers(dest="comando")

    # Subcomando para listar todos os usuários
    subparsers.add_parser("listar", help="Listar todos os usuários")

    # Subcomando para listar as tarefas de um usuário específico
    tarefas_parser = subparsers.add_parser("tarefas", help="Listar tarefas de um usuário")
    tarefas_parser.add_argument("user_id", type=int, help="ID do usuário para listar tarefas")

    # Subcomando para criar um novo usuário
    criar_parser = subparsers.add_parser("criar", help="Criar um novo usuário")
    criar_parser.add_argument("nome", help="Nome do usuário")
    criar_parser.add_argument("username", help="Nome de usuário")
    criar_parser.add_argument("email", help="Email do usuário")

    # Subcomando para atualizar um usuário existente
    atualizar_parser = subparsers.add_parser("atualizar", help="Atualizar um usuário existente")
    atualizar_parser.add_argument("user_id", type=int, help="ID do usuário a ser atualizado")
    atualizar_parser.add_argument("--nome", help="Novo nome do usuário")
    atualizar_parser.add_argument("--username", help="Novo nome de usuário")
    atualizar_parser.add_argument("--email", help="Novo email do usuário")

    # Subcomando para deletar um usuário
    deletar_parser = subparsers.add_parser("deletar", help="Deletar um usuário")
    deletar_parser.add_argument("user_id", type=int, help="ID do usuário a ser deletado")

    args = parser.parse_args()

    try:
        if args.comando == "listar":
            usuarios_lista = usuarios.listar_usuarios()
            for usuario in usuarios_lista:
                print(f"ID: {usuario['id']}, Nome: {usuario['name']}, Email: {usuario['email']}")
        elif args.comando == "tarefas":
            tarefas = usuarios.listar_tarefas_usuario(args.user_id)
            for tarefa in tarefas:
                print(f"Tarefa ID: {tarefa['id']}, Título: {tarefa['title']}, Concluída: {tarefa['completed']}")
        elif args.comando == "criar":
            novo_usuario = usuarios.criar_usuario(args.nome, args.username, args.email)
            print(f"Usuário criado: {novo_usuario}")
        elif args.comando == "atualizar":
            dados = {k: v for k, v in vars(args).items() if k in ["nome", "username", "email"] and v}
            usuario_atualizado = usuarios.atualizar_usuario(args.user_id, **dados)
            print(f"Usuário atualizado: {usuario_atualizado}")
        elif args.comando == "deletar":
            resultado = usuarios.deletar_usuario(args.user_id)
            print(resultado)
        else:
            parser.print_help()
    except requests.HTTPError as erro_http:
        if erro_http.response.status_code == 500:
            print("Erro interno no servidor. A API pode não suportar esta operação.")
        else:
            print(f"Erro HTTP: {erro_http}")
    except Exception as erro:
        print(f"Erro: {erro}")

if __name__ == "__main__":
    main()
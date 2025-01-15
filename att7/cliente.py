import requests
import argparse
import json

BASE_URL = "https://jsonplaceholder.typicode.com/users"
TASKS_URL = "https://jsonplaceholder.typicode.com/todos"

def listar_usuarios():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['name']}, Email: {usuario['email']}")
    else:
        print("Erro ao listar usuários.")

def listar_tarefas_usuario(user_id):
    response = requests.get(f"{TASKS_URL}?userId={user_id}")
    if response.status_code == 200:
        tarefas = response.json()
        for tarefa in tarefas:
            print(f"Tarefa ID: {tarefa['id']}, Título: {tarefa['title']}, Concluída: {tarefa['completed']}")
    else:
        print(f"Erro ao listar tarefas para o usuário {user_id}.")

def criar_usuario(nome, username, email):
    novo_usuario = {
        "name": nome,
        "username": username,
        "email": email
    }
    response = requests.post(BASE_URL, json=novo_usuario)
    if response.status_code == 201:
        print("Usuário criado com sucesso!")
    else:
        print("Erro ao criar usuário.")

def atualizar_usuario(user_id, nome=None, username=None, email=None):
    usuario_atualizado = {}
    if nome:
        usuario_atualizado['name'] = nome
    if username:
        usuario_atualizado['username'] = username
    if email:
        usuario_atualizado['email'] = email

    response = requests.put(f"{BASE_URL}/{user_id}", json=usuario_atualizado)
    if response.status_code == 200:
        print(f"Usuário {user_id} atualizado com sucesso!")
    else:
        print(f"Erro ao atualizar o usuário {user_id}.")

def deletar_usuario(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        print(f"Usuário {user_id} deletado com sucesso!")
    else:
        print(f"Erro ao deletar o usuário {user_id}.")

def main():
    parser = argparse.ArgumentParser(description="CRUD de usuários da JSON Placeholder")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("listar", help="Listar todos os usuários")

    listar_tarefas = subparsers.add_parser("tarefas", help="Listar tarefas de um usuário específico")
    listar_tarefas.add_argument("user_id", type=int, help="ID do usuário para listar as tarefas")

    criar_usuario_parser = subparsers.add_parser("criar", help="Criar um novo usuário")
    criar_usuario_parser.add_argument("nome", help="Nome do usuário")
    criar_usuario_parser.add_argument("username", help="Nome de usuário")
    criar_usuario_parser.add_argument("email", help="Email do usuário")

    atualizar_usuario_parser = subparsers.add_parser("atualizar", help="Atualizar informações de um usuário")
    atualizar_usuario_parser.add_argument("user_id", type=int, help="ID do usuário a ser atualizado")
    atualizar_usuario_parser.add_argument("--nome", help="Novo nome do usuário")
    atualizar_usuario_parser.add_argument("--username", help="Novo nome de usuário")
    atualizar_usuario_parser.add_argument("--email", help="Novo email do usuário")

    deletar_usuario_parser = subparsers.add_parser("deletar", help="Deletar um usuário")
    deletar_usuario_parser.add_argument("user_id", type=int, help="ID do usuário a ser deletado")

    args = parser.parse_args()

    if args.command == "listar":
        listar_usuarios()
    elif args.command == "tarefas":
        listar_tarefas_usuario(args.user_id)
    elif args.command == "criar":
        criar_usuario(args.nome, args.username, args.email)
    elif args.command == "atualizar":
        atualizar_usuario(args.user_id, args.nome, args.username, args.email)
    elif args.command == "deletar":
        deletar_usuario(args.user_id)
    else:
        print("Comando não reconhecido.")

if __name__ == "__main__":
    main()

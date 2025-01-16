import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"
TASKS_URL = "https://jsonplaceholder.typicode.com/todos"

def listar_usuarios():
    response = requests.get(BASE_URL)
    response.raise_for_status()
    return response.json()

def listar_tarefas_usuario(user_id):
    response = requests.get(f"{TASKS_URL}?userId={user_id}")
    response.raise_for_status()
    return response.json()

def criar_usuario(nome, username, email):
    novo_usuario = {
        "name": nome,
        "username": username,
        "email": email
    }
    response = requests.post(BASE_URL, json=novo_usuario)
    response.raise_for_status()
    return response.json()

def atualizar_usuario(user_id, nome=None, username=None, email=None):
    usuario_atualizado = {}
    if nome:
        usuario_atualizado['name'] = nome
    if username:
        usuario_atualizado['username'] = username
    if email:
        usuario_atualizado['email'] = email

    response = requests.put(f"{BASE_URL}/{user_id}", json=usuario_atualizado)
    response.raise_for_status()
    return response.json()

def deletar_usuario(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    response.raise_for_status()
    return {"mensagem": f"Usuário {user_id} deletado com sucesso"}

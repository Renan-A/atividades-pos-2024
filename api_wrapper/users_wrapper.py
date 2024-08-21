import requests

class UserAPI:
    def __init__(self):
        self.api_url = "https://jsonplaceholder.typicode.com/users"

    def list_users(self):
        response = requests.get(self.api_url)
        return response.json() if response.status_code == 200 else []

    def read_user(self, user_id):
        response = requests.get(f"{self.api_url}/{user_id}")
        return response.json() if response.status_code == 200 else None

    def create_user(self, user_data):
        response = requests.post(self.api_url, json=user_data)
        return response.json() if response.status_code == 201 else None

    def update_user(self, user_id, user_data):
        response = requests.put(f"{self.api_url}/{user_id}", json=user_data)
        return response.status_code == 200

    def delete_user(self, user_id):
        response = requests.delete(f"{self.api_url}/{user_id}")
        return response.status_code == 200

def main():
    api = UserAPI()

    while True:
        print("\nMenu:")
        print("1. Listar todos os usuários")
        print("2. Ver detalhes de um usuário")
        print("3. Criar um novo usuário")
        print("4. Atualizar um usuário existente")
        print("5. Deletar um usuário")
        print("0. Sair")
        
        opcao = input("Digite sua escolha: ")

        if opcao == "1":
            users = api.list_users()
            for user in users:
                print(f"{user['id']} - {user['name']}")

        elif opcao == "2":
            user_id = input("Digite o ID do usuário: ")
            user = api.read_user(user_id)
            if user:
                print(user)
            else:
                print("Usuário não encontrado.")

        elif opcao == "3":
            user_data = {}
            user_data["name"] = input("Digite o nome do usuário: ")
            user_data["username"] = input("Digite o username do usuário: ")
            user_data["email"] = input("Digite o email do usuário: ")
            user_address = {}
            user_address["street"] = input("Digite o endereço do usuário: ")
            user_address["city"] = input("Digite a cidade do usuário: ")
            user_data["address"] = user_address

            created_user = api.create_user(user_data)
            if created_user:
                print(f"Usuário criado com sucesso: {created_user['id']}")
            else:
                print("Falha ao criar o usuário.")

        elif opcao == "4":
            user_id = input("Digite o ID do usuário: ")
            existing_user = api.read_user(user_id)
            if existing_user:
                print(f"Editando o usuário: {existing_user['name']}")
                existing_user["name"] = input("Digite o novo nome do usuário: ") or existing_user["name"]
                existing_user["username"] = input("Digite o novo username do usuário: ") or existing_user["username"]
                existing_user["email"] = input("Digite o novo email do usuário: ") or existing_user["email"]
                success = api.update_user(user_id, existing_user)
                print("Usuário atualizado com sucesso." if success else "Falha ao atualizar o usuário.")
            else:
                print("Usuário não encontrado.")

        elif opcao == "5":
            user_id = input("Digite o ID do usuário: ")
            success = api.delete_user(user_id)
            print("Usuário deletado com sucesso." if success else "Falha ao deletar o usuário.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
from xml.dom.minidom import parse
import os

def carregar_cardapio(cardapio_xml):
    dom = parse(cardapio_xml)
    cardapio = dom.documentElement
    return cardapio.getElementsByTagName("prato")

def exibir_menu_principal():
    print("\n" + "=" * 30)
    print("Bem-vindo ao Cardápio!")
    print("1. Listar todos os pratos")
    print("2. Escolher um prato por ID")
    print("3. Sair")
    print("=" * 30)

def listar_pratos(pratos):
    print("\n" + "=" * 10 + " Lista de Pratos " + "=" * 10)
    for prato in pratos:
        prato_id = prato.getAttribute("id")
        prato_nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
        print(f"{prato_id}. {prato_nome}")
    print("=" * 30)

def exibir_detalhes_prato(pratos, prato_id):
    for prato in pratos:
        if prato.getAttribute("id") == prato_id:
            nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
            descricao = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue
            ingredientes = prato.getElementsByTagName("ingrediente")
            preco = prato.getElementsByTagName("preco")[0].firstChild.nodeValue
            calorias = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue
            tempo_preparo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue
            
            print("\n" + "=" * 10 + " Detalhes do Prato " + "=" * 10)
            print(f"Nome: {nome}")
            print(f"Descrição: {descricao}")
            print("Ingredientes:")
            for ingrediente in ingredientes:
                print(f" - {ingrediente.firstChild.nodeValue}")
            print(f"Preço: {preco}")
            print(f"Calorias: {calorias}")
            print(f"Tempo de Preparo: {tempo_preparo}")
            print("=" * 30)
            return
    print("Prato não encontrado!")

def executar_cardapio():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    cardapio_xml_path = os.path.join(current_dir, "cardapio.xml")
    
    pratos = carregar_cardapio(cardapio_xml_path)
    
    while True:
        exibir_menu_principal()
        opcao = input("Digite uma opção: ")
        
        if opcao == "1":
            listar_pratos(pratos)
        elif opcao == "2":
            prato_id = input("Digite o ID do prato: ")
            exibir_detalhes_prato(pratos, prato_id)
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    executar_cardapio()
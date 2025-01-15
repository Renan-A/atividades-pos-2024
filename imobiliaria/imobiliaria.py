from xml.dom.minidom import parse
import os

def carregar_imobiliaria(imobiliaria_xml):
    dom = parse(imobiliaria_xml)
    imobiliaria = dom.documentElement
    return imobiliaria.getElementsByTagName("imovel")


def listar_imoveis(imoveis):
    print("\n" + "=" * 10 + " Lista de Imóveis " + "=" * 10)
    for imovel in imoveis:
        descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue
        valor = imovel.getElementsByTagName("valor")[0].firstChild.nodeValue
        print(f"Descrição: {descricao}, Valor: {valor}")
    print("=" * 30)

def exibir_detalhes_imovel(imoveis, descricao_busca):
    for imovel in imoveis:
        descricao = imovel.getElementsByTagName("descricao")[0].firstChild.nodeValue
        if descricao == descricao_busca:
            id_imovel = imovel.getAttribute("id")
            endereco = imovel.getElementsByTagName("endereco")[0].firstChild.nodeValue
            valor = imovel.getElementsByTagName("valor")[0].firstChild.nodeValue
            print("\n" + "=" * 10 + " Detalhes do Imóvel " + "=" * 10)
            print(f"ID: {id_imovel}")
            print(f"Descrição: {descricao}")
            print(f"Endereço: {endereco}")
            print(f"Valor: {valor}")
            print("=" * 30)
            return
    print("Imóvel não encontrado!")

def exibir_menu_principal():
    print("\n" + "=" * 30)
    print("Bem-vindo à Imobiliária!")
    print("1. Listar todos os imóveis")
    print("2. Buscar imóvel por descrição")
    print("3. Sair")
    print("=" * 30)

def executar_imobiliaria():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    imobiliaria_xml_path = os.path.join(current_dir, "imobiliaria.xml")
    imoveis = carregar_imobiliaria(imobiliaria_xml_path)
    while True:
        exibir_menu_principal()
        opcao = input("Digite uma opção: ")
        
        if opcao == "1":
            listar_imoveis(imoveis)
        elif opcao == "2":
            descricao_busca = input("Digite a descrição do imóvel: ")
            exibir_detalhes_imovel(imoveis, descricao_busca)
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida...")

if __name__ == "__main__":
    executar_imobiliaria()
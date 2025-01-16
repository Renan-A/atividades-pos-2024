from zeep import Client

wsdl_countries = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
wsdl_number_to_words = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

countries_client = Client(wsdl=wsdl_countries)
numbers_client = Client(wsdl=wsdl_number_to_words)

def get_norway_capital():
    country_code = "NO"  
    capital = countries_client.service.CapitalCity(sCountryISOCode=country_code)
    return capital

def convert_number_to_words(number):
    try:
        result = numbers_client.service.NumberToWords(ubiNum=number)
        return result
    except Exception as e:
        return f"Erro ao converter número: {e}"

while True:
    print("\n" + "="*10 + " SOAP CLIENT " + "="*10)
    print("1. Qual é a capital da Noruega?")
    print("2. Converter número por extenso")
    print("0. Sair")
    
    option = input("Escolha uma opção: ").strip()
    
    if option == "0":
        print("Encerrando o programa. Até mais!")
        break

    elif option == "1":
        capital = get_norway_capital()
        print(f"\nA capital da Noruega é: {capital}")
    
    elif option == "2":
        try:
            number = int(input("Digite um número: "))
            result = convert_number_to_words(number)
            print(f"\nO número {number} por extenso é: {result}")
        except ValueError:
            print("Por favor, digite um número válido.")
    
    else:
        print("Opção inválida. Tente novamente.")

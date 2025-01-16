import requests
from xml.dom.minidom import parseString

# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# Função para montar e enviar requisições SOAP
def send_soap_request(function_name, body_content):
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <{function_name} xmlns="http://www.oorsprong.org/websamples.countryinfo">
          {body_content}
        </{function_name}>
      </soap:Body>
    </soap:Envelope>"""
    headers = {
        'Content-Type': 'text/xml; charset=utf-8'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.text

# Função para extrair valores do XML
def parse_xml_response(xml_data, tag_name):
    dom = parseString(xml_data)
    elements = dom.getElementsByTagName(tag_name)
    if elements and elements[0].firstChild:
        return elements[0].firstChild.nodeValue
    return "Informação não encontrada"

# Função para obter a capital
def get_capital(country_code):
    xml_response = send_soap_request("CapitalCity", f"<sCountryISOCode>{country_code}</sCountryISOCode>")
    return parse_xml_response(xml_response, "m:CapitalCityResult")

# Função para obter a população
def get_population(country_code):
    xml_response = send_soap_request("CountryPopulation", f"<sCountryISOCode>{country_code}</sCountryISOCode>")
    return parse_xml_response(xml_response, "m:CountryPopulationResult")

# Função para obter a moeda
def get_currency(country_code):
    xml_response = send_soap_request("CountryCurrency", f"<sCountryISOCode>{country_code}</sCountryISOCode>")
    return parse_xml_response(xml_response, "m:CountryCurrencyResult")

# Função para obter o idioma
def get_language(country_code):
    xml_response = send_soap_request("CountryLanguage", f"<sCountryISOCode>{country_code}</sCountryISOCode>")
    return parse_xml_response(xml_response, "m:CountryLanguageResult")

# Solicita o código do país ao usuário
country_code = input("Digite o código ISO do país (por exemplo, 'NZ' para Nova Zelândia): ").strip().upper()

# Mostra as informações para o país escolhido
print(f"\nInformações para o país com código '{country_code}':")
print(f"Capital: {get_capital(country_code)}")
print(f"População: {get_population(country_code)}")
print(f"Moeda: {get_currency(country_code)}")
print(f"Idioma principal: {get_language(country_code)}")

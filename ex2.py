from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

codigo = input("Digite o codigo do aerodromo ou 0 para sair:")
while codigo != "0":
    try:
        url = "https://www.aisweb.aer.mil.br/?i=aerodromos&codigo="+codigo
        page = urlopen(url)
        page_content = BeautifulSoup(page.read(), 'html.parser')

        # cartas
        cartas = []
        next_s = page_content.select_one('h4:contains("Cartas")').find_next_sibling("h4")
        while next_s.text.find("Rotas Preferenciais") < 0:
            cartas.append(next_s.text)
            next_s = next_s.find_next_sibling("h4")
        
        # taf e metar
        taf = page_content.select_one('h5:contains("TAF")').find_next_sibling("p").text
        metar = page_content.select_one('h5:contains("METAR")').find_next_sibling("p").text

        # nascer e por do sol
        sunrise = page_content.find('sunrise').contents[0]
        sunset = page_content.find('sunset').contents[0]


        print("Aerodromo: {}".format(codigo))
        print("_____\n")
        print("CARTAS:")
        for carta in cartas:
            print("-", carta)
        print("_____\n")
        print("Nascer do sol: {}\nPor do sol   : {}".format(sunrise, sunset))
        print("_____\n")
        print("TAF  : {}\nMETAR: {}".format(taf, metar))
        print("_____\n")
    except:
        print("Algo deu errado. Tente novamente.")

    codigo = input("Digite o codigo do aerodromo ou 0 para sair:")
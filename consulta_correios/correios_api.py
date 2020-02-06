import requests
from bs4 import BeautifulSoup
from unicodedata import normalize
import unidecode
import re


def busca_cep(data_info):

    # Getting data
    data_info = normalize('NFKD', data_info).encode(
        'ASCII', 'ignore').decode('ASCII')
    session = requests.session()
    data = {'relaxation': data_info,
            'TipoCep': 'ALL',
            'semelhante': 'N',
            }

    r = session.post(
        "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm", data)

    content = r.content

    # Parsing
    soup = BeautifulSoup(content, features="html.parser")
    content = soup.find_all('table')
    if content:
        items = content[0].find_all('td')
        data = {
            'address': unidecode.unidecode(re.sub(' - .*', '', items[0].string).strip()),
            'neighborhood': unidecode.unidecode(items[1].string.strip()),
            'city/state': unidecode.unidecode(items[2].string.strip()),
            'zipcode': unidecode.unidecode(items[3].string.strip()),
        }

    else:
        data = {'error': 'Address not found'}

    # Returning data
    return data

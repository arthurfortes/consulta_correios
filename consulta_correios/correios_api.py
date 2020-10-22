import requests
from bs4 import BeautifulSoup
from unicodedata import normalize
import unidecode
import re


def chunks(l, n):
    n = max(1, n)
    return list(l[i:i+n] for i in range(0, len(l), n))


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
        data = []
        items = content[0].find_all('td')
        for info in chunks(items, 4):
            data.append({
                'address': unidecode.unidecode(re.sub('<.*?>', '', str(info[0])).strip()),
                'neighborhood': unidecode.unidecode(info[1].string.strip()),
                'city/state': unidecode.unidecode(info[2].string.strip()),
                'zipcode': unidecode.unidecode(info[3].string.strip()),
            })

    else:
        data = {'error': 'Address not found'}

    # Returning data
    return data

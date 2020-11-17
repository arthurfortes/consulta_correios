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
    
    data = {
        'endereco': data_info.replace(' ','%20'),
            }
    # URl sending the string parameters: 
    #'pagina = %2Fapp%2Fendereco%2Findex.php','tipoCEP = ALL' and 'endereco=data'
    
    url = ('https://buscacep.correios.com.br/app/endereco/carrega-cep-endereco.php?pagina%2Fapp%2Fendereco%2Findex.php&cepaux=&mensagem_alerta=&endereco={endereco}&tipoCEP=ALL'.format(**data))
    
    r = session.get(url)

    content = r.json()

    if content:
        data = []
        items = content['dados']
        for info in items:
            data.append({
                'address': unidecode.unidecode(re.sub('<.*?>', '', str(info['logradouroDNEC'])).strip()),
                'neighborhood': unidecode.unidecode(info['bairro'].strip()),
                'city/state': unidecode.unidecode(info['localidade']+'/'+info['uf'].strip()),
                'zipcode': unidecode.unidecode(info['cep'].strip()),
            })

    else:
        data = {'error': 'Address not found'}

    # Returning data
    return data



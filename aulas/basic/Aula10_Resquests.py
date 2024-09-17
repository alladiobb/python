import requests

def retornaDadosCep(cep):

    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.text)
    print(type(response.json()))
    dadosCep=response.json()
    print(dadosCep['bairro'])


if __name__ == '__main__':
    retornaDadosCep('81670040')
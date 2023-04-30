import requests

def gerar_dados_veiculos(response):
    """coletando o token do response e passando o mesmo no metodo get para trazer os dados"""
    access_token = response.json()
    veiculos = requests.get(f"https://api-data-engineer-test-3bqvkbbykq-uc.a.run.app/token={access_token['API Token']}").json()
    return veiculos

def consumir_api():
    """realizando o acesso ao token através das orientações da proposta do desafio"""
    url = "https://api-data-engineer-test-3bqvkbbykq-uc.a.run.app/user/"
    payload = {
      "full_name": "Gregory Pierroti",
      "email": "gregorypierroti@hotmail.com"
    }
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return gerar_dados_veiculos(response)


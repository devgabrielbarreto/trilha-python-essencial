import requests

cep = int(input("Informe seu CEP (apenas números): "))

url = f"https://viacep.com.br/ws/{cep}/json/"

info = requests.get(url).json()


rua = info["logradouro"]
bairro = info["bairro"]
cidade = info["localidade"]
estado = info["estado"]

print(f"Você mora na rua: {rua}, no bairro: {bairro}, na cidade: {cidade}, no estado: {estado}")
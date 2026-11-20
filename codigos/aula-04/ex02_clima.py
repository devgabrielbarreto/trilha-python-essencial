import requests

cidade = input("Informe a cidade: ")

url = f"https://wttr.in/{cidade}?lang=pt"

resposta = requests.get(url)

print(resposta.text)
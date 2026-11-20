import requests
import webbrowser

url = "https://api.thecatapi.com/v1/images/search"

info = requests.get(url).json()

imagem = info[0]["url"]

print("🌐 Abrindo imagem...")

webbrowser.open(imagem)
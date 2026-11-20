import requests
import webbrowser

url = "https://dog.ceo/api/breeds/image/random"

info = requests.get(url).json()

print("🌐 Abrindo no navegador...")

webbrowser.open(info["message"])
import requests
import webbrowser
from deep_translator import GoogleTranslator


url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

info = requests.get(url).json()

tradutor = GoogleTranslator(source="en", target="pt")

titulo = tradutor.translate(info["title"])
descricao = tradutor.translate(info["explanation"])


print(f"\n📅 Data: {info['date']}")
print(f"🌌 {titulo}")

print("\n📝 DESCRIÇÃO")
print(descricao)

print("\n🌐 Abrindo imagem...")

webbrowser.open(info["url"])
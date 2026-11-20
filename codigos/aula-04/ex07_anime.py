import requests

codigo = input("🎌 Informe o código do anime: ")

url = f"https://api.jikan.moe/v4/anime/{codigo}"

resposta = requests.get(url)

info = resposta.json()["data"]

print(f"🎬 Nome:       {info['title']}")
print(f"⭐ Nota:       {info['score']}")
print(f"📺 Episódios:  {info['episodes']}")
print(f"🎭 Tipo:       {info['type']}")
print(f"📊 Popularidade: {info['popularity']}")

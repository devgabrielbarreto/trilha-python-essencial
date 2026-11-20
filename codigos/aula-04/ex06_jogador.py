import requests

nome = input("⚽ Digite o nome do jogador: ")

url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={nome}"

info = requests.get(url).json()

jogador = info["player"][0]

print(f"👤 Nome:       {jogador['strPlayer']}")
print(f"🏳️ Nacionalidade: {jogador['strNationality']}")
print(f"⚽ Esporte:     {jogador['strSport']}")
print(f"🏟️ Time:        {jogador['strTeam']}")
print(f"🎯 Posição:     {jogador['strPosition']}")

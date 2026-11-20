import requests

ano = int(input("📅 Informe o ano: "))

url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"

feriados = requests.get(url).json()

print("\n" + "=" * 50)
print(f"       📆 FERIADOS DE {ano}")
print("=" * 50)

for f in feriados:
    print(f"📅 {f['date']}  -  🎉 {f['name']}")

print("=" * 50)
print(f"Total de feriados: {len(feriados)}")
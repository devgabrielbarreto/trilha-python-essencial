motorista = input("Nome do motorista: ")
velocidade = float(input("Velocidade registrada (km/h): "))

if velocidade > 60.0:
    print(f"Multa aplicada! {motorista}, você ultrapassou o limite de 60 km/h.")
else:
    print(f"Tudo certo, {motorista}! Velocidade dentro do limite permitido.")
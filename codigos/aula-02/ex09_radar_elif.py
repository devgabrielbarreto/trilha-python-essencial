velocidade = float(input("Velocidade registrada (km/h): "))

if velocidade <= 80.0:
    print("Velocidade permitida. Boa viagem!")
elif velocidade <= 100.0:
    print("MULTA LEVE: Você ultrapassou o limite em até 20 km/h.")
else:
    print("MULTA GRAVE: Excesso de velocidade superior a 20 km/h!")
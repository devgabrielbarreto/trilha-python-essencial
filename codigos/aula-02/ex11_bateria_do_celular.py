bateria = int(input("Qual a porcentagem atual da bateria (%): "))

if bateria >= 80:
    print("Bateria cheia! Uso liberado para o dia todo.")
elif bateria >= 20:
    print("Bateria normal. Nível moderado.")
else:
    print("ALERTA: Bateria fraca! Conecte o carregador.")
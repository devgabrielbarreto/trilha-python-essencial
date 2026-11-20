meta = float(input("Qual é a sua meta de economia (ex: viagem, celular)? R$ "))
total_guardado = 0.0

while total_guardado < meta:
    print(f"Você tem R$ {total_guardado:.2f}. Ainda faltam R$ { meta - total_guardado:.2f}.")
    deposito = float(input("Quanto você vai depositar agora no cofrinho? R$ "))
    total_guardado += deposito

    
print(f"Parabéns! Meta alcançada: R$ {total_guardado:.2f} guardados!")

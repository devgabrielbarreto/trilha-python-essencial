nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros (ex: 1.50): "))

if altura >= 1.40:
    print(f"Entrada liberada, {nome}! Aproveite o passeio.")
else:
    print(f"Acesso não permitido, {nome}. Altura mínima: 1.40 m.")
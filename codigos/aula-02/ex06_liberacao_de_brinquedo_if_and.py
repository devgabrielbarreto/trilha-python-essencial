idade = int(input("Qual sua idade? "))
altura = float(input("Qual sua altura em metros (ex: 1.50): "))

if idade >= 12 and altura >= 1.40:
    print("Entrada liberada no brinquedo!")
else:
    print("Acesso bloqueado por segurança.")
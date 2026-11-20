idade = int(input("Qual sua idade? "))
estudante = input("Possui carteirinha de estudante? (s/n): ")

if idade >= 60 or estudante == "s":
    print("Desconto concedido! Meia-entrada liberada.")
else:
    print("Ingresso no valor normal (inteira).")
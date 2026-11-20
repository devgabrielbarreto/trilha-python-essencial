valor_total = float(input("Qual o valor total da conta? R$ "))
total_pessoas = int(input("A conta será dividida entre quantas pessoas? "))

valor_por_pessoa = valor_total / total_pessoas

print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")



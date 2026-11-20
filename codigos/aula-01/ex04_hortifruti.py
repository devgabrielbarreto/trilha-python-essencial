item = input("Qual fruta/legume você está pesando? ")
preco_kg = float(input(f"Preço do Kg de {item}: R$ "))
peso = float(input("Peso na balança (em Kg, ex: 1.75): "))

total_item = preco_kg * peso

print(f"Pesagem registrada: {peso}kg de {item}")
print(f"Valor total da pesagem: R$ {total_item:.2f}")
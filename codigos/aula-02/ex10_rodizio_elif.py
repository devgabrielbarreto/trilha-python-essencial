idade = int(input("Digite a idade do cliente: "))

if idade < 6:
    print("Categoria: Criança Pequena — Rodízio Grátis!")
elif idade <= 12:
    print("Categoria: Infantil — Rodízio Meia (R$ 35,00).")
elif idade < 65:
    print("Categoria: Adulto — Rodízio Completo (R$ 70,00).")
else:
    print("Categoria: Melhor Idade — Desconto Especial (R$ 50,00).")
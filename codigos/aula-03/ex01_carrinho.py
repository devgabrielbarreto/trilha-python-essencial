total = 0.0
preco = 2

while preco != 0:
    preco = float(input(f"Preço do produto: R$ "))
    total += preco

print(f"Total a pagar pelo carrinho: R$ {total:.2f}")
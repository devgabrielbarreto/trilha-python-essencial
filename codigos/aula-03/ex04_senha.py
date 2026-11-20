senha_correta = 4289

tentativa = 0

print("Iniciando busca automática...")

while tentativa != senha_correta:
    print(f"Testando: {tentativa} -> Incorreta!")
    tentativa += 1  

print("-" * 30)
print(f"Sucesso! A senha correta é: {tentativa}")
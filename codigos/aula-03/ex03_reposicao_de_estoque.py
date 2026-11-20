capacidade_maxima = 100
estoque_atual = 0

while estoque_atual < capacidade_maxima:

    print(f"Estoque atual: {estoque_atual} caixas.")
    chegada = int(input("Quantas caixas acabaram de ser descarregadas? "))
    estoque_atual += chegada

print("Depósito com capacidade máxima atingida! Pausar recebimento de cargas.")
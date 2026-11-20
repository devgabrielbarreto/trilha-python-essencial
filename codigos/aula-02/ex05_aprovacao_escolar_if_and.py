nota = float(input("Digite a nota final: "))
presenca = int(input("Digite a porcentagem de presença (%): "))

if nota >= 6.0 and presenca >= 75:
    print("Aluno APROVADO!")
else:
    print("Aluno REPROVADO.")
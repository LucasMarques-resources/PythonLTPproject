equipas = ["A", "B", "C", "D"]
equipaAtual = 0

for equipa in range(len(equipas) - 1):
    for j in range(equipaAtual + 1, len(equipas)):
        print(f"{equipas[equipaAtual]} x {equipas[j]}")

    equipaAtual += 1
import random

povoado = ["Anões", "Elfos", "Orcs", "Homens", "Dragões"]
quantia_de_combatentes = 200
altura_media = 0
porcentagem_pesados = 0

for i in range(len(povoado)):
    peso, idade, altura = [], [], []
    menores, pesados = 0, 0

    for j in range(quantia_de_combatentes):
        peso.append(random.randint(60, 120))
        idade.append(random.randint(15, 99))
        altura.append(random.randint(120, 215))

        if peso[j] > 80:
            pesados += 1

        if idade[j] < 18:
            menores += 1

    print("----------------------------------------------------------------------------------------")
    print(f"A média de peso do povoado dos {povoado[i]} é: {sum(peso) / len(peso)}kg")
    print(f"Média de altura do povoado dos {povoado[i]} é: {sum(altura) / len(altura)}cm")

    print(f"A quantia de menores de 18 anos no povoado dos {povoado[i]} é {menores}")
    print(f"Porcentagem de mais pesados que 80kg no povoado dos {povoado[i]} é {(pesados / len(peso)) * 100}%")
    print("----------------------------------------------------------------------------------------")

    altura_media += sum(altura) / len(altura) / len(povoado)
    porcentagem_pesados += (pesados / len(peso)) * 100 / len(povoado)

print(f"A Altura média de todos os combatentes dos cinco povoados é: {altura_media}cm")
print(f"A porcentagem de combatentes acima de 80kgs entre todos os combatentes dos cinco povoados é: {porcentagem_pesados}%")
quantos_anoes = 13
soma_pesos = 0
barris_reforcados = 0

nomes, pesos = [], []

for i in range(quantos_anoes):
    nome = input("\n\033[1;34mDigite o nome do anão: ")
    peso = float(input("\033[1;34mDigite o peso do anão: "))
    nomes.append(nome)
    pesos.append(peso)
    if peso > 70:
        print("\033[1;31mUm barril reforçado será necessário\033[1;34m")
        barris_reforcados += 1
    soma_pesos += peso

print("\nA média de peso dos anões é:", soma_pesos/quantos_anoes, "kgs.")
if barris_reforcados > 1:
    print("\033[1;31mSerão necessários", barris_reforcados ,"barris reforçados.\033[1;34m")
elif barris_reforcados <= 0:
    print("\033[1;31mNão serão necessários barris reforçados.\033[1;34m")
else:
    print("\033[1;31mSerá necessário", barris_reforcados ,"barril reforçado.\033[1;34m")
print("\nOs anões resgatados foram:")
print(*nomes, sep = ", ")
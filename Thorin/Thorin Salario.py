#Variáveis
salario_inicial = 1000
salario_atual = 1000
idade = 18
ano = 55
bonus = 0.015

def mostrarstatus(v):
    print("\n\033[1;32m---------Status do personagem---------")
    print("\033[1;34mNome:\033[1;37m Thorin, escudo de Carvalho.")
    if v > 0:
        print("\033[1;34mSalário:\033[1;37m", salario_atual)
    else:
        print("\033[1;34mSalário:\033[1;37m", salario_inicial)
    print("\033[1;34mAno:\033[1;37m", ano + v)
    print("\033[1;34mIdade:\033[1;37m", idade + v)
    print("\033[1;32m--------------------------------------\n")

mostrarstatus(0)

anos_avancados = int(input("Quantos anos você deseja avançar? (Apenas números inteiros):"))

if (idade + anos_avancados < 51):
    for i in range(anos_avancados - 1):
        if anos_avancados <= 1:
            bonus *= 1
        else:
            bonus *= 2
    salario_atual = salario_atual + salario_inicial * bonus
    mostrarstatus(anos_avancados)
else:
    print("Thorin infelizmente teve seu anel derretido e morreu aos", idade + 33, "anos.")
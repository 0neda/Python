smaug_raiva = 100

while smaug_raiva > 5:
    print("----------------------------------------------")
    entrada = int(input("Digite um número para tentar acalmar o Bugão: "))
    if entrada % 2 == 0:
        smaug_raiva -= 20
        print("O Bugão se acalmou um pouco!")
        if smaug_raiva < 5:
            pass
        else:
            print(f"Nível de raiva atual: {smaug_raiva}")
    else:
        smaug_raiva += 10
        print("Você irritou o Bugão!")
        print(f"Nível de raiva atual: {smaug_raiva}")


print("Você conseguiu acalmar o Bugão, parabéns!")
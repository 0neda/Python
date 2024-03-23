import pygame
import pygame_gui as ui
import random as r
import math as m
import definicoes as d
import funcoes as f
import classes as cl

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('recursos/sons/tema-jogo.mp3')
pygame.mixer.music.play(10)

tela = d.tela
inicio = True
status = cl.JanelaStatus()

while d.rodando:
    tempo = d.clock.tick(60) / 1000.0
    
    # CHECK DE GAMEOVER
    if not d.gameover:
        tela.blit(d.FUNDO_JANELA, (0, 0))
        d.mando._mostrarVida()
        if d.mando.pontos >= 350:
            cor_reputacao = '#b3ff00'
        elif 250 < d.mando.pontos < 350:
            cor_reputacao = '#696969'
        elif d.mando.pontos <= 250:
            cor_reputacao = '#ff5e00'
        status._alterarTexto(f"<b>Vida:</b> {d.mando.hp}/{d.mando.hpmax}<br><b>Dano:</b> {d.mando.atk}<br><b>Defesa:</b> {d.mando.dfs}<br><b><font color={cor_reputacao}>Reputação:{d.mando.pontos}</font></b><br><br>{d.mando.inventario()}")
        d.mando._atualizarStats()

        # CHECK DE INICIO (EVITAR CRIAÇÃO DO DIALOGBOX EM LOOP)
        if inicio:
            dialogo = cl.Dialogo(f"A nave do <b>Mandaloriano</b> está com defeito no sistema de viagem pelo hiper espaço. Para chegar no planeta mais próximo, o <b>Mandaloriano</b> passa por uma chuva de meteoritos, que danifica mais ainda a nave, mas vocês conseguem chegar até o planeta.")
            f.botoesAvancar() 
            inicio = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                d.rodando = False
                exit()

            # CHECAGEM DE PRESSIONAMENTO DE BOTÕES
            if event.type == ui.UI_BUTTON_PRESSED:
                # BOTÃO SIM
                if event.ui_element == d.botao_sim:
                    d.inicio_estagio = True
                    if d.estagio_atual == "1":
                        d.estagio_atual = "1A"
                        dialogo._alterarTexto(f"Grogu segue adiante, pega uma pedra e começa a brincar com ela.")

                    if d.estagio_atual == "2":
                        d.estagio_atual = "2A"
                        dialogo._alterarTexto(f"Vocês seguem viagem com o viajante, ao chegar na cidade, o viajante te dá uma Poção de Cura como agradecimento e segue sua viagem.<br>{d.mando._addPontos(250)}")
                        d.mando._addInventario("Poção de Cura", 0, 50, 0, 1)

                    if d.estagio_atual == "3":
                        d.estagio_atual = "3A"
                        dialogo._alterarTexto(f"Chegando no bar, você encontra alguns conhecidos e em consideração aos velhos tempos, eles te dão uma Poção de Cura.<br>Você segue sua viagem até a oficina.<br>{d.mando._addPontos(50)}")
                        d.mando._addInventario("Poção de Cura", 0, 50, 0, 1) 

                    if d.estagio_atual == "4":
                        if d.mando._temInventario("Poção de Cura", 1):
                            d.estagio_atual = "4A"
                            dialogo._alterarTexto(f"Você entrega a poção para o Stormtrooper e sai ileso.<br>{d.mando._rmvPontos(150)}")
                            d.indice_estagio += 1
                            d.mando._rmvInventario("Poção de Cura", 1)
                        else:
                            d.estagio_atual = "4C"
                            dialogo._alterarTexto(f"Você não tem uma poção de cura para entregar, o Stormtrooper te ataca.<br>{d.mando._rmvPontos(150)}")

                    if d.estagio_atual == "6":
                        d.estagio_atual = "6A"
                        dialogo._alterarTexto(f"Você segue Grogu e encontra uma melhoria para seu blaster.<br>{d.mando._addPontos(50)}")
                        d.mando._addInventario("Blaster X", 5, 0, 0, 1) 

                    if d.estagio_atual == "7":
                        d.estagio_atual = "7A"
                        dialogo._alterarTexto(f"Você vai até a cidade e invade o covil. Ao entrar, um bandido começa a disparar contra você.<br>{d.mando._addPontos(50)}")
                    
                    if d.estagio_atual == "8":
                        d.estagio_atual = "8A"
                        dialogo._alterarTexto(f"Você vai a procura do traficante e encontra ele em um canto isolado da cidade.")

                    if d.estagio_atual == "9":
                        d.estagio_atual = "9A"
                        d.quer_algo_traficante = True
                        dialogo._alterarTexto(f"Sim, gostaria de saber o que tem pra oferecer!<br>{d.mando._rmvPontos(50)}", "[Mandaloriano]")

                    if d.estagio_atual == "10":
                        if d.quer_algo_traficante:
                            if d.mando._temInventario("Poção de Cura", 1):
                                d.mando._addInventario("Blaster Y", 10, 0, 0, 1)
                                d.mando._rmvInventario("Poção de Cura", 1)
                                d.estagio_atual = "11C"
                                d.indice_estagio += 1
                            else:
                                d.estagio_atual = "11B"
                                d.indice_estagio += 1                             
                        else:
                            d.estagio_atual = "12"
                            d.indice_estagio += 2

                    if d.estagio_atual == "13":
                        d.estagio_atual = "13X"
                        dialogo._alterarTexto(f"Você confisca a bolacha de Grogu, ele fica notavelmente triste.<br>{d.mando._rmvPontos(500)}")


                # BOTÃO NÃO
                if event.ui_element == d.botao_nao:
                    d.inicio_estagio = True
                    if d.estagio_atual == "1":
                        d.estagio_atual = "1B"
                        dialogo._alterarTexto(f"Você chama Grogu e seguem viagem.")
                    
                    if d.estagio_atual == "2":
                        d.estagio_atual = "2B"
                        dialogo._alterarTexto(f"Você se nega a ajudar o viajante e ele fica irritado.<br>Você segue sua viagem até a cidade.<br>{d.mando._rmvPontos(100)}")
                        d.viajante_irritado = True

                    if d.estagio_atual == "3":
                        d.estagio_atual = "3B"
                        dialogo._alterarTexto(f"Você decide não passar no bar e segue sua viagem até a oficina.")

                    if d.estagio_atual == "4":
                        d.estagio_atual = "4B"

                    if d.estagio_atual == "6":
                        d.estagio_atual = "6B"
                        dialogo._alterarTexto(f"Você prefere não perder o mecânico de vista.")
                    
                    if d.estagio_atual == "7":
                        d.estagio_atual = "7B"
                        dialogo._alterarTexto(f"O mecânico entende que é uma missão perigosa, mas não perde a oportunidade de te zoar.<br>{d.mando._rmvPontos(150)}")
                    
                    if d.estagio_atual == "8":
                        d.estagio_atual = "8B"
                        dialogo._alterarTexto(f"Você prefere não arriscar sua vida e a vida do Grogu e volta para a oficina.<br>{d.mando._rmvPontos(50)}")

                    if d.estagio_atual == "9":
                        d.estagio_atual = "9B"
                        d.quer_algo_traficante = False
                        dialogo._alterarTexto(f"Não, não preciso de mais armas.<br>{d.mando._addPontos(50)}", "[Mandaloriano]")

                    if d.estagio_atual == "10":
                        if d.quer_algo_traficante:
                            d.quer_algo_traficante = False
                        else:
                            d.estagio_atual = "11"
                            d.indice_estagio = 11

                    if d.estagio_atual == "13":
                        d.estagio_atual = "13X"
                        dialogo._alterarTexto(f"Você não confisca a bolacha de Grogu, ele sorri e você nota uma certa expressão de agradecimento.<br>{d.mando._addPontos(1337)}")
                        



                # BOTÃO CURA
                if event.ui_element == d.botao_cura:
                    if d.mando._temInventario("Poção de Cura", 1):
                        d.mando._recuperarVida()


                # BOTÃO AVANÇAR
                if event.ui_element == d.botao_avancar:
                    if d.indice_estagio+1 <= len(d.estagios)-1:
                        if d.estagio_atual == "8B":
                            d.inicio_estagio = True
                            d.indice_estagio = 12
                            d.estagio_atual = "12"
                        elif d.estagio_atual == "11A" or d.estagio_atual == "11B" or d.estagio_atual == "11":
                            d.inicio_estagio = True
                            d.indice_estagio = 11
                            d.estagio_atual = "11X"
                        elif d.estagio_atual == "15A":
                            d.inicio_estagio = True
                            d.indice_estagio = 15
                            d.estagio_atual = "15B"
                        else:
                            d.inicio_estagio = True
                            d.indice_estagio += 1
                            d.estagio_atual = d.estagios[d.indice_estagio]
                    else:
                        dialogo._alterarTexto(f"<b>TÁ QUERENDO MAIS É? A GENTE FAZ UMA DLC POR MAIS UNS 10 PONTOS!</b>")


                # BOTÃO ATACAR
                if event.ui_element == d.botao_atacar:
                    dano_causado = r.randint(m.ceil(d.mando.atk / 2), m.ceil(d.mando.atk * 1.5))
                    dano_recebido = r.randint(m.ceil(d.inimigo.atk - (d.mando.dfs)), m.ceil((d.inimigo.atk * 1.5) - (d.mando.dfs)))
                    d.inimigo._receberDano(dano_causado)
                    if dano_recebido < 0:
                        dano_recebido = 0
                    d.mando._receberDano(dano_recebido)
                    dialogo._batalha(f"Você causou <b>{dano_causado}</b> de dano em seu inimigo.<br>Você recebeu <b>{dano_recebido}</b> de dano.")


                # BOTÃO DEFENDER
                if event.ui_element == d.botao_defender:
                    minimo = m.ceil(d.inimigo.atk - (d.mando.dfs * 1.5))
                    maximo = m.ceil((d.inimigo.atk * 1.5) - (d.mando.dfs * 1.5))

                    if minimo <= 0:
                        minimo = 0

                    dano_causado = r.randint(m.ceil(d.mando.atk / 4), m.ceil(d.mando.atk))
                    dano_recebido = r.randint(minimo, maximo)

                    if dano_recebido < 0:
                        dano_recebido = 0

                    d.inimigo._receberDano(dano_causado)
                    d.mando._receberDano(dano_recebido)
                    dialogo._batalha(f"Você recebeu <b>{dano_recebido}</b> de dano.<br>Você revidou e causou <b>{dano_causado}</b> de dano em seu inimigo.")


            # LOOP HISTÓRIA

            # CHECK DA VIDA DO MANDALORIANO
            if d.mando.hp <= 0:
                d.gameover = True

            # CHECKS DE ESTAGIO ATUAL
            if d.inicio_estagio:
                if d.estagio_atual == "0":
                    f.botoesAvancar()
                    d.inicio_estagio = False

                elif d.estagio_atual == "1":
                    dialogo._escolha(f"Você desce da nave. Grogu parece procurar alguma coisa. Você segue ele?")
                    d.inicio_estagio = False

                elif d.estagio_atual == "2":
                    dialogo._escolha("De longe você vê um homem esquisito se aproximando, trata-se de um viajante perdido.<br>Ao chegar mais perto, ele pede se você pode ajudá-lo a ir até a cidade.")
                    d.inicio_estagio = False

                elif d.estagio_atual == "3":
                    dialogo._escolha(f"Já na cidade, seu objetivo é chegar na oficina mais próxima, mas no meio do caminho tem um bar. Você quer passar no bar antes?")
                    d.inicio_estagio = False
                
                elif d.estagio_atual == "4":
                    dialogo._escolha(f"No meio do caminho, você é abordado por um Stormtrooper. Ele solicita uma poção em troca de te deixar em paz. Você aceita?")
                    d.inicio_estagio = False
                
                elif d.estagio_atual == "4B":
                    dialogo._alterarTexto("O Stormtrooper te ataca.")
                    d.inicio_estagio = False

                elif d.estagio_atual == "4C":
                    dialogo._batalha("Você não tinha poções para entregar. O Stormtrooper te ataca.")
                    d.inicio_estagio = False

                elif d.estagio_atual == "5":
                    f.criarInimigo("Stormtrooper", 50, 10, True, "Poção de Cura", 0, 50, 0, 3)

                elif d.estagio_atual == "6":
                    dialogo._escolha(f"Você chega na oficina, o mecânico fala que vai checar a nave. Enquanto isso, Grogu parece procurar algo. Você segue ele?")
                    d.inicio_estagio = False

                elif d.estagio_atual == "7":
                    dialogo._escolha(f"Você vai com o mecânico até a nave. Ele diz que pode consertar a nave, mas que levará um tempo. Ele diz que um covil de ladrões da cidade possui uma ferramenta que seria muito útil.<br>Você vai até o covil?")
                    d.inicio_estagio = False

                elif d.estagio_atual == "7A":
                    f.criarInimigo("Bandido", 75, 15, True, "Melhoria de Armadura", 0, 0, 10, 1)

                elif d.estagio_atual == "8":
                    dialogo._escolha(f"Enquanto espera o mecânico consertar a nave, você resolve ir atrás de uma missão, para isso, vai até o bar. No bar, você escuta conversas sobre um ex oficial Imperial que está traficando armas. Você quer procurar esse oficial?")
                    d.inicio_estagio = False

                elif d.estagio_atual == "9":
                    dialogo._escolha(f"Você! O que faz aqui? Está a procura de uma arma nova?!", "[Traficante]")
                    d.inicio_estagio = False

                elif d.estagio_atual == "10":
                    if d.quer_algo_traficante:
                        dialogo._escolha("Você pode trocar uma poção de cura por uma melhoria para seu Blaster, te interessa?", "[Traficante]")
                        d.inicio_estagio = False
                    else:
                        dialogo._escolha("Se você não quer nada, é melhor ir embora! Se você ficar, a coisa vai esquentar.<br><b>Você vai embora?</b>", "[Traficante]")
                        d.inicio_estagio = False

                elif d.estagio_atual == "11":
                    dialogo._alterarTexto("O Traficante te ataca.")
                    d.inicio_estagio = False

                elif d.estagio_atual == "11B":
                    dialogo._alterarTexto("Você não tinha poções. O Traficante te ataca.")
                    d.inicio_estagio = False
                    
                elif d.estagio_atual == "11X":
                    f.criarInimigo("Traficante", 75, 20, True, "Blaster Y", 10, 0, 0, 1)
                
                elif d.estagio_atual == "11C":
                    dialogo._alterarTexto(f"Ótimo, pegue essa Blaster Y em troca de uma Poção de Cura e suma da minha frente!", "[Traficante]")
                    d.inicio_estagio = False

                elif d.estagio_atual == "12":
                    dialogo._alterarTexto("Novamente na oficina, o mecânico diz que a nave está pronta para partir.")
                    d.inicio_estagio = False

                elif d.estagio_atual == "13":
                    dialogo._escolha("Você agradece e embarca na nave, mas ao embarcar, nota que Grogu está segurando algo, é uma bolacha azul. Você quer confiscar a bolacha de Grogu?")
                    d.inicio_estagio = False

                elif d.estagio_atual == "14":
                    if d.viajante_irritado:
                        d.estagio_atual = "15A"
                        d.indice_estagio = 15
                    else:
                        d.estagio_atual = "16"
                        d.indice_estagio = 16
                
                elif d.estagio_atual == "15A":
                    dialogo._alterarTexto("Ao olhar para a porta da nave, você nota que o Viajante que resolveu não ajudar no começo da sua jornada está com um Blaster apontado para você.<br><b>O Viajante ataca</b>.")
                    d.inicio_estagio = False
                
                elif d.estagio_atual == "15B":
                    f.criarInimigo("Viajante", 100, 25)

                elif d.estagio_atual == "16":
                    dialogo._alterarTexto(f"<b>Vocês ligam a nave e seguem viagem.")
                    d.inicio_estagio = False

                elif d.estagio_atual == "17":
                    dialogo._alterarTexto(f"<b>FIM DE JOGO, OBRIGADO POR JOGAR!</b><br>Sua reputação final foi: {d.mando.pontos}")
                    d.inicio_estagio = False

            d.gerenciador.process_events(event)


    # ACESSADO CASO GAMEOVER = TRUE
    else:
        # RE-LOOPANDO EVENTOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                d.rodando = False
                exit()

        tela.blit(d.TELA_GAMEOVER, (0, 0))  # DESENHA TELA DE GAMEOVER
        f.esconderInterface(dialogo, status)  # ESCONDE A INTERFACE


    d.gerenciador.update(tempo)
    d.gerenciador.draw_ui(d.tela)
    pygame.display.update()
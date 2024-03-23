import definicoes as d
from classes import Personagem

def botoesAvancar():
    d.botao_sim.disable()
    d.botao_nao.disable()
    d.botao_cura.disable()
    d.botao_atacar.disable()
    d.botao_defender.disable()
    d.botao_avancar.enable()

def botoesBatalha():
    d.botao_sim.disable()
    d.botao_nao.disable()
    if d.mando._temInventario("Poção de Cura", 1):
        d.botao_cura.enable()
    else:
        d.botao_cura.disable()
    d.botao_atacar.enable()
    d.botao_defender.enable()
    d.botao_avancar.disable()

def botoesEscolha():
    d.botao_sim.enable()
    d.botao_nao.enable()
    d.botao_cura.disable()
    d.botao_atacar.disable()
    d.botao_defender.disable()
    d.botao_avancar.disable()

def criarInimigo(nome, vida, ataque, recompensa=False, nomeRecompensa=None, danoRecompensa=None, curaRecompensa=None, defesaRecompensa=None, quantiaRecompensa=None):
    if not d.emBatalha:
        botoesBatalha()
        d.inimigo = Personagem(nome, vida, vida, ataque, 0, "#barrainimigo", "#labelinimigo", (560, 492), (464, 30), nome)
        d.emBatalha = True
    elif d.emBatalha:
        if d.inimigo.hp > 0:
            d.inimigo._mostrarVida()
        else:
            d.inimigo._esconderBarra()
            if d.indice_estagio < len(d.estagios)-1:
                d.indice_estagio += 1
            d.emBatalha = False
            d.estagio_atual = d.estagios[d.indice_estagio]
            botoesAvancar()
            if recompensa:
                d.mando._addInventario(nomeRecompensa, danoRecompensa, curaRecompensa, defesaRecompensa, quantiaRecompensa)

def esconderInterface(box_dialogo, janela_status):
    box_dialogo.box.visible = 0
    d.botao_sim.visible = 0
    d.botao_nao.visible = 0
    d.botao_avancar.visible = 0
    d.botao_defender.visible = 0
    d.botao_atacar.visible = 0
    d.botao_cura.visible = 0
    d.mando._esconderBarra()
    d.inimigo._esconderBarra()
    janela_status._esconderJanela()
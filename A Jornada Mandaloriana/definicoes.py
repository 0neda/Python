import pygame
import pygame_gui as ui
from pygame_gui.core import ObjectID

pygame.init()

pygame.display.set_caption("A jornada Mandaloriana - O começo")
resolucao = (1024, 768)
tela = pygame.display.set_mode(resolucao)
rodando = True
FUNDO_JANELA = pygame.image.load('recursos/backgrounds/main-menu.jpg')
TELA_GAMEOVER = pygame.image.load('recursos/backgrounds/tela-gameover.jpg')
clock = pygame.time.Clock()
inicio_estagio = True

# LISTA COM ESTÁGIOS PRINCIPAIS (INDICE_ESTAGIO)
estagios = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17"
]

quer_algo_traficante = False
viajante_irritado = False

estagio_atual = "0" # O ESTÁGIO ATUAL P/ SER USADO EM BRANCHES (1A, 1B....)
indice_estagio = 0  # O ESTÁGIO PRINCIPAL ATUAL (DEFINIDO PELA LISTA ACIMA)
emBatalha = False   # VARIÁVEL P/ CHECAR SE ESTAMOS EM BATALHA
gameover = False    # VARIÁVEL P/ DEFINIR GAMEOVER OU NÃO

# CRIAÇÃO DA UI:
gerenciador = ui.UIManager(resolucao, 'recursos/tema.json')
botao_sim = ui.elements.UIButton(relative_rect=pygame.Rect((154, 523), (154, 54)), text='Sim', manager=gerenciador, object_id=ObjectID(class_id='@botoes', object_id='#botao_verde'))
botao_nao = ui.elements.UIButton(relative_rect=pygame.Rect((308, 523), (154, 54)), text='Não', manager=gerenciador, object_id=ObjectID(class_id='@botoes', object_id='#botao_vermelho'))
botao_avancar = ui.elements.UIButton(relative_rect=pygame.Rect((0, 523), (154, 54)), text='Avançar', manager=gerenciador, object_id=ObjectID(class_id='@botoes', object_id='#botao_azul'))
botao_atacar = ui.elements.UIButton(relative_rect=pygame.Rect((716, 523), (154, 54)), text='Atacar', manager=gerenciador, object_id=ObjectID(class_id='@botoes', object_id='#botao_roxo'))
botao_defender = ui.elements.UIButton(relative_rect=pygame.Rect((870, 523), (154, 54)), text='Defender', manager=gerenciador, object_id=ObjectID(class_id='@botoes', object_id='#botao_roxo'))
botao_cura = ui.elements.UIButton(relative_rect=pygame.Rect((562, 523), (154, 54)), text='Curar', manager=gerenciador, object_id=ObjectID(class_id='@botoes', object_id='#botao_vermelho'))

rectCaixa = pygame.Rect((0, 576), (1025, 192))
idCaixa = "@caixadialogo"

# CRIAÇÃO DO PERSONAGEM E INIMIGOS:
from classes import Personagem
mando = Personagem("Mandaloriano", 100, 100, 10, 5, "#barramando", "#labelmando", (0, 492), (464, 30))
inimigo = Personagem("Placeholder", 1, 1, 1, 0, "#barrainimigo", "#labelinimigo", (560, 492), (618, 30), "Placeholder")
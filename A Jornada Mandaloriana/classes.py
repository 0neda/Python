import pygame
import pygame_gui as ui
from definicoes import gerenciador, idCaixa, rectCaixa

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Personagem():
    def __init__(self, nome, hpmax, hp, atk, dfs, tema_barra, tema_label, posicao, tamanho, texto="Pontos de Vida"):
        self.nome = nome
        self.hpmax = hpmax
        self.atk = atk
        self.hp = hp
        self.dfs = dfs
        self.pontos = 300
        self.barraVida = ui.elements.UIStatusBar(relative_rect=pygame.Rect(posicao, tamanho), manager=gerenciador, object_id=tema_barra, visible = 0)
        self.labelVida = ui.elements.UILabel(relative_rect=pygame.Rect(posicao, tamanho), manager=gerenciador, object_id=tema_label, text=texto, visible = 0, parent_element=self.barraVida)
        self.itens = []

    def _receberDano(self, damage):
        self.hp -= damage
        
    def _recuperarVida(self):
        for item in self.itens:
            if item['nome'] == "Poção de Cura":
                valor_cura = item['cura']
                if (self.hp + valor_cura) <= self.hpmax:
                    if self._temInventario("Poção de Cura", 1):
                        self.hp += valor_cura
                else:
                    if self._temInventario("Poção de Cura", 1):
                        self.hp = self.hpmax
                self._rmvInventario("Poção de Cura", 1)

    def _mostrarVida(self): 
        self.barraVida.percent_full = self.hp/self.hpmax
        self.barraVida.visible = 1
        self.labelVida.visible = 1
        self.barraVida.update
        self.labelVida.update

    def _esconderBarra(self):
        self.barraVida.visible = 0
        self.labelVida.visible = 0
        self.barraVida.update
        self.labelVida.update

    def _addInventario(self, nome, dano, cura=0, defesa=0, quantia=1):
        item = {'nome': nome, 'dano': dano, 'cura': cura, 'defesa': defesa, 'quantia': quantia, 'usado': False}
        for item_existente in self.itens:
            if item_existente['nome'] == item['nome']:
                item_existente['quantia'] += item['quantia']
                break
        else:
            self.itens.append(item)

    def _rmvInventario(self, nome, quantia=1):
        for item_existente in self.itens:
            if item_existente['nome'] == nome:
                if item_existente['quantia'] > 1:
                    item_existente['quantia'] -= quantia
                    break
                else:
                    self.itens.remove(item_existente)

    def _temInventario(self, nome, quantia):
        for item_existente in self.itens:
            if item_existente['nome'] == nome:
                if item_existente['quantia'] >= quantia:
                    return True
                else:
                    return False

    def inventario(self):
        if not self.itens:
            return "<b>Nenhum item no inventário</b>"
        else:
            inventario = ""
            for item in self.itens:
                if item['cura'] > 0:
                    tipo__item = (f"<b>Cura:</b> {str(item['cura'])}")
                elif item['dano'] > 0:
                    tipo__item = (f"<b>Dano Bonus:</b> {str(item['dano'])}")
                elif item['defesa'] > 0:
                    tipo__item = (f"<b>Defesa Bonus:</b> {str(item['defesa'])}")
                inventario += f"<b>{str(item['nome'])}</b><br>    <b>Quantia:</b> {str(item['quantia'])}</b><br>    {tipo__item}<br>"
            return inventario

    def _atualizarStats(self):  # FUNÇÃO PARA ATUALIZAR OS STATUS CONFORME OS STATUS DE DANO/DEFESA DOS ITENS ADICIONADOS AO INVENTÁRIO
        if self.itens:
            for item in self.itens:
                if not item['usado']:
                    if item['dano'] > 0:
                        item['usado'] = True
                        self.atk += item['dano']
                    elif item['defesa'] > 0:
                        item['usado'] = True
                        self.dfs += item['defesa']

    def _addPontos(self, pontos):  # FUNÇÃO P/ ADICIONAR REPUTAÇÃO E RETORNAR O TEXTO
        self.pontos += pontos
        return f"<b><font color='#b3ff00'>Reputação +{pontos}</font></b></effect>"
        
    def _rmvPontos(self, pontos):  # FUNÇÃO P/ REMOVER REPUTAÇÃO E RETORNAR O TEXTO DE ACORDO COM A QUANTIA ATUAL DE REPUTAÇÃO
        if self.pontos >= pontos:
            self.pontos -= pontos
            return f"<b><b><font color='#ff5e00'>Reputação -{pontos}</font></b></effect>"
        else:
            self.pontos = 0
            return f"<b><font color='#ff5e00'>Você conseguiu atingir o fundo do poço, sua reputação ZEROU, você é um fracasso, parabéns!</font></b>"


class JanelaStatus():
    def __init__(self):
        self.janela = ui.elements.UIPanel(object_id="@painelstatus", relative_rect=pygame.Rect((0, 0), (462, 462)), manager=gerenciador, visible=1)
        self.texto = ui.elements.UITextBox(object_id="@textostatus", relative_rect=self.janela.rect, container=self.janela, manager=gerenciador, html_text="", visible=1)
    
    def _esconderJanela(self):
        self.janela.visible = 0
        self.texto.visible = 0
        self.janela.update
        self.texto.update

    def _alterarTexto(self, texto):
        self.texto.set_text(texto)


import funcoes as f

class Dialogo():
    def __init__(self, texto, locutor="[História]"):
        self.box = ui.elements.UITextBox(html_text=f"<b>{locutor}</b><br>{texto}", relative_rect=rectCaixa, manager=gerenciador, object_id=idCaixa)
        self.box.set_active_effect(ui.TEXT_EFFECT_TYPING_APPEAR, params={'time_per_letter': 0.015})

    def _alterarTexto(self, texto="Placeholder", locutor="[História]"):
        self.box.set_text(f"<b>{locutor}</b><br>{texto}")
        self.box.set_active_effect(ui.TEXT_EFFECT_TYPING_APPEAR, params={'time_per_letter': 0.015})
        f.botoesAvancar()     

    def _escolha(self, texto="Placeholder", locutor="[Escolha]"):
        self.box.set_text(f"<b>{locutor}</b><br>{texto}")
        self.box.set_active_effect(ui.TEXT_EFFECT_TYPING_APPEAR, params={'time_per_letter': 0.015})
        f.botoesEscolha()

    def _batalha(self, texto="Placeholder", locutor="[Batalha]"):
        self.box.set_text(f"<b>{locutor}</b><br>{texto}")
        self.box.set_active_effect(ui.TEXT_EFFECT_TYPING_APPEAR, params={'time_per_letter': 0.015})
        f.botoesBatalha
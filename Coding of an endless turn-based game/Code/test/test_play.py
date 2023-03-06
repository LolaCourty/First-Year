############
# Python 3.8
#
# Coding Weeks
# Semaine 2 : Jeu de Combat
# test_personnage.py
#
# Equipe 23 :
# Chardin Hugues
# Courty Lola
# Martin Gabriel
# Rouby Morgane
# Sebban Soufiane
#
# Creation Date : Nov. 16th 2020
# Last Modif : Nov. 16th 2020
############

import os
import sys
dossier_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dossier_parent)

import builtins
import pytest
from src.play import *
from src.textual import *
from src.personnage import *
from parametres import *

def test_init(monkeypatch):

    name = 'Maxime'
    def mock_input_return(input):
        return name
    monkeypatch.setattr('builtins.input', mock_input_return)
    score, hero, monster = init()
    assert score == 0
    assert monster.name == 'Pabo' or monster.name == 'Gromauch' or monster.name == 'Touvisqeut'

def test_tour_du_heros(monkeypatch):
    score = 0
    hero = Hero()
    monster = Monster()
    monster.pv = 0

    def mock_input_return(prompt):
        prompt_to_return_val = {ASK_PLAYER_ACTION : "Attendre",
        "Que voulez-vous acheter ? Arme, Bouclier, Armure, Chaussures, Endurance ou Potion de soin ou d'énergie ? " : "Bouclier",
        "Voulez-vous acheter autre chose ? Oui/Non" : "Non"}
        return prompt_to_return_val[prompt]
    monkeypatch.setattr('builtins.input', mock_input_return)
    score, monster = tour_du_heros(monster, hero, score)
    
    assert monster.pv > 0
    assert score > 0

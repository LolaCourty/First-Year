############
# Python 3.8
#
# Coding Weeks
# Semaine 2 : Jeu de Combat
# test_textual.py
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

import pytest
import builtins
from src.textual import *
from parametres import *
from src.personnage import *


def test_read_player_action(monkeypatch):
    """ Trois actions possible : Attendre, Se soigner, Attaquer (Small, Medium, Big) """
   
    action = 'Attendre'
    def mock_input_return(input):
        return action
    monkeypatch.setattr('builtins.input', mock_input_return)
    assert read_player_action() == [action, None]

    action = 'Se soigner'
    def mock_input_return(input):
        return action
    monkeypatch.setattr('builtins.input', mock_input_return)
    assert read_player_action() == [action, None]

    action = 'Attaquer'
    for sous_action in ATTAQUES:
        def mock_input_return(prompt):
            prompt_to_return_val = {ASK_PLAYER_ACTION : action,
            ASK_PLAYER_ATTAQUE : sous_action}
            return prompt_to_return_val[prompt]
        monkeypatch.setattr('builtins.input', mock_input_return)
        assert read_player_action() == [action, sous_action]
    
    action = 'Bonjour'
    def mock_input_return(prompt):
        prompt_to_return_val = {ASK_PLAYER_ACTION : action,
        ASK_PLAYER_ACTION_WHEN_WRONG : 'Attendre'}
        return prompt_to_return_val[prompt]
    monkeypatch.setattr('builtins.input', mock_input_return)
    assert read_player_action() == ['Attendre', None]

    action = 'Attaquer'
    sous_action = 'Bonjour'
    def mock_input_return(prompt):
        prompt_to_return_val = {ASK_PLAYER_ACTION : action,
        ASK_PLAYER_ATTAQUE : sous_action,
        ASK_PLAYER_ATTAQUE_WHEN_WRONG : 'Attaque faible'}
        return prompt_to_return_val[prompt]
    monkeypatch.setattr('builtins.input', mock_input_return)
    assert read_player_action() == [action, 'Attaque faible']

def test_print_pv(capsys):
    hero = Hero()
    print_pv(hero)
    captured = capsys.readouterr()
    assert captured.out == 'Vous avez encore ' + str(hero.pv) + ' points de vie ! Pas plus de quelques bobos.\n'
    
    hero.pv = 60
    print_pv(hero)
    captured = capsys.readouterr()
    assert captured.out =='Vous avez encore ' + str(hero.pv) + ' points de vie ! Soyez prudent, vous commencez ?? saigner du nez.\n'
    
    hero.pv = 30
    print_pv(hero)
    captured = capsys.readouterr()
    assert captured.out == 'Vous avez encore ' + str(hero.pv) + ' points de vie ! Votre vision se trouble et votre souffle devient court, mais vous pouvez encore combattre.\n'
    
    hero.pv = 10
    print_pv(hero)
    captured = capsys.readouterr()
    assert captured.out == 'Vous avez encore ' + str(hero.pv) + " points de vie ! Vous ??tes ?? l'article de la mort, priez votre dieu si vous voulez survivre.\n"

    monster = Monster()
    print_pv(monster)
    captured = capsys.readouterr()
    assert captured.out == "Ce " + monster.name + ' a encore ' + str(monster.pv) + " points de vie ! Il n'a pas encore compris que vous lui tapiez dessus.\n"
    
    monster.pv = 15
    print_pv(monster)
    captured = capsys.readouterr()
    assert captured.out == "Ce " + monster.name + ' a encore '  + str(monster.pv) + ' points de vie ! Il commence ?? sentir les coups, mais pas assez pour avoir peur.\n' 
    
    monster.pv = 8
    print_pv(monster)
    captured = capsys.readouterr()
    assert captured.out == "Ce " + monster.name + ' a encore ' + str(monster.pv) + " points de vie ! L?? il commence ?? r??aliser en quoi l'homme est sup??rieur et pourquoi il a pu imposer les grattes-ciel ?? M??re Nature.\n"
    
    monster.pv = 2
    print_pv(monster)
    captured = capsys.readouterr()
    assert captured.out == "Ce " + monster.name + ' a encore ' + str(monster.pv) + " points de vie ! La SPA veut conna??tre votre localisation, d??p??chez-vous de l'achever.\n"

def test_print_energy(capsys):
    hero = Hero()
    print_energy(hero)
    captured = capsys.readouterr()
    assert captured.out == 'Vous avez encore ' + str(hero.energy) + " points d'??nergie ! Vous pourriez faire ??a toute la semaine.\n"

    hero.energy = 60
    print_energy(hero)
    captured = capsys.readouterr()
    assert captured.out =='Vous avez encore ' + str(hero.energy) + " points d'??nergie ! ??a commence ?? tirer dans les bras mais le plus important c'est le mental.\n"

    hero.energy = 30
    print_energy(hero)
    captured = capsys.readouterr()
    assert captured.out == 'Vous avez encore ' + str(hero.energy) + " points d'??nergie ! Vous vous mettez ?? regretter d'avoir s??ch?? l'EPS plus jeune, mais c'est trop tard pour revenir en arri??re.\n"
    
    hero.energy = 10
    print_energy(hero)
    captured = capsys.readouterr()
    assert captured.out == 'Vous avez encore ' + str(hero.energy) + " points d'??nergie ! Votre coup de poing ?? la capacit?? offensive d'une douche un peu trop ti??de, il vous est recommand?? de vous reposer tr??s vite.\n"

def test_print_score(capsys):
    score = 100
    print_score(score)
    captured = capsys.readouterr()
    assert captured.out == "Votre score est de " + str(score) + '\n'

def test_read_category_wanted(monkeypatch):
    """ 'Combattant ?? pied', 'Combattant mont??', 'Mage', 'Support' """
    for category in ['Combattant ?? pied', 'Combattant mont??', 'Mage', 'Support']:
        def mock_input_return(input):
            return category
        monkeypatch.setattr('builtins.input', mock_input_return)
        assert read_category_wanted() == [category]
    
    category = 'Bonjour'
    def mock_input_return(prompt):
        prompt_to_return_val = {ASK_PLAYER_CATEGORY : category,
        ASK_PLAYER_CATEGORY_WHEN_WRONG : 'Combattant ?? pied'}
        return prompt_to_return_val[prompt]
    monkeypatch.setattr('builtins.input', mock_input_return)
    assert read_category_wanted() == ['Combattant ?? pied']

def test_read_name_hero(monkeypatch):
    def mock_input_return(input):
            return 'Maxime'
    monkeypatch.setattr('builtins.input', mock_input_return)
    name = read_name_hero()
    assert name == 'Maxime'

############
# Python 3.8
#
# Coding Weeks
# Semaine 2 : Jeu de Combat
# textual.py
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

from src.personnage import *
from src.play import *
from parametres import *
from math import floor

def read_player_action():
    """ Input -> liste [action, sous-action]
    Demande et lit l'action (et potentiellement la sous-action) du héros
    S'il n'y a pas de sous-action, retourne (action, None) """

    action = input(ASK_PLAYER_ACTION)
    while action not in ACTIONS:
        action = input(ASK_PLAYER_ACTION_WHEN_WRONG)
    if action == ACTIONS[2]:
        sous_action = input(ASK_PLAYER_ATTAQUE)
        while sous_action not in ATTAQUES:
            sous_action = input(ASK_PLAYER_ATTAQUE_WHEN_WRONG)
    else:
        sous_action = None
    return [action, sous_action]


def print_score(score):
    """ Affiche le score du joueur """
    print(SCORE + str(score))

def read_category_wanted():
    """ Input -> liste [catégorie, None (prochainement la sous-catégorie)]
    Demande et lit la catégorie du héros """

    category = input(ASK_PLAYER_CATEGORY)
    while category not in CATEGORIES:
        category = input(ASK_PLAYER_CATEGORY_WHEN_WRONG)
    
    return [category]

def read_name_hero():
    name = input(ASK_HERO_NAME)
    return name

def fin_du_tour(monster, hero):
    if monster.pv == monster.pv_max :
        print(ANNONCE_PV_MONSTER(monster.name, monster.pv))
    else :
        print_pv(monster)

def init():
    score = 0
    hero = Hero(name=read_name_hero())
    rand = randint(1,3)
    if rand == 1:
        name = NAMES_MONSTERS[0]
    elif rand == 2:
        name = NAMES_MONSTERS[1]
    elif rand == 3:
        name = NAMES_MONSTERS[2]
    monster = Monster(name=name)
    level = 0
    return score, hero, monster, level


def tour_du_heros(monster, hero, score):
    print_pv(hero)
    print_energy(hero)
    action = read_player_action()
    while action[0] == ACTIONS[2] and not hero.has_enough_energy(action[1]):
        print(NOT_ENOUGH_ENERGY)
        print_energy(hero)
        action = read_player_action()
    hero.make_action(monster, action[0], action[1])
    if monster.is_dead():
        print(DEAD_MONSTER_MSG)
        score, monster, level = endless_monster(hero, monster, score, level)
        print_score(score)
        amelioration(hero)
    return score, monster

def amelioration(hero):
    """ hero, Input --> Augmentation """
    encore = True
    while encore:
        equipement = input(ASK_SHOP)
        while equipement not in SHOP_ITEMS or SHOP[equipement][0] > hero.money:
            equipement = input(ASK_SHOP_WHEN_WRONG)
        hero.money -= SHOP[equipement][0]
        if equipement == SHOP_ITEMS[0]:
            hero._attaque += SHOP[equipement][1]
        elif equipement == SHOP_ITEMS[1]:
            hero._defense += SHOP[equipement][1]
        elif equipement == SHOP_ITEMS[2]:
            hero._pv_max += SHOP[equipement][1]
        elif equipement == SHOP_ITEMS[3]:
            hero._initiative += SHOP[equipement][1]
        elif equipement == SHOP_ITEMS[4]:
            hero._energy_max += SHOP[equipement][1]
        elif equipement == SHOP_ITEMS[5]:
            hero.pv = hero.pv_max
        elif equipement == SHOP_ITEMS[6]:
            hero.energy = hero.energy_max
        
        print(ANNONCE_MONEY(hero.money))
        encore = input(ASK_KEEP_BUYING)
        if encore == 'Non' or encore == 'non' :
            encore = False

def game_play():
    score, hero, monster, level = init()
    while not hero.is_dead():
        # on regarde l'initiative pour définir qui agit en premier
        if hero.initiative < monster.initiative :
            monster.monster_attack(hero)
            # on sort de la boucle lorsque le héro décède
            if hero.is_dead():
                return DEAD_MSG
            score, monster = tour_du_heros(monster, hero, score)
            fin_du_tour(monster, hero)
        elif hero.initiative > monster.initiative :
            score, monster = tour_du_heros(monster, hero, score)
            monster.monster_attack(hero)
            #on sort de la boucle lorsque le héro décède
            if hero.is_dead():
                return DEAD_MSG
            fin_du_tour(monster, hero)
        else :
            #si les deux personnages ont la même initiative, on tire à pile ou face
            rd = randint(1,2)
            if rd == 1:
                monster.monster_attack(hero)
                #on sort de la boucle lorsque le héro décède
                if hero.is_dead():
                    return DEAD_MSG
                score, monster = tour_du_heros(monster, hero, score)
                fin_du_tour(monster, hero)
            else:
                score, monster = tour_du_heros(monster, hero, score)
                monster.monster_attack(hero)
                # on sort de la boucle lorsque le héros décède
                if hero.is_dead():
                    return DEAD_MSG
                fin_du_tour(monster, hero)  

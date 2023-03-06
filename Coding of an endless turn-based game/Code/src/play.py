############
# Python 3.8
#
# Coding Weeks
# Semaine 2 : Jeu de Combat
# play.py
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

from random import randint
from src.personnage import *


def endless_monster(hero, monster, score, level):
    """ si un monstre meurt, un autre tout frais prend sa place et on met à jour l'argent et le score du héros"""
    hero.money += monster.loot
    level += 1
    a = random.randint(1,3)
    if a == 1:
        monster = Monster(NAMES_MONSTERS[0], level)
    elif a == 2:
        monster = Monster(NAMES_MONSTERS[1], level)
    else :
        monster = Monster(NAMES_MONSTERS[2], level)
    score += GAIN_SCORE
    
    return score, monster, level
def print_pv(personnage):
    '''Affiche les PVs du perso ciblé.'''
   
    if type(personnage) == Hero:
        if personnage.pv >= personnage.pv_max * 0.8:
            res = ANNONCE_PV_HERO(personnage.pv) + PV_HERO_HIGH
            print(res)
            return res
        elif personnage.pv < personnage.pv_max * 0.8 and personnage.pv >= personnage.pv_max * 0.5:
            res = ANNONCE_PV_HERO(personnage.pv) + PV_HERO_GOOD
            print(res)
            return res
        elif personnage.pv < personnage.pv_max * 0.5 and personnage.pv >= personnage.pv_max * 0.2:
            res = ANNONCE_PV_HERO(personnage.pv) + PV_HERO_LOW
            print(res)
            return res
        elif personnage.pv < personnage.pv_max *0.2:
            res = ANNONCE_PV_HERO(personnage.pv) + PV_HERO_BAD
            print(res)
            return res

    if type(personnage) == Monster:
        if personnage.pv >= personnage.pv_max * 0.8:
            res = ANNONCE_PV_MONSTER(personnage.name, personnage.pv) + PV_MONSTER_HIGH
            print(res)
            return res
        elif personnage.pv < personnage.pv_max * 0.8 and personnage.pv >= personnage.pv_max * 0.5:
            res = ANNONCE_PV_MONSTER(personnage.name, personnage.pv) + PV_MONSTER_GOOD
            print(res)
            return res
        elif personnage.pv < personnage.pv_max * 0.5 and personnage.pv >= personnage.pv_max * 0.2:
            res = ANNONCE_PV_MONSTER(personnage.name, personnage.pv) + PV_MONSTER_LOW
            print(res)
            return res
        elif personnage.pv < personnage.pv_max * 0.2:
            res = ANNONCE_PV_MONSTER(personnage.name, personnage.pv) + PV_MONSTER_BAD
            print(res)
            return res

def print_energy(hero):

        if hero.energy >= hero.energy_max * 0.8:
            print(ANNONCE_ENERGY(hero.energy) + ENERGY_HIGH)
            return ANNONCE_ENERGY(hero.energy) + ENERGY_HIGH
        elif hero.energy < hero.energy_max * 0.8 and hero.energy >= hero.energy_max * 0.5:
            print(ANNONCE_ENERGY(hero.energy) + ENERGY_GOOD)
            return ANNONCE_ENERGY(hero.energy) + ENERGY_GOOD
        elif hero.energy < hero.energy_max * 0.5 and hero.energy >= hero.energy_max * 0.2:
            print(ANNONCE_ENERGY(hero.energy) + ENERGY_LOW)
            return ANNONCE_ENERGY(hero.energy) + ENERGY_LOW
        elif hero.energy < hero.energy_max *0.2:
            print(ANNONCE_ENERGY(hero.energy) + ENERGY_BAD)
            return ANNONCE_ENERGY(hero.energy) + ENERGY_BAD
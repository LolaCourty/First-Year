############
# Python 3.8
#
# Coding Weeks
# Semaine 2 : Jeu de Combat
# fonctions_grpahique.py
#
# Equipe 23 :
# Chardin Hugues
# Courty Lola
# Martin Gabriel
# Rouby Morgane
# Sebban Soufiane
#
# Creation Date : Nov. 18th 2020
# Last Modif : Nov. 18th 2020
############

import os
import sys
dossier_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dossier_parent)

from src.personnage import *
from parametres import *

def read_player_action():
    """ Input -> liste [action, sous-action]
    Demande et lit l'action (et potentiellement la sous-action) du héros
    S'il n'y a pas de sous-action, retourne (action, None) """

    action = input(ASK_PLAYER_ACTION)
    while action not in ACTIONS:
        action = input(ASK_PLAYER_ACTION_WHEN_WRONG)
    if action == 'Attaquer':
        sous_action = input(ASK_PLAYER_ATTAQUE)
        while sous_action not in ATTAQUES:
            sous_action = input(ASK_PLAYER_ATTAQUE_WHEN_WRONG)
    else:
        sous_action = None
    return [action, sous_action]

def print_pv(character):
    '''Affiche les PVs du perso ciblé.'''
    pv = character.pv
    pvm = character.pv_max

    if type(character) == Heros:
        if pv >= pvm * 0.8:
            res = 'Vous avez encore ' + str(pv) + ' points de vie ! Pas plus de quelques bobos.'
            return res
        elif pv < pvm*0.8 and pv >= pvm * 0.5:
            res = 'Vous avez encore ' + str(pv) + ' points de vie ! Soyez prudent, vous commencez à saigner du nez.'
            return res
        elif pv < pvm*0.5 and pv >= pvm * 0.2:
            res = 'Vous avez encore ' + str(pv) + ' points de vie ! Votre vision se trouble et votre souffle devient court, mais vous pouvez encore combattre.'
            return res
        elif pv < pvm*0.2:
            res = 'Vous avez encore ' + str(pv) + " points de vie ! Vous êtes à l'article de la mort, priez votre dieu si vous voulez survivre."
            return res

    if type(character) == Monster:
        if pv >= pvm * 0.8:
            res = "Ce " +character.name + ' a encore ' + str(pv) + " points de vie ! Il n'a pas encore compris que vous lui tapiez dessus."
            return res
        elif pv < pvm*0.8 and pv >= pvm * 0.5:
            res = "Ce " +character.name + ' a encore '  + str(pv) + ' points de vie ! Il commence à sentir les coups, mais pas assez pour avoir peur.'
            return res
        elif pv < pvm*0.5 and pv >= pvm * 0.2:
            res = "Ce " +character.name + ' a encore ' + str(pv) + " points de vie ! Là il commence à réaliser en quoi l'homme est supérieur et pourquoi il a pu imposer les grattes-ciel à Mère Nature."
            return res
        elif pv < pvm*0.2:
            res = "Ce " +character.name + ' a encore ' + str(pv) + " points de vie ! La SPA veut connaître votre localisation, dépêchez-vous de l'achever."
            return res

def print_energy(hero):
        en = hero.energie
        enm = hero.energie_max

        if en >= enm * 0.8:
            res = 'Vous avez encore ' + str(en) + " points d'énergie ! Vous pourriez faire ça toute la semaine."
            return res
        elif en < enm*0.8 and en >= enm * 0.5:
            res = 'Vous avez encore ' + str(en) + " points d'énergie ! Ça commence à tirer dans les bras mais le plus important c'est le mental."
            return res
        elif en < enm*0.5 and en >= enm * 0.2:
            res = 'Vous avez encore ' + str(en) + " points d'énergie ! Vous vous mettez à regretter d'avoir séché l'EPS plus jeune, mais c'est trop tard pour revenir en arrière."
            return res
        elif en < enm*0.2:
            res = 'Vous avez encore ' + str(en) + " points d'énergie ! Votre coup de poing à la capacité offensive d'une douche un peu trop tiède, il vous est recommandé de vous reposer très vite."
            return res

def print_score(score):
    """ Affiche le score du joueur """
    res = "Votre score est de " + str(score)
    return res

def read_categorie_wanted():
    """ Input -> liste [catégorie, None (prochainement la sous-catégorie)]
    Demande et lit la catégorie du héros """

    categorie = input(ASK_PLAYER_CATEGORIE)
    while categorie not in CATEGORIES:
        categorie = input(ASK_PLAYER_CATEGORIE_WHEN_WRONG)
    
    sous_categorie = None
    return [categorie, sous_categorie]

def read_name_heros():
    name = input("Veuillez choisir un nom pour votre héros : ")
    return name

def amelioration(heros):
    """ heros, Input --> Augmentation """
    equipement = input("Que voulez-vous acheter ? Arme, Bouclier, Armure, Chaussures, Endurance ou Potion de soin ou d'énergie ? ")
    while equipement not in AMELIORATIONS or AMELIORATIONS[equipement] > self.argent:
        equipement = input("C'est impossible. Que voulez-vous améliorer ? Arme, Bouclier, Armure, Chaussures ou Endurance, Potion de soin ou d'énergie ? ")
    heros.argent -= AMELIORATIONS[equipement]
    if equipement == 'Arme':
        heros._attaque += 2
    elif equipement == "Potion d'énergie":
        heros.energie = heros.energie_max
    elif equipement == 'Bouclier':
        heros._defense += 2
    elif equipement == 'Armure':
        heros._pv_max += 10
    elif equipement == 'Chaussures':
        heros._initiative += 1
    elif equipement == 'Potion de soin':
        heros.pv = heros.pv_max
    else: # equipement == 'Endurance'
        heros._energie_max += 10

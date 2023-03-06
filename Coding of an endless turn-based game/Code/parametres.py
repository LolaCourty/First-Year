############
# Python 3.8
#
# Coding Weeks
# Semaine 2 : Jeu de Combat
# parametres.py
#
# Equipe 23 :
# Chardin Hugues
# Courty Lola
# Martin Gabriel
# Rouby Morgane
# Sebban Soufiane
#
# Creation Date : Nov. 13th 2020
# Last Modif : Nov. 14th 2020
############

from math import floor

""" Ce fichier contient les paramètres nécessaires au jeu """

# Données par défault
CATEGORY_INIT = 'Combattant à pied'  # Le choix de la catégorie n'est finalement pas implanté
MONSTER_INIT = 'Pabo'  # Utilisé uniquement pour les tests

# Données nécessaires au jeu

CATEGORIES = {'Combattant à pied' : {'pv max' : 100, 'attaque' : 5, 'defense' : 5, 'initiative' : 0, 'energy max' : 100, 'money' : 0},
                'Combattant monté': {'pv max' : 100, 'attaque' : 5, 'defense' : 5, 'initiative' : 0, 'energy max' : 100, 'money' : 0},
                'Mage' : {'pv max' : 100, 'attaque' : 5, 'defense' : 5, 'initiative' : 0, 'energy max' : 100, 'money' : 0},
                'Support' : {'pv max' : 100, 'attaque' : 5, 'defense' : 5, 'initiative' : 0, 'energy max' : 100, 'money' : 0}}

NAMES_MONSTERS = ['Pabo', 'Gromauch', 'Touvisqeut']
MONSTERS = {NAMES_MONSTERS[0] : {'pv max' : 20, 'attaque' : 1, 'defense' : 3, 'initiative' : 3, 'loot' : 50},
            NAMES_MONSTERS[1] : {'pv max' : 80, 'attaque' : 3, 'defense' : 3, 'initiative' : 1, 'loot' : 50},
            NAMES_MONSTERS[2] : {'pv max' : 50, 'attaque' : 2, 'defense' : 3, 'initiative' : 2, 'loot' : 50}}

ACTIONS = ['Attendre', 'Se soigner', 'Attaquer']
ATTAQUES = ['Attaque faible', 'Attaque moyenne',  'Attaque puissante']
SHOP_ITEMS = ['Arme', 'Bouclier','Armure', 'Chaussures', 'Endurance', 'Potion de soin', "Potion d'énergie"]
SHOP = {SHOP_ITEMS[0] : [30, 2],  # [cout, nombre de points que ça ajoute]
        SHOP_ITEMS[1] : [10, 2],
        SHOP_ITEMS[2] : [10, 5],
        SHOP_ITEMS[3] : [20, 1],
        SHOP_ITEMS[4] : [30, 10],
        SHOP_ITEMS[5] : [50, None],
        SHOP_ITEMS[6] : [50, None]}

HEALING = 20
WAITING = 20
COUT_ATTAQUE_FAIBLE = 10
DEGATS_ATTAQUE_FAIBLE = [5, 15]
COUT_ATTAQUE_MOYENNE = 30
DEGATS_ATTAQUE_MOYENNE = [20, 30]
COUT_ATTAQUE_PUISSANTE = 50
DEGATS_ATTAQUE_PUISSANTE = [35, 55]
GAIN_SCORE = 100

# Formules de calcul des dégâts

def malus(defense, degats):
    return floor(defense * degats * 0.05)

def bonus(attaque, degats):
    return floor(attaque * degats * 0.1)

# Les Textes
## Demander quelque chose
ASK_HERO_NAME = "Veuillez choisir un nom pour votre héros : "
ASK_PLAYER_ACTION = 'Que voulez-vous faire ? Attaquer, Se soigner, Attendre ? '
ASK_PLAYER_ACTION_WHEN_WRONG = "Cette action n'existe pas. Veuillez choisir parmi Attaquer, Se soigner et Attendre. "
ASK_PLAYER_ATTAQUE = 'Quelle attaque voulez-vous faire ? Attaque faible, moyenne, puissante ? '
ASK_PLAYER_ATTAQUE_WHEN_WRONG = "Cette attaque n'existe pas. Veuillez choisir parmi Attaque faible, moyenne, puissante. "
ASK_PLAYER_CATEGORY = 'Choisissez une catégorie parmi Combattant à pied, Combattant monté, Mage et Support '
ASK_PLAYER_CATEGORY_WHEN_WRONG = "Cette catégorie n'existe pas. Choisissez une catégorie parmi Combattant à pied, Combattant monté, Mage et Support "
ASK_SHOP = "Que voulez-vous acheter ? Arme, Bouclier, Armure, Chaussures, Endurance ou Potion de soin ou d'énergie ? "
ASK_SHOP_WHEN_WRONG = "C'est impossible. Que voulez-vous améliorer ? Arme, Bouclier, Armure, Chaussures ou Endurance, Potion de soin ou d'énergie ? "
ASK_KEEP_BUYING = 'Voulez-vous acheter autre chose ? Oui/Non'

## Annoncer quelque chose
DEAD_MSG = 'Vous avez perdu, dommage. Vous aurez plus de chance la prochaine fois !'
DEAD_MONSTER_MSG = "Bravo, vous avez réussi à vaincre le monstre, vous avez été très fort et très courageux. Vous avez mérité un peu de repos... Mais !?! Que vois-je au loin ? Un autre monstre arrive !! Courage, Héro !"
NOT_ENOUGH_ENERGY = "Il semble que vous n'ayez pas assez d'énergie !"
ATTAQUE_FATALE = 'Cette attaque est fatale !'

def ANNONCE_DEGATS(degats):
    return "Cette attaque inflige "+ str(degats) + ' dégats !'

def ANNONCE_PV_HERO(pv):
    return 'Vous avez encore ' + str(pv) + ' points de vie !'

PV_HERO_HIGH =  ' Pas plus de quelques bobos.'
PV_HERO_GOOD = ' Soyez prudent, vous commencez à saigner du nez.'
PV_HERO_LOW = ' Votre vision se trouble et votre souffle devient court, mais vous pouvez encore combattre.'
PV_HERO_BAD = " Vous êtes à l'article de la mort, priez votre dieu si vous voulez survivre."

def ANNONCE_PV_MONSTER(name, pv):
    return "Ce " + name + ' a encore ' + str(pv) + " points de vie !"

PV_MONSTER_HIGH = " Il n'a pas encore compris que vous lui tapiez dessus."
PV_MONSTER_GOOD = ' Il commence à sentir les coups, mais pas assez pour avoir peur.'
PV_MONSTER_LOW =  " Là il commence à réaliser en quoi l'homme est supérieur et pourquoi il a pu imposer les grattes-ciel à Mère Nature."
PV_MONSTER_BAD = " La SPA veut connaître votre localisation, dépêchez-vous de l'achever." 

def ANNONCE_ENERGY(energy):
    return 'Vous avez encore ' + str(energy) + " points d'énergie !"

ENERGY_HIGH = " Vous pourriez faire ça toute la semaine."
ENERGY_GOOD = " Ça commence à tirer dans les bras mais le plus important c'est le mental."
ENERGY_LOW = " Vous vous mettez à regretter d'avoir séché l'EPS plus jeune, mais c'est trop tard pour revenir en arrière."
ENERGY_BAD = " Votre coup de poing à la capacité offensive d'une douche un peu trop tiède, il vous est recommandé de vous reposer très vite."

SCORE = "Votre score est de "

def ANNONCE_MONEY(money):
    return 'Il vous reste ' + str(money) + " pièce d'or."

# Chemin pour accéder aux images
CHEMIN = 'CodingWeeks2/owtf/images/'

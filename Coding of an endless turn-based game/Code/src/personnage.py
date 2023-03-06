############
# Python 3.8
#
# Coding Weeks
# Semaine 2 : Jeu de Combat
# personnage.py
#
# Equipe 23 :
# Chardin Hugues
# Courty Lola
# Martin Gabriel
# Rouby Morgane
# Sebban Soufiane
#
# Creation Date : Nov. 13th 2020
# Last Modif : Nov. 19th 2020
############

import random
import os
import sys
dossier_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dossier_parent)

from parametres import *
from math import floor
class Personnage:
    """ Classe Personnage

    Dans le jeu, les Héros (joués par les joueurs) et les Monstres (affrontés par les joueurs) sont des personnages.
    Chaque personnage possède un nombre de points de vie maximum et actuel (pv_max et pv), des stats d'attaque, de défense et d'initiative
    A la création, le personnage possède autant de pv que de pv_max """


    def __init__(self, pv_max, attaque, defense, initiative):

        if type(pv_max) != int:
            raise TypeError("Les pv_max doivent être un entier")
        elif pv_max <= 0:
            raise ValueError("Les pv_max doivent être strictement supérieurs à 0")
        
        if type(attaque) != int:
            raise TypeError("Le score d'attaque doit être un entier")
        elif attaque < 0:
            raise ValueError("Le score d'attaque doit être positif ou nul")

        if type(defense) != int:
            raise TypeError("Le score de défense doit être un entier")
        elif defense < 0:
            raise ValueError("Le score de défense doit être positif ou nul")

        if type(initiative) != int:
            raise TypeError("Le score d'initiative doit être un entier")
        elif initiative < 0:
            raise ValueError("Le score d'initiative doit être positif ou nul")

        self._pv_max = pv_max
        self._pv = pv_max
        self._attaque = attaque
        self._defense = defense
        self._initiative = initiative

    @property
    def pv_max(self):
        """ La valeur des pv max est initialisée à la création du personnage. Elle n'est par la suite plus modifiable que par la montée de niveau du personnage. """
        return self._pv_max
    
    @property
    def pv(self):
        """ La valeur des pv actuels, entier compris entre 0 et pv_max """
        return self._pv
    
    @pv.setter
    def pv(self, value):
        """ La valeur des pv actuels, entier compris entre 0 et pv_max """

        if type(value) != int:
            raise TypeError("Les pv doivent être un entier")
        elif value < 0 or value > self.pv_max:
            raise ValueError("Les pv doivent être compris entre 0 et {}".format(self.pv_max))

        self._pv = value
    
    @property
    def attaque(self):
        """ La valeur de la stat d'attaque est initialisée à la création du personnage. Elle n'est par la suite plus modifiable que par la montée de niveau du personnage. """
        return self._attaque

    @property
    def defense(self):
        """ La valeur de la stat de défense est initialisée à la création du personnage. Elle n'est par la suite plus modifiable que par la montée de niveau du personnage. """
        return self._defense
    
    @property
    def initiative(self):
        """ La valeur de la stat d'initiative est initialisée à la création du personnage. Elle n'est par la suite plus modifiable que par la montée de niveau du personnage. """
        return self._initiative
    
    def small_attack(self):
        degats = random.randint(DEGATS_ATTAQUE_FAIBLE[0], DEGATS_ATTAQUE_FAIBLE[1])
        return degats
    
    def medium_attack(self):
        degats = random.randint(DEGATS_ATTAQUE_MOYENNE[0], DEGATS_ATTAQUE_MOYENNE[1])
        return degats

    def big_attack(self):
        degats = random.randint(DEGATS_ATTAQUE_PUISSANTE[0], DEGATS_ATTAQUE_PUISSANTE[1])
        return degats

    def attack(self, opponent, action):
        '''Fonction qui caractérise le fait pour un personnage d'en attaquer un autre'''
        if action == 'Attaque faible':
            degats = self.small_attack()
            if type(self) == Hero :  # L'énergie n'est définie que pour les héros
                self.energy -= COUT_ATTAQUE_FAIBLE
            total = degats + bonus(self.attaque, degats)

        elif action == ATTAQUES[1]:
            degats = self.medium_attack()
            if type(self) == Hero :
                self.energy -= COUT_ATTAQUE_MOYENNE
            total = degats + bonus(self.attaque, degats)
        elif action == ATTAQUES[2]:
            degats = self.big_attack()
            if type(self) == Hero :
                self.energy -= COUT_ATTAQUE_PUISSANTE
            total = degats + bonus(self.attaque, degats)
        
        total -= malus(opponent.defense, total)

        text = [ANNONCE_DEGATS(total)]

        if total >= opponent.pv:
            opponent.pv = 0
            text.append(ATTAQUE_FATALE)
        
        else:
            opponent.pv -= total
            text.append("")
        
        return text  

    def is_dead(self):
        """ lorsque les pv tombent à zéro, le personnage est mort """
        if self.pv == 0:
            return True
        return False        


class Hero(Personnage):
    """ Classe Heros
    
    Chaque héros est un personnage contrôlé par le joueur. Il possède en particulier une catégorie
    (parmi Combattant à pied, Combattant monté, Mage, Support) et une sous_catégorie dépendant de son arme.
    A la création du héros, aucune arme n'est équipée, la sous_catégorie est "Combattant mains nues"
    Il possède également un inventaire auquel le joueur peut accéder au cours du combat.
    A la création du héros l'inventaire est vide
    A la création du héros l'énergie est maximale """

    def __init__(self, name=None, category=CATEGORY_INIT, pv_max=None, attaque=None, defense=None, initiative=None, energy_max=None, money=None):
        
        if type(category) != str:
            raise TypeError("La catégorie doit être chaine de caractère")
        elif category not in CATEGORIES:
            raise ValueError("La catégorie n'existe pas. Il faut choisir parmi " + str(CATEGORIES))
        if name != None and type(name) != str:
            raise TypeError('Le nom doit être une chaine de caractère')

        self._category = category
        self._name = name

        if energy_max != None:
            if type(energy_max) != int:
                raise TypeError("L'énergie maximale doit être un entier")
            elif energy_max <= 0:
                raise ValueError("L'énergie maximale doit être strictement positive")
            self._energy_max = energy_max
            self._energy = energy_max
        else:
            self._energy_max = CATEGORIES[category]['energy max']
            self._energy = CATEGORIES[category]['energy max']        
        
        if money != None:
            self._money = money
        else:
            self._money = CATEGORIES[category]['money']

        if pv_max == None:
            pv_max = CATEGORIES[category]['pv max']
        if attaque == None:
            attaque = CATEGORIES[category]['attaque']
        if defense == None:
            defense = CATEGORIES[category]['defense']
        if initiative == None:
            initiative = CATEGORIES[category]['initiative']

        Personnage.__init__(self, pv_max, attaque, defense, initiative)

    @property
    def name(self):
        return self._name

    @property
    def money(self):
        """ L'argent du héros lui permet d'acheter de nouveaux items ou d'amélliorer ceux qu'il possède """
        return self._money

    @money.setter
    def money(self, value):
        if type(value) != int :
            raise TypeError("int")
        self._money = value

    @property
    def energy_max(self):
        return(self._energy_max)
    
    @property
    def energy(self):
        return(self._energy)
    
    @energy.setter
    def energy(self, value):
        if type(value)!=int:
            raise TypeError("int")
        elif value < 0 or value > self.energy_max :
            raise ValueError("L'énergie doit être comprise entre 0 et energy_max.")
        self._energy = value
    

          
    def healing(self):
        """Action de se soigner : rajoute 20% des PV max"""
        pv_now = self.pv
        diff = self.pv_max - pv_now
        if diff >= int(0.2*self.pv_max) :
            self.pv = pv_now + int(0.2*self.pv_max)
        else : # On ne peut pas dépasser la valeur max
            self.pv = pv_now + diff

    def waiting(self):
        """Action d'attendre : rajoute 20 points d'énergie"""
        energy_now = self.energy
        diff = self.energy_max - energy_now
        if diff >= 20 :
            self.energy = energy_now + 20
        else : # On ne peut pas dépasser la valeur max
            self.energy  = energy_now + diff
    
    def has_enough_energy(self, attaque):
        '''Renvoie True si le héros a assez d'énergie pour faire l'attaque et False sinon.'''
        if attaque == 'Attaque faible':
            if self.energy < 10:
                    return False
            else:
                return True
        elif attaque == 'Attaque moyenne':
            if self.energy < 30:
                return False
            else:
                return True
        elif attaque == 'Attaque forte':
            if self.energy < 50:
                return False
            else:
                return True

    def make_action(self, cible, action, sous_action = None):
        if action == 'Attendre':
            self.waiting()
        elif action == 'Se soigner':
            self.healing()
        elif action == 'Attaquer':
            if self.has_enough_energy(sous_action):
                Personnage.attack(self, cible, sous_action)
            else:
                print("Il semble que vous n'ayez pas assez d'énergie !")



class Monster(Personnage):
    """ Classe Monstre
    
    Chaque monstre est un personnage contrôlé par l'ordinateur, qui affronte le joueur.
    Il possède un loot, que le joueur gagnera en vainquant le monstre. """

    def __init__(self, name=MONSTER_INIT, level = 0):
        
        if type(name) != str:
            raise TypeError('Le nom est une str')
        elif name not in MONSTERS:
            raise ValueError("Le nom n'existe pas. Il faut choisir parmi " + str(MONSTERS))

        pv_max = MONSTERS[name]['pv max'] + level * 2
        attaque = MONSTERS[name]['attaque'] + floor(level / 5)
        defense = MONSTERS[name]['defense'] + floor(level /5)
        initiative = MONSTERS[name]['initiative'] + floor(level /10)
        loot = MONSTERS[name]['loot'] + level

        if type(loot) != int:
            raise TypeError("Le loot est un entier")

        Personnage.__init__(self, pv_max, attaque, defense, initiative)
        self._name = name
        self._loot = loot
        self.level = level

    @property
    def name(self):
        """ Le nom du monstre est défini à l'initialisation. Il ne peut plus être modifié par la suite """
        return self._name

    @property
    def loot(self):
        """ Le loot est ce que possède le monstre et que le joueur peut récupérer en le tuant """
        return self._loot
    
    def monster_attack(self, opponent):
        """renvoie le type d'attaque du monstre pondéré par certaines probabilités"""
        a = random.randint(1,10)
        if 1 <= a <= 6 :
            text = Personnage.attack(self, opponent, ATTAQUES[0])
        elif 7 <= a <= 9 :
            text = Personnage.attack(self, opponent, ATTAQUES[1])
        elif a == 10 :
            text = Personnage.attack(self, opponent, ATTAQUES[2])
        return text 

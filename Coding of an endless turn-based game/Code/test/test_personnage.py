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
# Creation Date : Nov. 13th 2020
# Last Modif : Nov. 19th 2020
############

import os
import sys
dossier_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dossier_parent)

import pytest
from parametres import *
from src.personnage import *
from math import floor


def test_creation_personnage():
    Personnage(20, 5, 5, 1)
    with pytest.raises(TypeError):
        Personnage('Bonjour', 5, 5, 1)
    with pytest.raises(ValueError):
        Personnage(-20, 5, 5, 1)
    with pytest.raises(ValueError):
        Personnage(0, 5, 5, 1)
    with pytest.raises(TypeError):
        Personnage(20, 'Bonjour', 5, 1)
    with pytest.raises(ValueError):
        Personnage(20,-5, 5, 1)
    with pytest.raises(TypeError):
        Personnage(20, 5, 'Bonjour', 1)
    with pytest.raises(ValueError):
        Personnage(20, 5, -5, 1)
    with pytest.raises(TypeError):
        Personnage(20, 5, 5, 'Bonjour')
    with pytest.raises(ValueError):
        Personnage(20, 5, 5, -1)

def test_récupération_attributs_personnage():
    perso = Personnage(20, 5, 5, 1)
    assert perso.pv_max == 20
    assert perso.pv == 20
    assert perso.attaque == 5
    assert perso.defense == 5
    assert perso.initiative == 1

def test_modification_attributs_personnage():
    perso = Personnage(20, 5, 5, 1)
    with pytest.raises(TypeError):
        perso.pv = 'Bonjour'
    with pytest.raises(ValueError):
        perso.pv = -1
    with pytest.raises(ValueError):
        perso.pv = 200
    with pytest.raises(AttributeError):
        perso.pv_max = 200
    with pytest.raises(AttributeError):
        perso.attaque = 50
    with pytest.raises(AttributeError):
        perso.defense = 50
    with pytest.raises(AttributeError):
        perso.initiative = 10

def test_small_attack():
    hero = Hero()
    L = [k for k in range(5,16)]
    assert hero.small_attack() in L 

def test_medium_attack():
    hero = Hero()
    L = [k for k in range(20,31)]
    assert hero.medium_attack() in L

def test_big_attack():
    perso = Personnage(20, 5, 5, 1)
    L=[k for k in range(35, 56)]
    assert perso.big_attack() in L

def test_attack():
    perso1 = Personnage(150, 5, 5, 1)
    perso2= Personnage(100,7,5,1)
    L1=[]
    pv_now2 = perso2.pv
    for k in  range(pv_now2 - 22, pv_now2 - 6):
        L1.append(k)
    perso1.attack(perso2,'Attaque faible')
    assert perso2.pv in L1
    pv_now1 = perso1.pv
    L2 = []
    for k in range(pv_now1 - 25, pv_now1):
        L2.append(k)
    perso2.attack(perso1,'Attaque faible')
    assert perso1.pv in L2
    perso3 = Personnage(150, 5, 5, 1)
    perso4= Personnage(100,7,5,1)
    pv_now4 = perso4.pv
    L3=[]
    for k in  range(pv_now4 -34, pv_now4 - 22):
        L3.append(k)
    perso3.attack(perso4,'Attaque moyenne')
    assert perso4.pv in L3
    pv_now3 = perso3.pv
    L4 = []
    for k in range(pv_now3 - 39, pv_now3 - 25):
        L4.append(k)
    perso4.attack(perso3,'Attaque moyenne')
    assert perso3.pv in L4
    perso5 = Personnage(150, 5, 5, 1)
    perso6= Personnage(100,7,5,1)
    pv_now6 = perso6.pv
    L5 = []
    for k in range(pv_now6 - 69, pv_now6 - 33):
        L5.append(k)
    perso5.attack(perso6,'Attaque puissante')
    assert perso6.pv in L5
    pv_now5 = perso5.pv
    L6 = []
    for k in range(pv_now5 - 70, pv_now5 - 44):
        L6.append(k)
    perso6.attack(perso5,'Attaque puissante')
    assert perso5.pv in L6

def test_is_dead():
    perso = Personnage(20, 5, 5, 1)
    assert not perso.is_dead()
    perso.pv = 0
    assert perso.is_dead()

def test_creation_hero():
    Hero('Maxime', 'Combattant à pied', 20, 5, 5, 1, 100, 0)
    with pytest.raises(TypeError):
        Hero(name=4)
    with pytest.raises(TypeError):
        Hero('Maxime', 'Combattant à pied', 'Bonjour', 5, 5, 1, 100, 0)
    with pytest.raises(ValueError):
        Hero('Maxime', 'Combattant à pied', -20, 5, 5, 1, 100, 0)
    with pytest.raises(ValueError):
        Hero('Maxime', 'Combattant à pied', 0, 5, 5, 1, 100, 0)
    with pytest.raises(TypeError):
        Hero('Maxime', 'Combattant à pied', 20, 'Bonjour', 5, 1, 100, 0)
    with pytest.raises(ValueError):
        Hero('Maxime', 'Combattant à pied', 20,-5, 5, 1, 100, 0)
    with pytest.raises(TypeError):
        Hero('Maxime', 'Combattant à pied', 20, 5, 'Bonjour', 1, 100, 0)
    with pytest.raises(ValueError):
        Hero('Maxime', 'Combattant à pied', 20, 5, -5, 1, 100, 0)
    with pytest.raises(TypeError):
        Hero('Maxime', 'Combattant à pied', 20, 5, 5, 'Bonjour', 100, 0)
    with pytest.raises(ValueError):
        Hero('Maxime', 'Combattant à pied', 20, 5, 5, -1, 100, 0)
    with pytest.raises(TypeError):
        Hero('Maxime', 1, 20, 5, 5, 1, 100, 0)
    with pytest.raises(ValueError):
        Hero('Maxime', 'Bonjour', 20, 5, 5, 1, 100, 0)
    with pytest.raises(TypeError):
        Hero('Maxime', 'Combattant à pied', 20, 5, 5, 1, 'Bonjour', 0)
    with pytest.raises(ValueError):
        Hero('Maxime', 'Combattant à pied', 20, 5, 5, 1, -100, 0)
    with pytest.raises(TypeError):
        Hero('Maxime', 'Combattant à pied', 20, 5, 5, 1, 100, 'Bonjour')
    with pytest.raises(ValueError):
        Hero('Maxime', 'Combattant à pied', 20, 5, 5, 1, 100, -10)

def test_recuperation_attributs_hero():
    hero = Hero('Maxime', 'Combattant à pied', 20, 5, 5, 1, 100, 0)
    assert hero.name == 'Maxime'
    assert hero.pv_max == 20
    assert hero.pv == 20
    assert hero.attaque == 5
    assert hero.defense == 5
    assert hero.initiative == 1
    assert hero.category == 'Combattant à pied'
    assert hero.energy_max == 100
    assert hero.energy == 100
    assert hero.money == 0

def test_modification_attributs_hero():
    hero = Hero('Maxime', 'Combattant à pied', 20, 5, 5, 1, 100, 0)
    with pytest.raises(AttributeError):
        hero.name = 'Myriam'
    with pytest.raises(TypeError):
        hero.pv = 'Bonjour'
    with pytest.raises(ValueError):
        hero.pv = -1
    with pytest.raises(ValueError):
        hero.pv = 200
    with pytest.raises(AttributeError):
        hero.pv_max = 200
    with pytest.raises(AttributeError):
        hero.attaque = 50
    with pytest.raises(AttributeError):
        hero.defense = 50
    with pytest.raises(AttributeError):
        hero.initiative = 10
    with pytest.raises(AttributeError):
        hero.category = 'Combattant monté'
    with pytest.raises(AttributeError):
        hero.energy_max = 50
    hero.energy = 20
    assert hero.energy == 20
    with pytest.raises(TypeError):
        hero.energy = 'Bonjour'
    with pytest.raises(ValueError):
        hero.energy = -5
    with pytest.raises(ValueError):
        hero.energy = 200
    with pytest.raises(TypeError):
        hero.money = 'Bonjour'
    with pytest.raises(ValueError):
        hero.money = -100
    hero.money = 50
    assert hero.money == 50

def test_healing():
    hero1 = Hero()
    hero1.healing()
    assert hero1._pv == 100
    hero2 = Hero()
    hero2.pv = 40
    hero2.healing()
    assert hero2._pv == 60
    hero3 = Hero()
    hero3.pv = 90
    hero3.healing()
    assert hero3._pv == 100

def test_waiting():
    hero1 = Hero()
    hero1.waiting()
    assert hero1.energy == 100
    hero2 = Hero()
    hero2.energy = 40
    hero2.waiting()
    assert hero2.energy == 60
    hero3 = Hero()
    hero3.energy = 90
    hero3.waiting()
    assert hero3.energy == 100

def test_make_action():
    monster = Monster('Pabo')
    hero = Hero()

    e = random.randint(0, 100)
    hero.energy = e
    hero.make_action(monster, 'Attendre')
    assert hero.energy == e + 20 or hero.energy == 100

    v = random.randint(0, 100)
    hero.pv = v
    hero.make_action(monster, 'Se soigner')
    assert hero.pv == v + 20 or hero.pv == 100

    for k in ['Attaque faible', 'Attaque moyenne', 'Attaque puissante']:
        hero.pv = hero.pv_max
        hero.energy = hero.energy_max
        monster.pv = monster.pv_max
        hero.make_action(monster, 'Attaquer', k)
        assert monster.pv < monster.pv_max

def test_creation_monster():
    Monster('Pabo')
    with pytest.raises(TypeError):
        Monster(3)
    with pytest.raises(ValueError):
        Monster('Bonjour')

def test_récupération_attributs_monster():
    monster = Monster('Pabo')
    assert monster.pv_max == 20
    assert monster.pv == 20
    assert monster.attaque == 1
    assert monster.defense == 3
    assert monster.initiative == 2
    assert monster.loot == 50
    assert monster.name == 'Pabo'

def test_modification_attributs_monster():
    monster = Monster('Pabo')
    with pytest.raises(AttributeError):
        monster.name = 'Gromauch'
    with pytest.raises(TypeError):
        monster.pv = 'Bonjour'
    with pytest.raises(ValueError):
        monster.pv = -1
    with pytest.raises(ValueError):
        monster.pv = 200
    with pytest.raises(AttributeError):
        monster.pv_max = 200
    with pytest.raises(AttributeError):
        monster.attaque = 50
    with pytest.raises(AttributeError):
        monster.defense = 50
    with pytest.raises(AttributeError):
        monster.initiative = 10
    with pytest.raises(AttributeError):
        monster.loot = ['Fourrure']

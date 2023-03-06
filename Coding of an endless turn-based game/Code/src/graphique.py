############
# Python 3.8
#
# Coding Weeks
# Semaine 2 : Jeu de Combat
# graphique.py
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
import time
import threading

dossier_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dossier_parent)

from playsound import playsound
from random import randint
from math import floor
from parametres import *
from tkinter import *
from PIL import ImageTk, Image
from src.personnage import *
from src.play import *


hero_name =''
small_attack = False
medium_attack = False
big_attack = False
healing = False
waiting = False
button_small_attack = None
button_medium_attack = None
button_big_attack = None
button_attacking = None
button_waiting = None
button_healing = None
button_previous = None
attack = False
in_store = False


### AIDE ET STATISTIQUES


def window_stats(hero):
    window = Toplevel()
    window.title('Statistiques du héros')
    window.iconbitmap(CHEMIN + "logo.ico")
    pv_max = Label(window, text = 'PV max : ' + str(hero.pv_max))
    energie_max = Label(window, text = 'Energie max : ' + str(hero.energy_max))
    initiative = Label(window, text = 'Initiative : ' + str(hero.initiative))
    attaque = Label(window, text = 'Attaque : ' + str(hero.attaque))
    defense = Label(window, text = 'Défense : ' + str(hero.defense))
    pv_max.pack()
    energie_max.pack()
    initiative.pack()
    attaque.pack()
    defense.pack()
    window.mainloop()

"""
def window_aide():
    '''Cette fonction permet de créer une fenêtre d'aide, qui donne les informations nécessaire au joueur'''
    window = Toplevel()
    window.title('Aide')
    window.iconbitmap(CHEMIN + "logo.ico")
    image_stamina = PhotoImage(file = CHEMIN + 'endurance.gif')
    image_weapon = PhotoImage(file = CHEMIN + 'arme.gif')
    image_armor = PhotoImage(file = CHEMIN + 'armure.gif')
    image_shoes = PhotoImage(file = CHEMIN + 'chaussures.gif')
    image_shield = PhotoImage(file = CHEMIN + 'bouclier.gif')
    image_life_potion = PhotoImage(file = CHEMIN + 'potion_de_soin.gif')
    image_energy_potion = PhotoImage(file = CHEMIN + 'potion_d_energy.gif')
    image_text_stamina = PhotoImage(file = CHEMIN + 'texte_endurance.gif')
    image_text_weapon = PhotoImage(file = CHEMIN + 'texte_arme.gif')
    image_text_armor = PhotoImage(file = CHEMIN + 'texte_armure.gif')
    image_text_shoes = PhotoImage(file = CHEMIN + 'texte_chaussures.gif')
    image_text_shield = PhotoImage(file = CHEMIN + 'texte_bouclier.gif')
    image_text_life_potion = PhotoImage(file = CHEMIN + 'texte_potion_de_soin.gif')
    image_text_energy_potion = PhotoImage(file = CHEMIN + 'texte_potion_d_energy.gif')
    image_healing = PhotoImage(file = CHEMIN + 'se_soigner.gif')
    image_attacking = PhotoImage(file = CHEMIN + 'attaquer.gif')
    image_waiting = PhotoImage(file = CHEMIN + 'attendre.gif')
    image_big_attack = PhotoImage(file = CHEMIN + 'attaque_puissante.gif')
    image_medium_attack = PhotoImage(file = CHEMIN + 'attaque_moyenne.gif')
    image_small_attack = PhotoImage(file = CHEMIN + 'attaque_faible.gif')
    image_next = PhotoImage(file = CHEMIN + 'tour_suivant.gif')
    image_text_healing = PhotoImage(file = CHEMIN + 'texte_se_soigner.gif')
    image_text_attacking = PhotoImage(file = CHEMIN + 'texte_attaquer.gif')
    image_text_waiting = PhotoImage(file = CHEMIN + 'texte_attendre.gif')
    image_text_big_attack = PhotoImage(file = CHEMIN + 'texte_attaque_puissante.gif')
    image_text_medium_attack = PhotoImage(file = CHEMIN + 'texte_attaque_moyenne.gif')
    image_text_small_attack = PhotoImage(file = CHEMIN + 'texte_attaque_faible.gif')
    image_text_next = PhotoImage(file = CHEMIN + 'texte_tour_suivant.gif')
    window.image_stamina = image_stamina
    window.image_weapon = image_weapon
    window.image_armor = image_armor
    window.image_shoes = image_shoes
    window.image_shield = image_shield
    window.image_life_potion = image_life_potion
    window.image_energy_potion = image_energy_potion
    window.image_text_stamina = image_text_stamina
    window.image_text_weapon = image_text_weapon
    window.image_text_armor = image_text_armor
    window.image_text_shoes = image_text_shoes
    window.image_text_shield = image_text_shield
    window.image_text_life_potion = image_text_life_potion
    window.image_text_energy_potion = image_text_energy_potion
    window.image_attacking = image_attacking
    window.image_waiting = image_waiting
    window.image_big_attack = image_big_attack
    window.image_medium_attack = image_medium_attack
    window.image_small_attack = image_small_attack
    window.image_next = image_next
    window.image_text_healing = image_text_healing
    window.image_text_attacking = image_text_attacking
    window.image_text_waiting = image_text_waiting
    window.image_text_big_attack = image_text_big_attack
    window.image_text_medium_attack = image_text_medium_attack
    window.image_text_small_attack = image_text_small_attack
    window.image_text_next = image_text_next
    canvas = Canvas(window, width = 370, height = 680, bg = 'white')
    canvas.create_image(3, 3, anchor = 'nw', image = image_healing, activeimage = image_text_healing)
    canvas.create_image(3, 103, anchor = 'nw', image = image_attacking, activeimage = image_text_attacking)
    canvas.create_image(3, 203, anchor = 'nw', image = image_waiting, activeimage = image_text_waiting)
    canvas.create_image(3, 303, anchor = 'nw', image = image_big_attack, activeimage = image_text_big_attack)
    canvas.create_image(3, 403, anchor = 'nw', image = image_medium_attack, activeimage = image_text_medium_attack)
    canvas.create_image(3, 503, anchor = 'nw', image = image_small_attack, activeimage = image_text_small_attack)
    canvas.create_image(3, 603, anchor = 'nw', image = image_next, activeimage = image_text_next)
    canvas.create_image(200, 3, anchor = 'nw', image = image_armor, activeimage = image_text_armor)
    canvas.create_image(200, 103, anchor = 'nw', image = image_shield, activeimage = image_text_shield)
    canvas.create_image(200, 203, anchor = 'nw', image = image_weapon, activeimage = image_text_weapon)
    canvas.create_image(200, 303, anchor = 'nw', image = image_shoes, activeimage = image_text_shoes)
    canvas.create_image(200, 403, anchor = 'nw', image = image_stamina, activeimage = image_text_stamina)
    canvas.create_image(200, 503, anchor = 'nw', image = image_life_potion, activeimage = image_text_life_potion)
    canvas.create_image(200, 603, anchor = 'nw', image = image_energy_potion, activeimage = image_text_energy_potion)
    canvas.pack()
    window.mainloop()

"""
### LES BOUTONS


def validation(window, canvas, hero, monster, image_hero):
    """Cette fonction est appelée lorsque le joueur appuie sur valider. Elle réalise l'action choisie.""" 
    global button_previous, button_small_attack, button_waiting, button_attacking, button_small_attack, button_medium_attack, button_big_attack 
    global rectangle_monster_pv, rectangle_hero_pv, rectangle_energy, pv_text_monster, pv_text_hero, energy_text
    global small_attack, medium_attack, big_attack, healing, waiting, attack
    if small_attack :
        canvas.delete(image_hero)
        image_my_hero, position_hero = right_image(hero, 'attaque')
        image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
        window.update()
        window.after(400)
        canvas.delete(image_hero)
        image_my_hero, position_hero = right_image(hero, None)
        image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
        messages = hero.attack(monster, "Attaque faible")
        message1 = canvas.create_text(500, 25, anchor = 'n',font = ('Helvetica', -25), text= messages[0])
        message2 = canvas.create_text(500, 50, anchor = 'n',font = ('Helvetica', -25), text= messages[1])
        window.update()
        #On introduit un temps d'arrêt pour laisser au joueur le temps de lire les messages.
        window.after(2500)
        #On met à jour les barres de vie et d'énergie. On supprime les messages.
        update_bars(canvas, hero, monster)
        canvas.delete(message1)
        canvas.delete(message2)
        window.update()
        small_attack = False
    elif medium_attack :
        canvas.delete(image_hero)
        image_my_hero, position_hero = right_image(hero, 'attaque')
        image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
        window.update()
        window.after(400)
        canvas.delete(image_hero)
        image_my_hero, position_hero = right_image(hero, None)
        image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
        messages = hero.attack(monster, "Attaque moyenne")
        message1 = canvas.create_text(500, 25, anchor = 'n',font = ('Helvetica', -25), text = messages[0])
        message2 = canvas.create_text(500, 50, anchor = 'n',font = ('Helvetica', -25), text = messages[1])
        window.update()
        #On introduit un temps d'arrêt pour laisser au joueur le temps de lire les messages.
        window.after(2000)
        #On met à jour les barres de vie et d'énergie. On supprime les messages.
        update_bars(canvas, hero, monster)
        canvas.delete(message1)
        canvas.delete(message2)
        canvas.delete(image_hero)
        window.update()
        medium_attack = False
    elif big_attack :
        canvas.delete(image_hero)
        image_my_hero, position_hero = right_image(hero, 'attaque')
        image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
        window.update()
        canvas.delete(image_hero)
        image_my_hero, position_hero = right_image(hero, None)
        image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
        messages = hero.attack(monster, "Attaque puissante")
        message1 = canvas.create_text(500, 25, anchor = 'n',font = ('Helvetica', -25), text = messages[0])
        message2 = canvas.create_text(500, 50, anchor = 'n',font = ('Helvetica', -25), text = messages[1])
        canvas.delete(message1)
        canvas.delete(message2)
        canvas.delete(image_hero)
        update_bars(canvas, hero, monster)
        window.update()
        big_attack = False
    elif waiting :
        #Action d'attendre
        hero.waiting()
        message = canvas.create_text(500, 25, anchor = 'n',font = ('Helvetica', -25), text = "Vous récupérez 20 d'énergie !")
        window.update()
        window.after(1500)
        #On met à jour les barres de vie et d'énergie, et on efface le message.
        canvas.delete(message)

        update_bars(canvas, hero, monster)
        waiting = False
    elif healing :
        #Action de se soigner.
        hero.healing()
        bonus_pv = floor(0.2*hero.pv_max)
        message = canvas.create_text(500, 25, anchor = 'n',font = ('Helvetica', -25), text = "Vous récupérez "+ str(bonus_pv)+" PV!")
        window.update()
        window.after(1500)
        #On met à jour les barres de vie et d'énergie, et on efface le message.
        canvas.delete(message)
        update_bars(canvas, hero, monster)
        healing = False 
    else :
        message = canvas.create_text(500, 25, anchor = 'n',font = ('Helvetica', -25), text="Vous venez de passez votre tour...")
        window.update()
        window.after(1000)
        canvas.delete(message)
    button_waiting.destroy()
    button_attacking.destroy()
    button_healing.destroy()
    if attack : #Si on a pensé attaquer
        button_small_attack.destroy()
        button_medium_attack.destroy()
        button_big_attack.destroy()
        attack = False
    

def do_button_small_attack(b1, b2, b3, b4, hero, target, canvas, window):
    """Fait l'action correspondante au bouton 'Attaque faible' et détruit ensuite tous les boutons.
    b1, b2, b3, b4 : boutons
    hero et target : personnages 
    canvas : canevas
    window : fenêtre tkinter"""
    global small_attack, button_previous
    small_attack = True
    button_previous = Button(window, text = "Retour")
    button_previous['command'] = lambda b4 = button_previous : display_buttons_action(window, canvas, hero, target, b1, b2, b3, b4)
    button_window4 = canvas.create_window(220,147, anchor = 'nw', window = button_previous)


def do_button_medium_attack(b1, b2, b3, b4, hero, target, canvas, window):
    """Fait l'action correspondante au bouton 'Attaque moyenne' et détruit ensuite tous les boutons.
    b1, b2, b3, b4 : boutons
    hero et target : personnages
    canvas : canevas
    window : fenêtre tkinter """
    global medium_attack, button_previous
    medium_attack = True
    button_previous = Button(window, text = "Retour")
    button_previous['command'] = lambda b4 = button_previous : display_buttons_action(window, canvas, hero, target, b1, b2, b3, b4)
    button_window4 = canvas.create_window(220, 147, anchor = 'nw', window = button_previous)


def do_button_big_attack(b1, b2, b3, b4, hero, target, canvas, window):
    """Fait l'action correspondante au bouton 'Attaque puissante' et détruit ensuite tous les boutons.
    mon_heros et cible : personnages
>>>>>>> 53828823d2bbd6540ac8cb13f2f2ab8a7e335b9e
    canvas : canevas
    window : fenêtre """
    global big_attack, button_previous
    big_attack = True
    button_previous = Button(window, text = "Retour")
    button_previous['command'] = lambda b4 = button_previous : display_buttons_action(window, canvas, hero, target, b1, b2, b3, b4)
    button_window4 = canvas.create_window(220,147, anchor = 'nw', window = button_previous)


def buttons_attack(window, b1, b2, b3, hero, target, canvas):
    """Crée trois boutons pour déterminer l'intensité de l'attaque et détruit tous les précédents boutons.
    b1, b2, b3 : boutons
    hero et target : personnages
    window : fenêtre d'affichage 
    canvas : canevas"""
    global button_small_attack, button_medium_attack, button_big_attack, attack
    b1.destroy()
    b2.destroy()
    b3.destroy()
    attack = True
    #On crée trois boutons, un pour chaque type d'attaque, ainsi qu'un bouton pour revenir en arrière.
    button_small_attack = Button(window, text = "Attaque faible")
    button_medium_attack = Button(window, text = "Attaque moyenne")
    button_big_attack = Button(window, text = "Attaque puissante")
    button_previous = Button(window, text = "Retour")

    button_small_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack, b4 = button_previous : do_button_small_attack(b1, b2, b3, b4, hero, target, canvas, window)
    button_medium_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack, b4 = button_previous : do_button_medium_attack(b1, b2, b3, b4, hero, target, canvas, window)
    button_big_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack, b4 = button_previous : do_button_big_attack( b1, b2, b3, b4, hero, target, canvas, window)
    button_previous['command'] = lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack, b4 = button_previous : display_buttons_action(window, canvas, hero, target, b1, b2, b3, b4)
    #On les affiche.
    button_window1 = canvas.create_window(7,120, anchor = 'w', window = button_small_attack)
    button_window2 = canvas.create_window(200,120, anchor = 'e', window = button_medium_attack)
    button_window3 = canvas.create_window(7,160, anchor = 'w', window = button_big_attack)
    button_window4 = canvas.create_window(266,160, anchor = 'e', window = button_previous)
    #On désactive des boutons d'attaque si le héros n'a pas assez d'énergie.
    if hero.energy < 50:
        button_big_attack.config(state = DISABLED)
    if hero.energy < 30:
        button_medium_attack.config(state = DISABLED)

def do_button_healing(b1, b2,b3, hero, monster, canvas, window):
    """Fait l'action correspondante au bouton "Se soigner" et détruit tous les boutons.
    b1, b2, b3 : boutons
    hero, monster : personnages """
    global healing, button_previous, button_healing
    healing = True
    button_previous = Button(window, text = "Retour")
    button_previous['command'] = lambda b4 = button_previous : display_buttons_action(window, canvas, hero, monster, b1, b2, b3, b4)
    button_window4 = canvas.create_window(220,147, anchor = 'nw', window = button_previous)


def do_button_waiting(b1, b2,b3, hero, monster, canvas, window):
    """Fait l'action correspondante au bouton "Attendre" et détruit tous les boutons.
    b1, b2, b3 : boutons
    hero, monster : personnages """
    global waiting, button_previous, button_waiting
    waiting = True
    button_previous = Button(window, text = "Retour")
    button_previous['command'] = lambda b4 = button_previous : display_buttons_action(window, canvas, hero, monster, b1, b2, b3, b4)
    button_window4 = canvas.create_window(220,147, anchor = 'nw', window = button_previous)


def display_buttons_action(window, canvas, hero, target, b1 = None, b2 = None, b3 = None, b4 = None):
    """ Crée trois boutons 'Attendre', 'Se soigner' et 'Attaquer
    canvas : canevas
    hero et target : personnages
    window : fenêtre d'affichage """
    global rectangle_hero_pv, rectangle_monster_pv, rectangle_energy, pv_text_monster, pv_text_hero, energy_text
    global button_healing, button_waiting, button_attacking
    if b1 != None:
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
    #On crée les trois boutons.
    button_waiting = Button(window, text = "Attendre")
    button_healing = Button(window, text = "Se soigner")
    button_attacking = Button(window, text = "Attaquer")
    button_healing['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : do_button_healing(b1, b2, b3, hero, target, canvas, window)
    button_waiting['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : do_button_waiting(b1, b2, b3, hero, target, canvas, window)
    button_attacking['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : buttons_attack(window, b1, b2, b3, hero, target, canvas)
    #On les affiche.
    button_window1 = canvas.create_window(45, 120, anchor = 'center', window = button_healing)
    button_window2 = canvas.create_window(155, 120, anchor = 'center', window = button_waiting)
    button_window3 = canvas.create_window(100, 160, anchor = 'center', window = button_attacking)


### RENVOYER LES IMAGES


def right_image(character, action):
    """Renvoie l'image, ainsi que sa position optimale (liste [abscisse, ordonnée])"""
    if type(character) == Hero:
        if character.pv == 0:
            return(PhotoImage(file = CHEMIN + 'perso1-8.gif'), [220, 600, 'center'])
        else:
            if action == None :
                return(PhotoImage(file = CHEMIN + 'perso1-0.gif'), [220, 640, 's'])
            else :
                return(PhotoImage(file = CHEMIN + 'perso1-1.gif'), [250, 640, 's'])
    else :
        if character.name == 'Pabo':
            if action == None :
                return(PhotoImage(file = CHEMIN + 'monstre1.gif'), [730, 640, 's'])
            elif action == "reflechit":
                return(PhotoImage(file = CHEMIN + 'monstre1-1.gif'), [730, 640, 's'])
            elif action == "attaque" :
                return(PhotoImage(file = CHEMIN + 'monstre1-2.gif'), [730, 640, 's'])
            else :
                return(PhotoImage(file = CHEMIN + 'monstre1-3.gif'), [800, 600, 'center'])
        elif character.name == 'Gromauch' :
            if action == None :
                return(PhotoImage(file = CHEMIN + 'monstre3.gif'), [730, 640, 's'])
            elif action == "reflechit":
                return(PhotoImage(file = CHEMIN + 'monstre3-1.gif'), [730, 640, 's'])
            elif action == "attaque" :
                return(PhotoImage(file = CHEMIN  +'monstre3-2.gif'), [730, 640, 's'])
            else :
                return(PhotoImage(file = CHEMIN + 'monstre3-3.gif'), [730, 640, 's'])
        else :
            if action == None :
                return(PhotoImage(file = CHEMIN + 'monstre4.gif'), [730, 640, 's'])
            elif action == "reflechit":
                return(PhotoImage(file = CHEMIN + 'monstre4-1.gif'), [720, 630, 's'])
            elif action == "attaque" :
                return(PhotoImage(file = CHEMIN + 'monstre4-2.gif'), [720, 660, 's'])
            else :
                return(PhotoImage(file = CHEMIN + 'monstre4-3.gif'), [730, 590, 'center'])



def update_bars(canvas, hero, monster):
    """Cette fonction met à jour les barres de vie et d'énergie.
    canvas : canevas
    hero, monster : personnages"""
    global rectangle_monster_pv, rectangle_hero_pv, rectangle_energy, pv_text_monster, pv_text_hero, energy_text
    canvas.delete(pv_text_monster)
    canvas.delete(pv_text_hero)
    canvas.delete(energy_text)
    rectangle_monster_pv, pv_text_monster = monster_pv_bar(canvas, monster.pv_max, monster.pv)
    rectangle_hero_pv, pv_text_hero = hero_pv_bar(canvas, hero.pv_max, hero.pv)
    rectangle_energy, energy_text = energy_bar(canvas, hero.energy_max, hero.energy)

def hero_pv_bar(canvas, pv_max, pv):
    """Affiche une barre représentant la proportion de PV du héros par rapport à leur nombre maximal
    canvas : canevas
    Pv_max, Pv : int """
    canvas.create_rectangle(3, 32, 203, 62, fill='grey')
    #Calcul la longueur du rectangle interne
    length = (pv*200)/pv_max 
    rectangle = canvas.create_rectangle(3, 32, 3 + length, 62, fill='green')
    canvas.create_text(10, 47, text='PV', anchor='w')
    pv_text_hero = canvas.create_text(210, 47, anchor='w', text = str(pv) + '/' + str(pv_max))
    return(rectangle, pv_text_hero)


def monster_pv_bar(canvas, pv_max, pv):
    """Affiche une barre représentant la proportion de PV du monstre par rapport à leur nombre maximal
    canvas : canevas
    Pv_max, Pv : int """
    canvas.create_rectangle(797, 32, 997, 62, fill='grey')
    #Calcul la longueur du rectangle interne
    length = (pv*200)/pv_max 
    rectangle = canvas.create_rectangle(997 - length, 32, 997, 62, fill='green')
    canvas.create_text(990, 47, text='PV', anchor='e')
    pv_text_monster = canvas.create_text(790, 47, anchor='e', text = str(pv) + '/' + str(pv_max))
    return(rectangle, pv_text_monster)

def energy_bar(canvas, energy_max, energy):
    canvas.create_rectangle(3, 65, 203, 95, fill='grey')
    #Calcul la longueur du rectangle interne
    length = (energy*200)/energy_max 
    rectangle = canvas.create_rectangle(3, 65, 3+ length, 95, fill='blue')
    canvas.create_text(10, 80, text='Energie', anchor='w')
    energy_text = canvas.create_text(210, 80, anchor='w', text = str(energy) + '/' + str(energy_max))
    return(rectangle,energy_text)


### FENETRE INITIALE  


def get_name(window, var):
    """Cette fonction récupère le nom du héros et détruit la fenêtre correspondante."""
    global hero_name
    hero_name = var.get()
    window.destroy()

def init_data():
    score = 0
    rand = randint(1,3)
    if rand == 1:
        name = NAMES_MONSTERS[0]
    elif rand == 2:
        name = NAMES_MONSTERS[1]
    elif rand == 3:
        name = NAMES_MONSTERS[2]
    monster = Monster(name=name)
    level = 0
    return score, monster, level

def init_affichage():
    """Crée une fenêtre pour initialiser le nom du héros. Crée un monstre et iniatialise le score"""
    score, monster, level = init_data()
    window = Tk()
    window.title('Initialisation')
    window.iconbitmap(CHEMIN+"logo.ico")
    var = StringVar()
    label = Label(window, text = "Veuillez choisir un nom pour votre héros : ")
    label.pack()
    name = Entry(window, text = var)
    name.pack()
    button = Button(window, text = "Valider", command = lambda : get_name(window, var))
    button.pack()
    window.mainloop()
    return score, hero_name, monster, level



### COMMENTAIRES


def commentary(window, canvas, hero, monster):
    """Cette fonction affiche des commentaires sur les états du héros et du monstre."""
    message_pv_hero = print_pv(hero)
    print_message_pv_hero = canvas.create_text(500, 30, anchor = 'n',font = ('Helvetica', -23), width = 400, justify ='center', text= message_pv_hero)
    window.update()
    #Temps d'arrêt pour lire.
    window.after(2500)
    #On efface le commentaire.
    canvas.delete(print_message_pv_hero)
    message_energy = print_energy(hero)
    #Et on recommence !
    print_message_energy = canvas.create_text(500, 30, anchor = 'n',font = ('Helvetica', -23), width = 400, justify = 'center', text= message_energy)
    window.update()
    window.after(2500)
    canvas.delete(print_message_energy)
    message_pv_monster = print_pv(monster)
    print_message_pv_monster = canvas.create_text(500, 30, anchor = 'n',font = ('Helvetica', -23), width = 400, justify = 'center', text= message_pv_monster)
    window.update()
    window.after(2500)
    canvas.delete(print_message_pv_monster)
    window.update()


# TOUR DU MONSTRE


def tour_du_monstre(window, canvas, hero, monster, image_monster, score, message_score, monster_name, message_argent, level, hero_begin = False):
    """Cette fonction réalise le tour du monstre : faire l'attaque en mettant à jour l'affichage, et les barres de vie et d'énergie."""
    global rectangle_monster_pv, rectangle_hero_pv, rectangle_energy, pv_text_monster, pv_text_hero, energy_text
    if hero_begin :
        #On affiche le héros
        image_my_hero, position_hero = right_image(hero, None)
        window.image_my_hero = image_my_hero
        image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor =  position_hero[2], image = image_my_hero)
    if monster.is_dead():
        tour_de_jeu(window, canvas, hero, monster, score, message_score, monster_name, message_argent, level)
    else :
        window.after(1000)
        #On efface la précédente image
        canvas.delete(image_monster)
        #On affiche le monstre en train de réfléchir
        image_my_monster, position_monster = right_image(monster, 'reflechit')
        image_monster = canvas.create_image(position_monster[0],position_monster[1], anchor = position_monster[2], image = image_my_monster)
        window.update()
        #Pour ne pas que les changements se fassent 'instantanément', on rajoute des temps d'arrêt
        window.after(1000)
        canvas.delete(image_monster)
        #On affiche le monstre en train d'attaquer
        image_my_monster, position_monster = right_image(monster, 'attaque')
        image_monster = canvas.create_image(position_monster[0],position_monster[1], anchor = position_monster[2], image = image_my_monster)
        window.update()
        #Action d'attaquer : on récupère les messages correspondants
        messages = monster.monster_attack(hero)
        window.after(400)
        canvas.delete(image_monster)
        #On affiche ces messages
        message1 = canvas.create_text(500, 25, anchor = 'n',font = ('Helvetica', -25), text= messages[0])
        message2 = canvas.create_text(500, 50, anchor = 'n',font = ('Helvetica', -25), text= messages[1])
        image_my_monster, position_monster = right_image(monster, None)
        image_monster = canvas.create_image(position_monster[0],position_monster[1], anchor = position_monster[2], image = image_my_monster)
        window.update()
        window.after(2000)
        #On nettoie l'affichage (suppresion des messages, mise à jour des barres)
        canvas.delete(message1)
        canvas.delete(message2)
        canvas.delete(image_monster)
        canvas.delete(rectangle_monster_pv)
        canvas.delete(rectangle_energy)
        canvas.delete(rectangle_hero_pv)
        canvas.delete(pv_text_hero)
        canvas.delete(pv_text_monster)
        canvas.delete(energy_text)
        update_bars(canvas, hero, monster)
        window.update()
    if hero_begin :
            canvas.delete(image_hero)
            window.update()
            if hero.is_dead():
                #On affiche le héros mort
                image_my_hero, position_hero = right_image(hero, None)
                window.image_my_hero = image_my_hero
                image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
                canvas.delete(image_hero)
                image_my_hero, position_hero = right_image(hero, "mort")
                window.image_my_hero = image_my_hero
                image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
                canvas.create_text(500, 30, anchor = 'n',font = ('Helvetica', -23), width = 400, justify = 'center', text=DEAD_MSG)
                window.mainloop()
            else :
                tour_de_jeu(window, canvas, hero, monster, score, message_score, monster_name, message_argent, level)



### TOUR DE JEU


def tour_de_jeu(window, canvas, hero, monster, score, message_score, message_money, monster_name, level):
    """Cette fonction réalise un tour de jeu.
    window : fenêtre tkinter
    canvas : canevas, hero, monster : personnages
    message_score : zone de texte du canevas affichant le score
    monster_name : zone de texte du canevas affichant le nom du monstre"""
    global rectangle_monster_pv, rectangle_hero_pv, rectangle_energy, pv_text_monster, pv_text_hero, energy_text
    global in_store
    #On affiche le héros.
    image_my_hero, position_hero = right_image(hero, None)
    window.image_my_hero = image_my_hero
    image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
    image_my_monster, position_monster = right_image(monster, None)
    window.image_my_monster = image_my_monster
    image_monster = canvas.create_image(position_monster[0], position_monster[1], anchor = position_monster[2], image = image_my_monster)
    canvas.delete(image_monster)
    window.update()
    
    #Si notre monstre est mort :
    if monster.is_dead():
        if not in_store:
            in_store = True
            image_my_monster, position_monster = right_image(monster, 'mort')
            image_monster = canvas.create_image(position_monster[0],position_monster[1], anchor = position_monster[2], image = image_my_monster)
            window.update()
            message_dead_monster = canvas.create_text(500, 25, anchor = 'n',font = ('Helvetica', -25), width = 400, text = DEAD_MONSTER_MSG)
            window.update()
            window.after(3000)
            #On efface les précédentes caractéristiques du monstre ainsi que le score.
            canvas.delete(message_dead_monster)
            canvas.delete(image_monster)
            canvas.delete(message_score)
            canvas.delete(message_money)
            canvas.delete(monster_name)
            window.update()
            #On met à jour le score et on crée un nouveau monstre.
            score, monster, level = endless_monster(hero, monster, score, level)
            message_score = canvas.create_text(495, 5, anchor = 'ne',font = ('Helvetica', -15), text='score : ' + str(score))
            message_money = canvas.create_text(505, 5, anchor = 'nw',font = ('Helvetica', -15), text='argent : ' + str(hero.money))
            window.update()
            store(window, canvas, hero, monster, score, message_score, message_money, monster_name, level)
    
    # Dès que l'on a quitté la boutique, le combat reprend 
    if not in_store:
        #On affiche le nouveau monstre.
        image_my_monster, position_monster = right_image(monster, None)
        image_monster = canvas.create_image(position_monster[0], position_monster[1], anchor = position_monster[2], image = image_my_monster)
        update_bars(canvas, hero, monster)
        canvas.delete(monster_name)
        monster_name = canvas.create_text(997, 0, anchor = 'ne',font = ('Helvetica', -30), text = monster.name + ' LV : ' + str(monster.level))
        window.update()
        #On affiche des commentaires sur les états du héros et du monstre.
        commentary(window, canvas, hero, monster)
        
        #Premier cas : le monstre a une initiative plus grande. Il commence donc à jouer.  
        if hero.initiative < monster.initiative :           
            #Le monstre joue.
            tour_du_monstre(window, canvas, hero, monster, image_monster, score, message_score, monster_name, message_money, level)
            #On fixe l'image du monstre.
            image_my_monster, position_monster = right_image(monster, None)
            window.image_my_monster = image_my_monster
            image_monster = canvas.create_image(position_monster[0],position_monster[1], anchor = position_monster[2], image = image_my_monster)
            window.update()
            if not hero.is_dead():
                #On affiche un bouton pour relancer un tour.
                next_round = Button(window, text = 'Valider', command = lambda : [validation(window, canvas, hero, monster, image_hero), tour_de_jeu(window, canvas, hero, monster, score, message_score, monster_name, message_money, level)])
                button_next_round = canvas.create_window(220, 120, anchor = 'w', window = next_round)
            else :
                #Sinon, on affiche le héros mort
                image_my_hero, position_hero = right_image(hero, None)
                window.image_my_hero = image_my_hero
                image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
                canvas.delete(image_hero)
                image_my_hero, position_hero = right_image(hero, "mort")
                window.image_my_hero = image_my_hero
                image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
                canvas.create_text(500, 30, anchor = 'n',font = ('Helvetica', -23), width = 400, justify = 'center', text = DEAD_MSG)
                return(window)
            display_buttons_action(window, canvas, hero, monster)
        
        #Deuxième cas : le héros à une initiative plus grande.
        elif hero.initiative > monster.initiative :
            hero_begin = True
            display_buttons_action(window, canvas, hero, monster)
            #On réaffiche le monstre
            image_my_monster, position_monster = right_image(monster, None)
            window.image_my_monster = image_my_monster
            image_monster = canvas.create_image(position_monster[0], position_monster[1], anchor = position_monster[2], image = image_my_monster)
            #Dès que le joueur a fini de jouer, on lance le tour du monstre
            next_round = Button(window, text = 'Valider', command = lambda : [validation(window, canvas, hero, monster, image_hero), tour_du_monstre(window, canvas, hero, monster, image_monster, score, message_score, monster_name, message_money, level, hero_begin)])
            button_next_round = canvas.create_window(220, 120, anchor = 'w', window = next_round)
        
        #Troisième cas : si les deux personnages ont la même initiative, on tire à pile ou face.
        else :
            rd = randint(1,2)
            if rd == 1 :
                #Le monstre joue.
                tour_du_monstre(window, canvas, hero, monster, image_monster, score, message_score, monster_name, message_money, level)
                #On fixe l'image du monstre.
                image_my_monster, position_monster = right_image(monster, None)
                window.image_my_monster = image_my_monster
                image_monster = canvas.create_image(position_monster[0], position_monster[1], anchor = position_monster[2], image = image_my_monster)
                window.update()
                if not hero.is_dead():
                    #On affiche un bouton pour relancer un tour.
                    next_round = Button(window, text = 'Valider', command = lambda : [validation(window, canvas, hero, monster, image_hero), tour_de_jeu(window, canvas, hero, monster, score, message_score, monster_name, message_money, level)])
                    button_next_round = canvas.create_window(220, 120, anchor = 'w', window = next_round)
                else :
                    #Sinon, on affiche le héros mort
                    image_my_hero, position_hero = right_image(hero, None)
                    window.image_my_hero = image_my_hero
                    image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
                    canvas.delete(image_hero)
                    image_my_hero, position_hero = right_image(hero, "mort")
                    window.image_my_hero = image_my_hero
                    image_hero = canvas.create_image(position_hero[0], position_hero[1], anchor = position_hero[2], image = image_my_hero)
                    return(window)
                display_buttons_action(window, canvas, hero, monster)
            else :
                hero_begin = True
                display_buttons_action(window, canvas, hero, monster)
                #On réaffiche le monstre
                image_my_monster, position_monster = right_image(monster, None)
                window.image_my_monster = image_my_monster
                image_monster = canvas.create_image(position_monster[0],position_monster[1], anchor = position_monster[2], image = image_my_monster)
                #Dès que le joueur a fini de jouer, on lance le tour du monstre
                next_round = Button(window, text = 'Valider', command = lambda : [validation(window, canvas, hero, monster, image_hero), tour_du_monstre(window, canvas, hero, monster, image_monster, score, message_score, monster_name, message_money, hero_begin)])
                button_next_round = canvas.create_window(220, 120, anchor = 'w', window = next_round)

    
### LA BOUTIQUE


def store(window, canvas, hero, monster, score, message_score, message_money, monster_name, level):
    '''Affiche les différentes propositions de la boutique.'''
    #On déclare les commandes des boutons
    button_armor = Button(window, text = "Armure, " + str(SHOP['Armure'][0]) + " pièces d'or.") #Bouton pour amméliorer l'armure
    button_shield = Button(window, text = "Bouclier, " + str(SHOP['Bouclier'][0]) + " pièces d'or.") #Bouton pour amméliorer le bouclier
    button_weapon = Button(window, text = "Arme, " + str(SHOP['Arme'][0]) + " Pièces d'or.") #Bouton pour amméliorer l'arme
    button_shoes = Button(window, text = "Chaussures, " + str(SHOP['Chaussures'][0]) + " Pièces d'or.") #Bouton pour amméliorer les chaussures
    button_stamina = Button(window, text = "Endurance, " + str(SHOP['Endurance'][0]) + " Pièces d'or.") #Bouton pour amméliorer l'andurance
    button_life_potion = Button(window, text = "Potion de soin, " + str(SHOP['Potion de soin'][0]) + " Pièces d'or.") #Bouton pour acheter une potion de vie
    button_energy_potion = Button(window, text = "Potion d'énergie, " + str(SHOP["Potion d'énergie"][0]) + " Pièces d'or.") #Bouton pour prendre une potion d'énergie
    button_leave = Button(window, text = "Quitter la boutique") #Bouton pour quitter la boutique
    #On ajoute les commandes des boutons
    button_armor['command']= lambda b1=button_armor, b2=button_shield, b3=button_weapon, b4=button_shoes, b5=button_stamina, b6=button_life_potion, b7=button_energy_potion, b8=button_leave : amelioration(hero, 'Armure', message_money, window, canvas, monster, score, message_score, monster_name, level, b1, b2, b3, b4, b5, b6, b7, b8)
    button_shield['command']= lambda b1=button_armor, b2=button_shield, b3=button_weapon, b4=button_shoes, b5=button_stamina, b6=button_life_potion, b7=button_energy_potion, b8=button_leave : amelioration(hero, 'Bouclier', message_money, window, canvas, monster, score, message_score, monster_name, level, b1, b2, b3, b4, b5, b6, b7, b8)
    button_weapon['command']= lambda b1=button_armor, b2=button_shield, b3=button_weapon, b4=button_shoes, b5=button_stamina, b6=button_life_potion, b7=button_energy_potion, b8=button_leave : amelioration(hero, 'Arme', message_money, window, canvas, monster, score, message_score, monster_name, level, b1, b2, b3, b4, b5, b6, b7, b8)
    button_shoes['command']= lambda b1=button_armor, b2=button_shield, b3=button_weapon, b4=button_shoes, b5=button_stamina, b6=button_life_potion, b7=button_energy_potion, b8=button_leave : amelioration(hero, 'Chaussures', message_money, window, canvas, monster, score, message_score, monster_name, level, b1, b2, b3, b4, b5, b6, b7, b8)
    button_stamina['command']= lambda b1=button_armor, b2=button_shield, b3=button_weapon, b4=button_shoes, b5=button_stamina, b6=button_life_potion, b7=button_energy_potion, b8=button_leave : amelioration(hero, 'Endurance', message_money, window, canvas, monster, score, message_score, monster_name, level, b1, b2, b3, b4, b5, b6, b7, b8)
    button_life_potion['command']= lambda b1=button_armor, b2=button_shield, b3=button_weapon, b4=button_shoes, b5=button_stamina, b6=button_life_potion, b7=button_energy_potion, b8=button_leave : amelioration(hero, 'Potion de soin', message_money, window, canvas, monster, score, message_score, monster_name, level, b1, b2, b3, b4, b5, b6, b7, b8)
    button_energy_potion['command']= lambda b1=button_armor, b2=button_shield, b3=button_weapon, b4=button_shoes, b5=button_stamina, b6=button_life_potion, b7=button_energy_potion, b8=button_leave : amelioration(hero, "Potion d'énergie", message_money, window, canvas, monster, score, message_score, monster_name, level, b1, b2, b3, b4, b5, b6, b7, b8)
    button_leave['command']= lambda b1=button_armor, b2=button_shield, b3=button_weapon, b4=button_shoes, b5=button_stamina, b6=button_life_potion, b7=button_energy_potion, b8=button_leave : leave_store(window, canvas, hero, monster, score, message_score, message_money, monster_name, level, b1, b2, b3, b4, b5, b6, b7, b8)
    #On affiche les boutons
    button_window1 = canvas.create_window(450,67, anchor = 'nw', window = button_armor)
    button_window2 = canvas.create_window(450,97, anchor = 'nw', window = button_shield)
    button_window3 = canvas.create_window(450,157, anchor = 'nw', window = button_weapon)
    button_window4 = canvas.create_window(450,127, anchor = 'nw', window = button_shoes)
    button_window5 = canvas.create_window(450,187, anchor = 'nw', window = button_stamina)
    button_window6 = canvas.create_window(450,217, anchor = 'nw', window = button_life_potion)
    button_window7 = canvas.create_window(450,247, anchor = 'nw', window = button_energy_potion)
    button_window8 = canvas.create_window(450,37, anchor = 'nw', window = button_leave)
    #Il faut que les amméliorations pour lesquelles le joueur n'a pas assez d'argent soient indisponibles
    if hero.money < SHOP['Arme'][0]:
        button_weapon.config(state = DISABLED)
    if hero.money < SHOP['Bouclier'][0]:
        button_shield.config(state = DISABLED)
    if hero.money < SHOP['Armure'][0]:
        button_armor.config(state = DISABLED)
    if hero.money < SHOP['Chaussures'][0]:
        button_shoes.config(state = DISABLED)
    if hero.money < SHOP['Endurance'][0]:
        button_stamina.config(state = DISABLED)
    if hero.money < SHOP['Potion de soin'][0]:
        button_life_potion.config(state = DISABLED)
    if hero.money < SHOP["Potion d'énergie"][0]:
        button_energy_potion.config(state = DISABLED)


def leave_store(window, canvas, hero, monster, score, message_score, message_money, monster_name, level, b1, b2, b3, b4, b5, b6, b7, b8):
    '''Fonction qui permet de quitter la boutique et de retourner au combat'''
    global in_store
    in_store = False
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()
    b8.destroy()
    tour_de_jeu(window, canvas, hero, monster, score, message_score, message_money, monster_name, level)


def amelioration(hero, equipement, message_money, window, canvas, monster, score, message_score, monster_name, level, b1, b2, b3, b4, b5, b6, b7, b8):
    """ Fonction qui connecte la boutique aux amméliorations du héros. """
    #On commence par détruire les boutons existants pour pouvoir en recréer d'autres au prochain appel de la boutique
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()
    b8.destroy()
    hero._money -= SHOP[equipement][0] #On retire l'argent nécessaire à l'ammélioration
    canvas.delete(message_money) #On supprime le texte avec l'argent pour le mettre à jour et le recréer
    message_money = canvas.create_text(505, 5, anchor = 'nw',font = ('Helvetica', -15), text='Argent : ' + str(hero.money))
    window.update()
    if equipement == 'Arme':
        hero._attaque += SHOP[equipement][1] #La statistique du héros est modifiée
        #On poste un message de confirmation au joueur
        message_weapon = canvas.create_text(300, 100, width = 400, justify = CENTER, anchor = 'nw',font = ('Helvetica', -25), text="Votre arme sort fraîchement de la forge. Vous avez hâte de poutrer des hérétiques avec.")
        window.update()
        window.after(3000)
        canvas.delete(message_weapon)
        window.update()
    elif equipement == "Potion d'énergie":
        hero.energy = hero.energy_max
        update_bars(canvas, hero, monster)
        message_weapon = canvas.create_text(300, 100, width = 400, justify = CENTER, anchor = 'nw',font = ('Helvetica', -25), text="Votre énergie est de nouveau pleine. Vous vous sentez capable de courir un marathon sur les petits doigts tout en faisant la toupie.")
        window.update()
        window.after(3000)
        canvas.delete(message_weapon)
        window.update()
    elif equipement == 'Bouclier':
        hero._defense += SHOP[equipement][1]
        message_arme = canvas.create_text(300, 100, width = 400, justify = CENTER, anchor = 'nw',font = ('Helvetica', -25), text="Votre bouclier a l'air bien plus solide qu'avant. Vous pourriez arrêter un train lancé à vive allure si seulement les trains existaient dans ce monde.")
        window.update()
        window.after(3000)
        canvas.delete(message_arme)
        window.update()
    elif equipement == 'Armure':
        hero._pv_max += SHOP[equipement][1]
        update_bars(canvas, hero, monster)
        message_weapon = canvas.create_text(300, 100, width = 400, justify = CENTER, anchor = 'nw',font = ('Helvetica', -25), text="Votre armure est flambant neuve. Tailladez quelques monstres pour votre réputation et vous êtes assuré de séduire n'importe quelle princesse au prochain bal impérial.")
        window.update()
        window.after(3000)
        canvas.delete(message_weapon)
        window.update()
    elif equipement == 'Chaussures':
        hero._initiative += SHOP[equipement][1]
        message_weapon = canvas.create_text(300, 100, width = 400, justify = CENTER, anchor = 'nw',font = ('Helvetica', -25), text="Le tanneur a fini de réparer vos souliers. Mais vous auriez sans doute mieux fait d'économiser pour acheter un cheval.")
        window.update()
        window.after(3000)
        canvas.delete(message_weapon)
        window.update()
    elif equipement == 'Potion de soin':
        hero.pv = hero.pv_max
        update_bars(canvas, hero, monster)
        message_weapon = canvas.create_text(300, 100, width = 400, justify = CENTER, anchor = 'nw',font = ('Helvetica', -25), text="Votre santé est à nouveau à son maximum. Quoi de mieux pour célébrer votre regain de vie que d'aller prendre celles de créatures impures ?")
        window.update()
        window.after(3000)
        canvas.delete(message_weapon)
        window.update()
    else: # equipement == 'Endurance'
        hero._energy_max += SHOP[equipement][1]
        update_bars(canvas, hero, monster)
        message_weapon = canvas.create_text(300, 100, width = 400, justify = CENTER, anchor = 'nw',font = ('Helvetica', -25), text="Votre endurance a augmenté. Le plus important reste le mental mais un corps d'athlète qui peut faire le tour du monde en sprintant sans faire de pause est toujours utile.")
        window.update()
        window.after(3000)
        canvas.delete(message_weapon)
        window.update()
    button_stats = Button(canvas, text = 'Stats héros', command = lambda hero = hero : window_stats(hero))
    canvas.create_window(200, 660, window = button_stats)
    store(window, canvas, hero, monster, score, message_score, message_money, monster_name, level)



### MUSIQUE


#Musique : Death Mountain, composée par Ryo Nagamatsu, issu du jeu-vidéo "The Legend of Zelda: A Link Between Worlds"
#playsound(CHEMIN + "wmusic2.wav", False)


### LANCER LE JEU


#Lancer la partie en initialisant le nom du heros, le monstre et le score.
score, hero_name, monster, level = init_affichage()
#On crée le héros.
hero = Hero(name = hero_name)
#On crée la fenêtre.
window = Tk()
window.title('One week to fight !')
#On affiche le fond.
window.iconbitmap(CHEMIN +'logo.ico')
background_image = PhotoImage(file = CHEMIN + 'fond.gif')
canvas = Canvas(window, width=1000, height=679)
canvas.create_image(500, 339, image = background_image)
canvas.pack()
button_help = Button(canvas, text = 'Aide', command = window_aide)
canvas.create_window(100, 200, anchor = 'center', window = button_help)
button_stats = Button(canvas, text = 'Stats héros', command = lambda hero = hero : window_stats(hero))
canvas.create_window(200, 660, window = button_stats)
#On crée les barres de vie et d'énergie.
rectangle_hero_pv, pv_text_hero = hero_pv_bar(canvas, hero.pv_max, hero.pv)
rectangle_monster_pv, pv_text_monster = monster_pv_bar(canvas, monster.pv_max, monster.pv)
rectangle_energy, energy_text = energy_bar(canvas, hero.energy_max, hero.energy)
#On crée des zones de texte pour afficher le score et les noms du héros et du monstre. 
message_score = canvas.create_text(495, 5, anchor = 'ne',font = ('Helvetica', -15), text='score : ' + str(score))
message_money = canvas.create_text(505, 5, anchor = 'nw',font = ('Helvetica', -15), text='argent : ' + str(hero.money))
canvas.create_text(3, 0, anchor = 'nw',font = ('Helvetica', -30), text = hero.name)
monster_name = canvas.create_text(997, 0, anchor = 'ne',font = ('Helvetica', -30), text = monster.name + ' LV : ' + str(monster.level))
tour_de_jeu(window, canvas, hero, monster, score, message_score, message_money, monster_name, level)
window.mainloop()

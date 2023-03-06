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
# Last Modif : Nov. 17th 2020
############

from random import randint


import os
import sys
dossier_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dossier_parent)

from parametres import *
from tkinter import *
from PIL import ImageTk, Image
from src.personnage import *
'''
global image_hero
global image_

def do_button_small_attack(window, b1, b2, b3, mon_heros, cible):
    """Fait l'action correspondante au bouton 'Attaque faible', détruit ensuite tous les boutons et change l'image du héros.
    b1, b2, b3 : boutons
    mon_heros et cible : personnages """
    global image_heros
    canvas.delete(image_hero)
    image_mon_heros, position_mon_heros = right_image(mon_heros, 'Attaque')
    global image_heros
    image_heros = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    mon_heros.attack(cible, "Attaque faible")
    b1.destroy()
    b2.destroy()
    b3.destroy()
    window.after(1000)
    window.update()


def do_button_medium_attack(window, b1, b2, b3, mon_heros, cible):
    """Fait l'action correspondante au bouton 'Attaque moyenne', détruit ensuite tous les boutons et change l'image du héros.
    b1, b2, b3 : boutons
    mon_heros et cible : personnages """
    global image_heros
    canvas.delete(image_hero)
    image_mon_heros, position_mon_heros = right_image(mon_heros, 'Attaque')
    global image_heros
    image_heros = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    mon_heros.attack(cible, "Attaque moyenne")
    b1.destroy()
    b2.destroy()
    b3.destroy()
    window.after(1000)
    window.update()


def do_button_big_attack(window, b1, b2, b3, mon_heros, cible):
    """Fait l'action correspondante au bouton 'Attaque puissante', détruit ensuite tous les boutons et change l'image du héros.
    b1, b2, b3 : boutons
    mon_heros et cible : personnages """
    global image_heros
    canvas.delete(image_hero)
    image_mon_heros, position_mon_heros = right_image(mon_heros, 'Attaque')
    global image_heros
    image_heros = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    mon_heros.attack(cible, "Attaque puissante")
    b1.destroy()
    b2.destroy()
    b3.destroy()
    window.after(1000)
    window.update()


def buttons_attack(window, canvas, b1, b2, b3, mon_heros, cible):
    """Crée trois boutons pour déterminer l'intensité de l'attaque et détruit tous les précédents boutons.
    b1, b2, b3 : boutons
    mon_heros et cible : personnages
    window : fenêtre d'affichage """
    b1.destroy()
    b2.destroy()
    b3.destroy()
    button_small_attack = Button(window, text = "Attaque faible")
    button_medium_attack = Button(window, text = "Attaque moyenne")
    button_big_attack = Button(window, text = "Attaque puissante")
    button_small_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack : do_button_small_attack(b1, b2, b3, mon_heros, cible)
    button_medium_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack : do_button_medium_attack(b1, b2, b3, mon_heros, cible)
    button_big_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack : do_button_big_attack( b1, b2, b3, mon_heros, cible)
    button_window_1 = canvas.create_window(50,120, anchor = 'center', window = button_small_attack)
    button_window_2 = canvas.create_window(150,120, anchor = 'center', window = button_medium_attack)
    button_window_3 = canvas.create_window(100,160, anchor = 'center', window = button_big_attack)
    window.update()


def do_button_healing(window, b1, b2,b3, mon_heros):
    """Fait l'action correspondante au bouton "Se soigner", détruit tous les boutons et change l'image du héros.
    b1, b2, b3 : boutons
    mon_heros : héros """
    global image_heros
    canvas.delete(image_hero)
    image_mon_heros, position_mon_heros = right_image(mon_heros, 'Se soigne')
    global image_heros
    image_heros = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    mon_heros.healing()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    window.after(1000)
    window.update()


def do_button_waiting(window, b1, b2,b3, mon_heros):
    """Fait l'action correspondante au bouton "Attendre" et détruit tous les boutons.
    b1, b2, b3 : boutons
    mon_heros : héros """
    global image_heros
    canvas.delete(image_heros)
    global image_heros
    image_mon_heros, position_mon_heros = right_image(mon_heros, 'Rien')
    image_heros = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    mon_heros.waiting()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    window.after(1000)
    window.update()


def display_buttons_action(window, canvas, mon_heros, cible):
    """ Crée trois boutons 'Attendre', 'Se soigner' et 'Attaquer et change l'image du personnage
    canvas : canevas 
    mon_heros et cible : personnages
    window : fenêtre d'affichage """
    global image_heros
    canvas.delete(image_heros)
    image_mon_heros, position_mon_heros = right_image(mon_heros, 'Attend')
    global image_heros
    image_heros = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    button_waiting = Button(window, text = "Attendre")
    button_healing = Button(window, text = "Se soigner")
    button_attacking = Button(window, text = "Attaquer")
    button_healing['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : do_button_healing(b1, b2, b3, mon_heros)
    button_waiting['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : do_button_waiting(b1, b2, b3, mon_heros)
    button_attacking['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : buttons_attack(window, canvas, b1, b2, b3, mon_heros, cible)
    button_window1 = canvas.create_window(50,120, anchor = 'center', window = button_healing)
    button_window2 = canvas.create_window(150,120, anchor = 'center', window = button_waiting)
    button_window3 = canvas.create_window(100,160, anchor = 'center', window = button_attacking)
    window.update()


def right_image(mon_perso, action):
    """Renvoie l'image, ainsi que sa position optimale (liste [abscisse, ordonnée])"""
    if type(mon_perso) == Heros: 
        if mon_perso.pv == 0:
            return(PhotoImage(file='owtf/images/perso1-8.gif'), [250, 570])
        if action == 'Rien':
            return(PhotoImage(file='owtf/images/perso1-0.gif'), [150, 450])
        if action == 'Attaque':
            return(PhotoImage(file='owtf/images/perso1-2.gif'), [500, 400])
        #if action == 'Attend':
            #return(PhotoImage(file='owtf/images/perso1-attendre.gif'), [?, ?])
        #if action == 'Se soigne':
            #return(PhotoImage(file='owtf/images/perso1-se_soigne.gif'), [?, ?])
    else :
        if mon_perso.name == 'Pabo':
            if mon_perso.pv == 0:
                return(PhotoImage(file='owtf/images/monstre1.gif'), [500, 300])
            if action == 'Rien':
                return(PhotoImage(file= 'owtf/images/monstre1.gif'), [730, 450])
            if action == 'Attend':
                return(PhotoImage(file='owtf/images/monstre1.gif'), [600, 200])
            if action == 'Attaque':
                return(PhotoImage(file='owtf/images/monstre1.gif'), [300, 500])
        elif mon_perso.name == 'Gromauch' :
            if mon_perso.pv == 0:
                return(PhotoImage(file='owtf/images/monstre3.gif'), [100, 500])
            if action == 'Rien':
                return(PhotoImage(file= 'owtf/images/monstre3.gif'), [730, 450])
            if action == 'Attend':
                return(PhotoImage(file='owtf/images/monstre3.gif'), [240, 345])
            if action == 'Attaque':
                return(PhotoImage(file='owtf/images/monstre3.gif'), [456, 543])
        else :
            if mon_perso.pv == 0:
                return(PhotoImage(file='owtf/images/monstre4.gif'), [265, 265])
            if action == 'Rien':
                return(PhotoImage(file= 'owtf/images/monstre4.gif'), [730, 450])
            if action == 'Attend':
                return(PhotoImage(file='owtf/images/monstre4.gif'), [876, 564])
            if action == 'Attaque':
                return(PhotoImage(file='owtf/images/monstre4.gif'), [763, 274])


def hero_pv_bar(canvas, PV_max, PV):
    """Affiche une barre représentant la proportion de PV du héros par rapport à leur nombre maximal
    canvas : canevas
    Pv_max, Pv : int """
    canvas.create_rectangle(3, 30, 203, 60, fill='red')
    #Calcul la longueur du rectangle interne
    longueur = (PV*200)/PV_max 
    pv_bar_hero = canvas.create_rectangle(3, 30, 3+longueur, 60, fill='green')
    canvas.create_text(10, 45, text='PV', anchor='w')
    pv_text_hero = canvas.create_text(210, 45, anchor='w', text=str(PV)+'/'+str(PV_max))


def monster_pv_bar(canvas, PV_max, PV):
    """Affiche une barre représentant la proportion de PV du monstre par rapport à leur nombre maximal
    canvas : canevas
    Pv_max, Pv : int """
    canvas.create_rectangle(797, 30, 997, 60, fill='red')
    #Calcul la longueur du rectangle interne
    longueur = (PV*200)/PV_max 
    pv_bar_monster = canvas.create_rectangle(997 - longueur, 30, 997, 60, fill='green')
    canvas.create_text(990, 45, text='PV', anchor='e')
    pv_text_monster = canvas.create_text(790, 45, anchor='e', text=str(PV)+'/'+str(PV_max))


def energy_bar(canvas, energy_max, energy):
    """Affiche une barre représentant la proportion d'énergie par rapport à sa valeur maximale
    canvas : canevas
    energy_max, energy : int """
    canvas.create_rectangle(3, 64, 203, 94, fill='red')
    #Calcul la longueur du rectangle interne, représentant la proportion de PV rpar rapport à leur nombre maximal
    longueur = (energy*200)/energy_max 
    energy_bar = canvas.create_rectangle(3, 64, 3+longueur, 94, fill='blue')
    canvas.create_text(10, 77, text='Energie',anchor='w', fill='white')
    energy_text = canvas.create_text(210, 77, anchor='w', text=str(energy)+'/'+str(energy_max))


def update_hero_pv_bar(canvas, PV_max, PV):
    """Met à jour la barre représentant les PV du héros
    canvas : canevas
    PV_max, PV : int """
    #suppression des données obsolètes
    canvas.delete(pv_bar_hero)
    canvas.delete(pv_text_hero)
    #création des données mises à jour
    longueur = (PV*200)/PV_max 
    pv_bar_hero = canvas.create_rectangle(3, 30, 3+longueur, 60, fill='green')
    pv_text_hero = canvas.create_text(210, 45, anchor='w', text=str(PV)+'/'+str(PV_max))
    window.update()


def update_monster_pv_bar(canvas, PV_max, PV):
    """Met à jour la barre représentant les PV du monstre
    canvas : canevas
    PV_max, PV : int """
    global pv_bar_monster, pv_text_monster
    #suppression des données obsolètes
    canvas.delete(pv_bar_monster)
    canvas.delete(pv_text_monster)
    #création des données mises à jour
    global pv_bar_monster, pv_text_monster
    longueur = (PV*200)/PV_max 
    pv_bar_monster = canvas.create_rectangle(997 - longueur, 30, 997, 60, fill='green')
    pv_text_monster = canvas.create_text(790, 45, anchor='e', text=str(PV)+'/'+str(PV_max))
    window.update()


def update_energy_bar(canvas, energy_max, energy):
    """Met à jour la barre représentant l'énergie' du héros
    canvas : canevas
    energy_max, energy : int """
    global energy_bar_hero, energy_text_hero
    #suppression des données obsolètes
    canvas.delete(energy_bar)
    canvas.delete(energy_text)
    #création des données mises à jour
    longueur = (energy*200)/energy_max 
    energy_bar = canvas.create_rectangle(3, 64, 3+longueur, 94, fill='blue')
    energy_text = canvas.create_text(210, 77, anchor='w', text=str(energy)+'/'+str(energy_max))
    window.update()


def tour_du_heros_graphique(window, canvas, mon_heros, mon_monstre):
    """Effectue les modifications graphiques lorsque c'est le tour du héros
    window : fenêtre d'affichage
    canevas : canevas
    mon_heros, mon_monstre : personnages """
    display_buttons_action(window, canvas, mon_heros, mon_monstre)
    update_hero_pv_bar(canvas, mon_heros.pv_max, mon_heros.pv)
    update_monster_pv_bar(canvas, mon_monstre.pv_max, mon_monstre.pv)
    update_energy_bar(canvas, mon_heros.energy_max, mon_heros.energy)
    if monster.pv == 0:
        changer_monstre(window, canvas, mon_monstre)
    window.update()
    

def tour_du_monstre_graphique(window, canvas, mon_heros, mon_monstre):
    """Effectue les modifications graphiques lorsque c'est le tour du monstre
    window : fenêtre d'affichage
    canevas : canevas
    mon_heros, mon_monstre : personnages """
    canvas.delete(image_monstre)
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, 'Attend')
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    window.after(1000)
    mon_monstre.monster_attack(mon_heros)
    canvas.delete(image_monstre)
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, 'Attaque')
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    update_hero_pv_bar(canvas, mon_heros.pv_max, mon_heros.pv)
    window.after(1000)
    canvas.delete(image_monstre)
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, 'Rien')
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    window.update()


def changer_monstre(window, canvas, mon_monstre):
    """Change de monstre lorsqu'un monstre décède
    window : fenêtre d'affichage
    canevas : canevas
    mon_monstre : personnages """
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, 'Rien')
    canvas.delete(image_monstre)
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    window.after(1000)
    canvas.delete(image_monstre)
    score, mon_monstre = endless_monster(mon_heros, mon_monstre, score)
    canvas.delete(affichage_score)
    affichage_score = canvas.create_text(500, 5, anchor = 'n',font = ('Helvetica', -15), text='score : ' + str(score))
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, 'Rien')
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    update_monster_pv_bar(canvas, mon_monstre.pv_max, mon_monstre.pv)
    window.update()


def init():
    score = 0
    rand = randint(1,3)
    if rand == 1:
        name = 'Pabo'
        monster = Monster(name = 'Pabo')
    elif rand == 2:
        name = 'Gromauch'
        monster = Monster(name = 'Gromauch')
    elif rand == 3:
        name = 'Touvisqeut'
        monster = Monster(name = 'Touvisqeut')
    return score, monster


def init_affichage():
    """Crée une fenêtre pour initialiser le nom du héros. Crée un monstre et iniatialise le score"""
    score, monster = init()
    window = Tk()
    window.title('Initialisation')
    var = StringVar()
    label = Label(window, text="Veuillez choisir un nom pour votre héros : ")
    label.pack()
    name = Entry(window, text=var)
    name.pack()
    button = Button(window, text="Valider", command = lambda : get_name(window, var))
    button.pack()
    window.mainloop()
    return score, name, monster


def get_name(window, var):
    """Cette fonction récupère le nom du héros et détruit la fenêtre correspondante."""
    global hero_name
    hero_name = var.get()
    window.destroy()


def game_play_affichage():
    score, heros_name, monster = init_affichage()
    heros = Heros(name = str(heros_name))
    window = Tk()
    window.title('One week to fight !')
    background_image = PhotoImage(file ='owtf/images/fond.gif')
    canvas = Canvas(window, width=1000, height=679)
    canvas.create_image(500, 339, image = background_image)
    canvas.pack()
    image_mon_heros, position_mon_heros = right_image(heros, 'Rien')
    image_mon_monstre, position_mon_monstre = right_image(monster, 'Rien')
    image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    hero_pv_bar(canvas, heros.pv_max, heros.pv)
    monster_pv_bar(canvas, monster.pv_max, monster.pv)
    energy_bar(canvas, heros.energie_max, heros.energie)
    score = 0
    affichage_score = canvas.create_text(500, 5, anchor = 'n',font = ('Helvetica', -15), text='score : ' + str(score))
    canvas.create_text(140, 210, anchor = 'center',font = ('Helvetica', -30), text = 'Eric') #personnages.py pas update
    canvas.create_text(796, 70, anchor = 'nw',font = ('Helvetica', -30), text = monster.name) #personnages.py pas update (anglais normalement)
    # initialisation de la variable texte (ex: le mostre vous inflige 20 dégats)
    middle_text = canvas.create_text(430, 200, anchor = 'center',font = ('Helvetica', -20), text = ' ')
    window.update()
    while not heros.is_dead():
        # on regarde l'initiative pour définir qui agit en premier
        if heros.initiative < monster.initiative :
            tour_du_monstre_graphique(window, canvas, heros, monster)
            tour_du_heros_graphique(window, canvas, heros, monster)
        elif heros.initiative > monster.initiative :
            tour_du_heros_graphique(window, canvas, heros, monster)
            tour_du_monstre_graphique(window, canvas, heros, monster)
        else :
            #si les deux personnages ont la même initiative, on tire à pile ou face
            rd = randint(1,2)
            if rd == 1:
                monster.monster_attack(heros)
                #on sort de la boucle lorsque le héro décède
                score, monster = tour_du_heros(monster, heros, score)
                fin_du_tour(monster, heros)
            else:
                tour_du_heros_graphique(window, canvas, heros, monster)
                tour_du_monstre_graphique(window, canvas, heros, monster)  
'''
heros = Heros()
monster = Monster(name = 'Pabo')

window = Tk()
window.title('One week to fight !')
background_image = PhotoImage(file ='owtf/images/fond.gif')
canvas = Canvas(window, width=1000, height=679)
canvas.create_image(500, 339, image = background_image)
canvas.pack()
image_mon_heros = PhotoImage(file='owtf/images/perso1-0.gif')
image_mon_heros1 = PhotoImage(file='owtf/images/perso1-1.gif')
image_mon_monstre = PhotoImage(file='owtf/images/monstre4.gif')
image_mon_monstre1 = PhotoImage(file='owtf/images/monstre4-3.gif')


canvas.create_image(220, 640, anchor = 's', image = image_mon_heros)
canvas.create_image(300, 640, anchor = 's', image = image_mon_heros1)
canvas.create_image(730, 640, anchor = 's', image = image_mon_monstre)
canvas.create_image(730, 590, anchor = 'center', image = image_mon_monstre1)




canvas.create_rectangle(3, 32, 203, 62, fill='grey')
longueur = (heros.pv*200)/heros.pv_max 
pv_bar_hero = canvas.create_rectangle(3, 32, 3+longueur, 62, fill='green')
canvas.create_text(10, 47, text='PV', anchor='w')
pv_text_hero = canvas.create_text(210, 47, anchor='w', text=str(heros.pv)+'/'+str(heros.pv_max))
canvas.create_rectangle(797, 32, 997, 62, fill='grey')
longueur = (monster.pv*200)/monster.pv_max 
pv_bar_monster = canvas.create_rectangle(997 - longueur, 32, 997, 62, fill='green')
canvas.create_text(990, 47, text='PV', anchor='e')
pv_text_monster = canvas.create_text(790, 47, anchor='e', text=str(monster.pv)+'/'+str(monster.pv_max))
canvas.create_rectangle(3, 66, 203, 96, fill='grey')
longueur = (heros.energie*200)/heros.energie_max 
energy_bar = canvas.create_rectangle(3, 66, 3+longueur, 96, fill='blue')
canvas.create_text(10, 79, text='Energie',anchor='w', fill='white')
energy_text = canvas.create_text(210, 79, anchor='w', text=str(heros.energie)+'/'+str(heros.energie_max))
score = 0
affichage_score = canvas.create_text(500, 5, anchor = 'n',font = ('Helvetica', -15), text='score : ' + str(score))
canvas.create_text(3, 0, anchor = 'nw',font = ('Helvetica', -30), text = 'Eric') #personnages.py pas update
canvas.create_text(997, 0, anchor = 'ne',font = ('Helvetica', -30), text = monster.name) #personnages.py pas update (anglais normalement)
# initialisation de la variable texte (ex: le mostre vous inflige 20 dégats)
middle_text = canvas.create_text(430, 200, anchor = 'center',font = ('Helvetica', -20), text = ' ')
window.mainloop()


"""


monstre3 : Grosmauch    --> stand-by [730, 640, anchor = 's']
                        --> attaque [730, 640, anchor = 's']
                        --> attend [730, 640, anchor = 's']
                        --> mort [730, 640, anchor = 's']

monstre1 : Pasbo        --> stand-by [730, 640, anchor = 's']
                        --> attaque [730, 640, anchor = 's']
                        --> attend [730, 640, anchor = 's']
                        --> mort [800, 600, anchor = 'center']

monstre4 : Toutvisqueut --> stand-by [730, 640, anchor = 's']
                        --> attaque [720, 660, anchor = 's']
                        --> attend [720, 630, anchor = 's']
                        --> mort [720, 685, anchor = 's']

Héros :                 --> stand-by [220, 640, anchor = 's']
                        --> attaque [250, 640, anchor = 's']
                        --> mort [220, 600, anchor = 'center']


"""
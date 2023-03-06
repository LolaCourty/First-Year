import os
import sys
import time
import threading
dossier_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dossier_parent)
from random import randint
from parametres import *
from tkinter import *
from PIL import ImageTk, Image
from src.personnage import *
from src.play import *
hero_name =''
image_hero = ""
image_monstre = ""
monster_name =''
message_score = ''
image_monstre_attaque = ''
image_monstre_reflechit = ''

pas_au_joueur = True #permet d'indiquer si le joueur a fini de jouer

from threading import Timer

def has_played():
    global pas_au_joueur
    if not pas_au_joueur :
        Timer(1.0, has_played).start()
    else :
        print("ouiii")


def retour_hero_normale(canvas, window, mon_heros):
    global image_hero
    image_mon_heros, position_mon_heros = right_image(mon_heros, None)
    image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    window.update()

def retour_monstre_normale(canvas, window, mon_monstre) :
    global image_monstre
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)

def update_bars(canvas, mon_heros, mon_monstre):
    global rectangle_monstre_pv, rectangle_hero_pv, rectangle_energy
    rectangle_monstre_pv = monster_pv_bar(canvas, mon_monstre.pv_max, mon_monstre.pv)
    rectangle_hero_pv = hero_pv_bar(canvas, mon_heros.pv_max, mon_heros.pv)
    rectangle_energy = energy_bar(canvas, mon_heros.energie_max, mon_heros.energie)



def do_button_small_attack(b1, b2, b3, b4, mon_heros, cible, canvas, window):
    """Fait l'action correspondante au bouton 'Attaque faible' et détruit ensuite tous les boutons.
    b1, b2, b3, b4 : boutons
    mon_heros et cible : personnages """
    global image_hero
    global rectangle_monstre_pv, rectangle_hero_pv, rectangle_energy
    global pas_au_joueur
    canvas.delete(image_hero)
    image_mon_heros_attaque, position_mon_heros_attaque = right_image(mon_heros, "attaque")
    image_hero_attaque = canvas.create_image(position_mon_heros_attaque[0],position_mon_heros_attaque[1], image = image_mon_heros_attaque)
    window.update()
    window.after(2000)
    mon_heros.attack(cible, "Attaque faible")
    canvas.delete(image_hero_attaque)
    #image_mon_heros, position_mon_heros = right_image(mon_heros, None)
    #image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    canvas.delete(rectangle_monstre_pv)
    canvas.delete(rectangle_energy)
    canvas.delete(rectangle_hero_pv)
    update_bars(canvas, mon_heros, mon_monstre)
    #canvas.create_rectangle(500,300,600,400, fill=red)
    #retour_hero_normale(canvas, window, mon_heros)
    window.update()
    pas_au_joueur = True
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    image_mon_heros, position_mon_heros = right_image(mon_heros, None)
    image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    window.update()
    pas_au_joueur = True

def do_button_medium_attack(b1, b2, b3, b4, mon_heros, cible, canvas, window):
    """Fait l'action correspondante au bouton 'Attaque moyenne' et détruit ensuite tous les boutons.
    b1, b2, b3 : boutons
    mon_heros et cible : personnages """
    global image_hero
    global pas_au_joueur
    canvas.delete(image_hero)
    image_mon_heros_attaque, position_mon_heros_attaque = right_image(mon_heros, "attaque")
    image_hero_attaque = canvas.create_image(position_mon_heros_attaque[0],position_mon_heros_attaque[1], image = image_mon_heros_attaque)
    window.update()
    window.after(2000)
    mon_heros.attack(cible, "Attaque moyenne")
    canvas.delete(image_hero_attaque)
    retour_hero_normale(canvas, window, mon_heros)
    image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    update_bars(canvas, mon_heros, mon_monstre)
    window.update()
    pas_au_joueur = True
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()

def do_button_big_attack(b1, b2, b3, b4, mon_heros, cible, canvas, window):
    """Fait l'action correspondante au bouton 'Attaque puissante' et détruit ensuite tous les boutons.
    b1, b2, b3 : boutons
    mon_heros et cible : personnages """
    global image_hero
    global pas_au_joueur
    canvas.delete(image_hero)
    image_mon_heros_attaque, position_mon_heros_attaque = right_image(mon_heros, "attaque")
    image_hero_attaque = canvas.create_image(position_mon_heros_attaque[0],position_mon_heros_attaque[1], image = image_mon_heros_attaque)
    window.update()
    window.after(2000)
    mon_heros.attack(cible, "Attaque puissante")
    canvas.delete(image_hero_attaque)
    retour_hero_normale(canvas, window, mon_heros)
    update_bars(canvas, mon_heros, mon_monstre)
    window.update()
    pas_au_joueur = True
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()

def buttons_attack(window, b1, b2, b3, mon_heros, cible, canvas, rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy, pas_au_joueur):
    """Crée trois boutons pour déterminer l'intensité de l'attaque, un autre pour le retour et détruit tous les précédents boutons.
    b1, b2, b3 : boutons
    mon_heros et cible : personnages
    window : fenêtre d'affichage 
    canvas : canevas
    image_hero : widget de l'image "classique" du héros"""
    b1.destroy()
    b2.destroy()
    b3.destroy()
    button_small_attack = Button(window, text = "Attaque faible")
    button_medium_attack = Button(window, text = "Attaque moyenne")
    button_big_attack = Button(window, text = "Attaque puissante")
    button_previous = Button(window, text = "Retour")
    button_small_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack, b4 = button_previous : do_button_small_attack(b1, b2, b3, b4, mon_heros, cible, canvas, window)
    button_medium_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack, b4 = button_previous : do_button_medium_attack(b1, b2, b3, b4, mon_heros, canvas, window)
    button_big_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack, b4 = button_previous : do_button_big_attack( b1, b2, b3, b4, mon_heros, cible, canvas, window)
    button_previous['command'] = lambda b1=b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack, b4 = button_previous : display_buttons_action(window, canvas, mon_heros, cible, rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy, b1, b2, b3, b4)
    button_window1 = canvas.create_window(400,590, anchor = 'nw', window = button_small_attack)
    button_window2 = canvas.create_window(400,620, anchor = 'nw', window = button_medium_attack)
    button_window3 = canvas.create_window(400,650, anchor = 'nw', window = button_big_attack)
    button_window4 = canvas.create_window(400,680, anchor = 'nw', window = button_previous)

def do_button_healing(b1, b2,b3, mon_heros, mon_monstre, canvas):
    """Fait l'action correspondante au bouton "Se soigner" et détruit tous les boutons.
    b1, b2, b3 : boutons
    mon_heros : héros """
    global pas_au_joueur
    mon_heros.healing()
    update_bars(canvas, mon_heros, mon_monstre)
    pas_au_joueur = True
    b1.destroy()
    b2.destroy()
    b3.destroy()

def do_button_waiting(b1, b2,b3, mon_heros, mon_monstre, canvas):
    """Fait l'action correspondante au bouton "Attendre" et détruit tous les boutons.
    b1, b2, b3 : boutons
    mon_heros : héros """
    global pas_au_joueur
    mon_heros.waiting()
    update_bars(canvas, mon_heros, mon_monstre)
    pas_au_joueur = True
    b1.destroy()
    b2.destroy()
    b3.destroy()



def display_buttons_action(window, canvas, mon_heros, cible, rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy, b1 = None, b2 = None, b3 = None, b4 = None):
    """ Crée trois boutons 'Attendre', 'Se soigner' et 'Attaquer
    canvas : canevas 
    mon_heros et cible : personnages
    window : fenêtre d'affichage """

    if type(b1) != None:
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()

    pas_au_joueur = False
    button_waiting = Button(window, text = "Attendre")
    button_healing = Button(window, text = "Se soigner")
    button_attacking = Button(window, text = "Attaquer")
    button_healing['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : do_button_healing(b1, b2, b3, mon_heros, cible, canvas)
    button_waiting['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : do_button_waiting(b1, b2, b3, mon_heros, cible, canvas)
    button_attacking['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : buttons_attack(window, b1, b2, b3, mon_heros, cible, canvas, rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy, pas_au_joueur)
    button_window1 = canvas.create_window(400,590, anchor = 'nw', window = button_healing)
    button_window2 = canvas.create_window(400,620, anchor = 'nw', window = button_waiting)
    button_window3 = canvas.create_window(400,650, anchor = 'nw', window = button_attacking)

def right_image(mon_perso, action):
    """Renvoie l'image, ainsi que sa position optimale (liste [abscisse, ordonnée])"""
    if type(mon_perso) == Heros: 
        if action == 'mort':
            return(PhotoImage(file='owtf/images/perso1-8.gif'), [250, 570])
        else:
            if action == None :
                return(PhotoImage(file='owtf/images/perso1-0.gif'), [150, 450])
            else :
                return(PhotoImage(file='owtf/images/perso1-1.gif'), [150, 450])
    else :
        if mon_perso.name == 'Pabo':
            if action == None :
                return(PhotoImage(file= 'owtf/images/monstre1.gif'), [730, 450])
            elif action == "reflechit":
                return(PhotoImage(file= 'owtf/images/monstre1-1.gif'), [730, 400])
            elif action == "attaque" :
                return(PhotoImage(file= 'owtf/images/monstre1-2.gif'), [730, 420])
            else :
                return(PhotoImage(file= 'owtf/images/monstre1-3.gif'), [730, 450])
        elif mon_perso.name == 'Gromauch' :
            if action == None :
                return(PhotoImage(file='owtf/images/monstre3.gif'), [830, 500])
            elif action == "reflechit":
                return(PhotoImage(file='owtf/images/monstre3-1.gif'), [830, 500])
            elif action == "attaque" :
                return(PhotoImage(file='owtf/images/monstre3-2.gif'), [830, 500])
            else :
                return(PhotoImage(file= 'owtf/images/monstre3-3.gif'), [830, 500])
        else :
            if action == None :
                return(PhotoImage(file='owtf/images/monstre4.gif'), [775, 500])
            elif action == "reflechit":
                return(PhotoImage(file='owtf/images/monstre4-1.gif'), [775, 500])
            elif action == "attaque" :
                return(PhotoImage(file='owtf/images/monstre4-2.gif'), [775, 500])
            else :
                return(PhotoImage(file='owtf/images/monstre4-3.gif'), [775, 500])

def hero_pv_bar(canvas, PV_max, PV):
    """Affiche une barre représentant la proportion de PV du héros par rapport à leur nombre maximal
    canvas : canevas
    Pv_max, Pv : int """

    canvas.create_rectangle(3, 30, 203, 60, fill='red')
    #Calcul la longueur du rectangle interne
    longueur = (PV*200)/PV_max 
    rectangle = canvas.create_rectangle(3, 30, 3+longueur, 60, fill='green')
    canvas.create_text(23, 45, text='PV')
    return(rectangle)

def monster_pv_bar(canvas, PV_max, PV):
    """Affiche une barre représentant la proportion de PV du monstre par rapport à leur nombre maximal
    canvas : canevas
    Pv_max, Pv : int """

    canvas.create_rectangle(797, 30, 997, 60, fill='red')
    #Calcul la longueur du rectangle interne
    longueur = (PV*200)/PV_max 
    rectangle = canvas.create_rectangle(997 - longueur, 30, 997, 60, fill='green')
    canvas.create_text(977, 45, text='PV')
    return(rectangle)

def energy_bar(canvas, energy_max, energy):
    """Affiche une barre représentant la proportion d'énergie par rapport à sa valeur maximale
    canvas : canevas
    energy_max, energy : int """
    canvas.create_rectangle(3, 64, 203, 94, fill='red')
    #Calcul la longueur du rectangle interne, représentant la proportion de PV rpar rapport à leur nombre maximal
    longueur = (energy*200)/energy_max 
    rectangle =canvas.create_rectangle(3, 64, 3+longueur, 94, fill='blue')
    canvas.create_text(23, 77, text='Energie')
    return(rectangle)

def get_name(window, var):
    """Cette fonction récupère le nom du héros et détruit la fenêtre correspondante."""
    global hero_name
    hero_name = var.get()
    window.destroy()

def endless_monster_affichage(mon_heros, mon_monstre, score, window, canvas) :
    """ si un monstre meurt, un autre tout frais prend sa place et on met à jour l'argent et le score du héros, ainsi que l'affichage"""
    global image_monstre
    global monster_name
    heros.argent += 50
    canvas.delete(image_monstre)
    canvas.delete(monster_name)
    a = random.randint(1,3)
    if a == 1:
        mon_monstre = Monster('Pabo')
        image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
        image_monstre = canvas.create_image(position_mon_monstre[0], position_mon_monstre[1], image=image_mon_monstre)
        monster_name = canvas.create_text(796, 70, anchor = 'nw',font = ('Helvetica', -30), text = mon_monstre.name)
        window.update()
    elif a == 2:
        mon_monstre = Monster('Gromauch')
        image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
        image_monstre = canvas.create_image(position_mon_monstre[0], position_mon_monstre[1], image=image_mon_monstre)
        monster_name = canvas.create_text(796, 70, anchor = 'nw',font = ('Helvetica', -30), text = mon_monstre.name)
        window.update()
    else :
        mon_monstre = Monster('Touvisqeut')
        image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
        image_monstre = canvas.create_image(position_mon_monstre[0], position_mon_monstre[1], image=image_mon_monstre)
        monster_name = canvas.create_text(796, 70, anchor = 'nw',font = ('Helvetica', -30), text = mon_monstre.name)
        window.update()
    score += 100
    return score, mon_monstre

def tour_du_heros_affichage(window, canvas, mon_heros, mon_monstre, rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy, score):
    """Cette fonction réalise le tour du héros en lui affichant les différentes actions possibles. Elle met aussi à jour les barres de vie et d'énergie et les renvoie. """ 
    display_buttons_action(window, canvas, mon_heros, mon_monstre, rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy)
    window.update()
    if mon_monstre.is_dead():
        image_mon_monstre_mort, position_mon_monstre_mort = right_image(mon_monstre, "mort")
        image_monstre_mort = canvas.create_image(position_mon_monstre_mort[0], position_mon_monstre_mort[1], image=image_mon_monstre_mort)
        message_mort_monstre = canvas.create_text(500, 200, anchor = 'nw',font = ('Helvetica', -30), text=DEAD_MONSTER_MSG)
        window.after(3)
        canvas.delete(message_mort_monstre)
        score, mon_monstre = endless_monster_affichage(mon_heros, mon_monstre, score, window, canvas)
        rectangle_monstre_pv = monster_pv_bar(canvas, mon_monstre.pv_max, mon_monstre.pv)
        canvas.delete(message_score)
        message_score = canvas.create_text(500, 5, anchor = 'n',font = ('Helvetica', -15), text='score : ' + str(score))
        window.update()
    return(mon_monstre)

def normal_a_reflechit(window, canvas, mon_monstre):
    global image_monstre_reflechit
    global image_monstre
    canvas.delete(image_monstre)
    image_mon_monstre_reflechit, position_mon_monstre_reflechit = right_image(mon_monstre, "reflechit")
    image_monstre_reflechit = canvas.create_image(position_mon_monstre_reflechit[0], position_mon_monstre_reflechit[1], image=image_mon_monstre_reflechit)
    window.update()

def reflechit_a_attaque(window, canvas, mon_monstre):
    """ Cette fonction permet de passer de l'affichage "le monstre réfléchit" au "monstre attaque" """
    global image_monstre_reflechit
    global image_monstre_attaque
    canvas.delete(image_monstre_reflechit)
    image_mon_monstre_attaque, position_mon_monstre_attaque = right_image(mon_monstre, "attaque")
    image_monstre_attaque = canvas.create_image(position_mon_monstre_attaque[0], position_mon_monstre_attaque[1], image=image_mon_monstre_attaque)
    window.update()


def tour_du_monstre(window, canvas, mon_heros, mon_monstre):
    """Cette fonction réalise le tour du monstre : faire l'attaque en mettant à jour l'affichage, et les barres de vie et d'énergie."""
    global image_monstre
    global image_monstre_attaque
    global rectangle_monstre_pv, rectangle_hero_pv, rectangle_energy
    window.after(1000)
    window.after(2000, normal_a_reflechit(window, canvas, mon_monstre))
    window.after(2000, reflechit_a_attaque(window, canvas, mon_monstre))
    mon_monstre.monster_attack(mon_heros)
    canvas.delete(image_monstre_attaque)
    retour_monstre_normale(canvas, window, mon_monstre)
    canvas.delete(rectangle_monstre_pv)
    canvas.delete(rectangle_energy)
    canvas.delete(rectangle_hero_pv)
    update_bars(canvas, mon_heros, mon_monstre)
    window.update()

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
    return score, hero_name, monster


def game_play_affichage():
    """Affiche la fenêtre initiale de jeu. 
    mon_heros, mon_monstre : personnages """
    global rectangle_monstre_pv, rectangle_hero_pv, rectangle_energy
    global image_hero
    global image_monstre
    global monster_name
    global message_score
    global pas_au_joueur
    score, hero_name, mon_monstre = init_affichage()
    mon_heros = Heros(name=hero_name)
    window = Tk()
    window.title('One week to fight !')
    background_image = PhotoImage(file ='owtf/images/fond.gif')
    canvas = Canvas(window, width=1000, height=679)
    canvas.create_image(500, 339, image = background_image)
    canvas.pack()
    image_mon_heros, position_mon_heros = right_image(mon_heros, None)
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
    image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    rectangle_hero_pv = hero_pv_bar(canvas, mon_heros.pv_max, mon_heros.pv)
    rectangle_monstre_pv =monster_pv_bar(canvas, mon_monstre.pv_max, mon_monstre.pv)
    rectangle_energy =energy_bar(canvas, mon_heros.energie_max, mon_heros.energie)
    message_score = canvas.create_text(500, 5, anchor = 'n',font = ('Helvetica', -15), text='score : ' + str(score))
    canvas.create_text(140, 210, anchor = 'center',font = ('Helvetica', -30), text = mon_heros.name) #personnages.py pas update
    monster_name = canvas.create_text(796, 70, anchor = 'nw',font = ('Helvetica', -30), text = mon_monstre.name) #personnages.py pas update (anglais normalement)
    while not mon_heros.is_dead():
            # on regarde l'initiative pour définir qui agit en premier
            if mon_heros.initiative < mon_monstre.initiative:
                if pas_au_joueur : #vérifie que le joueur a bien fini son tour
                    tour_du_monstre(window, canvas, mon_heros, mon_monstre)
                    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
                    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
                    window.update()
                # on sort de la boucle lorsque le héro décède
                if mon_heros.is_dead():
                    message_fin = canvas.create_text(500, 200, anchor = 'nw',font = ('Helvetica', -30), text= DEAD_MSG)
                    window.mainloop()
                pas_au_joueur = False
                mon_monstre = tour_du_heros_affichage(window, canvas, mon_heros, mon_monstre, rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy, score)
                image_mon_heros, position_mon_heros = right_image(mon_heros, None)
                image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
            elif mon_heros.initiative > mon_monstre.initiative :
                mon_monstre = tour_du_heros_affichage(window, canvas, mon_heros, mon_monstre, rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy, score)
                if pas_au_joueur :
                    tour_du_monstre(window, canvas, mon_heros, mon_monstre)
                    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
                    window.update()
                    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
                #on sort de la boucle lorsque le héro décède
                if mon_heros.is_dead() :
                    message_fin = canvas.create_text(500, 200, anchor = 'nw',font = ('Helvetica', -30), text= DEAD_MSG)
                    window.mainloop()
            else :
                #si les deux personnages ont la même initiative, on tire à pile ou face
                rd = randint(1,2)
                if rd == 1:
                    if pas_au_joueur :
                        tour_du_monstre(window, canvas, mon_heros, mon_monstre)
                        image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
                        image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
                        window.update()
                    if mon_heros.is_dead() :
                        message_fin = canvas.create_text(500, 200, anchor = 'nw',font = ('Helvetica', -30), text= DEAD_MSG)
                        window.mainloop()
                    mon_monstre = tour_du_heros_affichage(window, canvas, mon_heros, mon_monstre, rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy, score)
                else :
                    mon_monstre = tour_du_heros_affichage(window, canvas, mon_heros, mon_monstre, rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy, score)
                    if pas_au_joueur :
                        tour_du_monstre(window, canvas, mon_heros, mon_monstre)
                        image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
                        image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
                        window.update()
                    if mon_heros.is_dead() :
                        message_fin = canvas.create_text(500, 200, anchor = 'nw',font = ('Helvetica', -30), text= DEAD_MSG)
                        window.mainloop()
                    

            
#game_play_affichage()

score, hero_name, mon_monstre = init_affichage()
mon_heros = Heros(name=hero_name)
window = Tk()
window.title('One week to fight !')
background_image = PhotoImage(file ='owtf/images/fond.gif')
canvas = Canvas(window, width=1000, height=679)
canvas.create_image(500, 339, image = background_image)
canvas.pack()
image_mon_heros, position_mon_heros = right_image(mon_heros, None)
image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
rectangle_hero_pv = hero_pv_bar(canvas, mon_heros.pv_max, mon_heros.pv)
rectangle_monstre_pv =monster_pv_bar(canvas, mon_monstre.pv_max, mon_monstre.pv)
rectangle_energy =energy_bar(canvas, mon_heros.energie_max, mon_heros.energie)
message_score = canvas.create_text(500, 5, anchor = 'n',font = ('Helvetica', -15), text='score : ' + str(score))
canvas.create_text(140, 210, anchor = 'center',font = ('Helvetica', -30), text = mon_heros.name)
monster_name = canvas.create_text(796, 70, anchor = 'nw',font = ('Helvetica', -30), text = mon_monstre.name)

tour_du_monstre(window, canvas, mon_heros, mon_monstre)
image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
pas_au_joueur = False
compteur = 0
mon_monstre = tour_du_heros_affichage(window, canvas, mon_heros, mon_monstre, rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy, score)
Timer(1.0, has_played).start()
print('uo')
image_mon_heros, position_mon_heros = right_image(mon_heros, None)
image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)

#image_mon_heros, position_mon_heros = right_image(mon_heros, None)

window.update()
"""
window.after(1000)
window.after(2000, normal_a_reflechit(window, canvas, mon_monstre))
window.after(2000, reflechit_a_attaque(window, canvas, mon_monstre))
mon_monstre.monster_attack(mon_heros)
canvas.delete(image_monstre_attaque)
image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
canvas.delete(rectangle_monstre_pv)
canvas.delete(rectangle_energy)
canvas.delete(rectangle_hero_pv)
rectangle_monstre_pv = monster_pv_bar(canvas, mon_monstre.pv_max, mon_monstre.pv)
rectangle_hero_pv = hero_pv_bar(canvas, mon_heros.pv_max, mon_heros.pv)
rectangle_energy = energy_bar(canvas, mon_heros.energie_max, mon_heros.energie)

"""

window.mainloop()

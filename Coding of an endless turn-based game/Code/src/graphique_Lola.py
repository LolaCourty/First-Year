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
a_fini = True
pas_au_joueur = True #permet d'indiquer si le joueur a fini de jouer

from threading import Timer

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = Timer(sec, func_wrapper)
    t.start()
    return t

def wait():
    i = 0
    pygame.init()
    print('yo')
    while i == 0 :
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.QUIT
                sys.exit()
            if event.type == 1:
                i=1



def retour_hero_normale(canvas, window, mon_heros):
    global image_hero
    image_mon_heros, position_mon_heros = right_image(mon_heros, None)
    image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)


def retour_monstre_normale(canvas, window, mon_monstre) :
    global image_monstre
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)


def update_bars(canvas, mon_heros, mon_monstre):
    global rectangle_monstre_pv, rectangle_hero_pv, rectangle_energy
    rectangle_monstre_pv = monster_pv_bar(canvas, mon_monstre.pv_max, mon_monstre.pv)
    rectangle_hero_pv = hero_pv_bar(canvas, mon_heros.pv_max, mon_heros.pv)
    rectangle_energy = energy_bar(canvas, mon_heros.energie_max, mon_heros.energie)



def do_button_small_attack(b1, b2, b3, mon_heros, cible, canvas, window):
    """Fait l'action correspondante au bouton 'Attaque faible' et détruit ensuite tous les boutons.
    b1, b2, b3 : boutons
    mon_heros et cible : personnages """
    b1.destroy()
    b2.destroy()
    b3.destroy()
    global pas_au_joueur
    canvas.delete(image_hero)
    image_mon_heros_attaque, position_mon_heros_attaque = right_image(mon_heros, "attaque")
    image_hero = canvas.create_image(position_mon_heros_attaque[0],position_mon_heros_attaque[1], image = image_mon_heros_attaque)
    window.update()
    window.after(2000)
    mon_heros.attack(cible, "Attaque puissante")
    canvas.delete(image_hero)
    update_bars(canvas, mon_heros, cible)
    window.update()
    pas_au_joueur = True


def do_button_medium_attack(b1, b2, b3, mon_heros, cible, canvas, window):
    """Fait l'action correspondante au bouton 'Attaque moyenne' et détruit ensuite tous les boutons.
    b1, b2, b3 : boutons
    mon_heros et cible : personnages """
    b1.destroy()
    b2.destroy()
    b3.destroy()
    global pas_au_joueur
    canvas.delete(image_hero)
    image_mon_heros_attaque, position_mon_heros_attaque = right_image(mon_heros, "attaque")
    image_hero = canvas.create_image(position_mon_heros_attaque[0],position_mon_heros_attaque[1], image = image_mon_heros_attaque)
    window.update()
    window.after(2000)
    mon_heros.attack(cible, "Attaque moyenne")
    canvas.delete(image_hero)
    update_bars(canvas, mon_heros, cible)
    window.update()
    pas_au_joueur = True


def do_button_big_attack(b1, b2, b3, mon_heros, cible, canvas, window):
    """Fait l'action correspondante au bouton 'Attaque puissante' et détruit ensuite tous les boutons.
    b1, b2, b3 : boutons
    mon_heros et cible : personnages """
    canvas.delete(image_hero)
    image_mon_heros_attaque, position_mon_heros_attaque = right_image(mon_heros, "attaque")
    image_hero = canvas.create_image(position_mon_heros_attaque[0],position_mon_heros_attaque[1], image = image_mon_heros_attaque)
    window.update()
    mon_heros.attack(cible, "Attaque puissante")
    canvas.delete(image_hero)
    update_bars(canvas, mon_heros, cible)
    window.update()
    pas_au_joueur = True


def buttons_attack(window, b1, b2, b3, mon_heros, cible, canvas):
    """Crée trois boutons pour déterminer l'intensité de l'attaque et détruit tous les précédents boutons.
    b1, b2, b3 : boutons
    mon_heros et cible : personnages
    window : fenêtre d'affichage 
    canvas : canevas
    image_hero : widget de l'image "classique" du héros"""
    global image_hero
    b1.destroy()
    b2.destroy()
    b3.destroy()
    button_small_attack = Button(window, text = "Attaque faible")
    button_medium_attack = Button(window, text = "Attaque moyenne")
    button_big_attack = Button(window, text = "Attaque puissante")
    button_small_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack : do_button_small_attack(b1, b2, b3, mon_heros, cible, canvas, window)
    button_medium_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack : do_button_medium_attack(b1, b2, b3, mon_heros, cible, canvas, window)
    button_big_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack : do_button_big_attack( b1, b2, b3, mon_heros, cible, canvas, window)
    button_window1 = canvas.create_window(400,590, anchor = 'center', window = button_small_attack)
    button_window2 = canvas.create_window(400,620, anchor = 'center', window = button_medium_attack)
    button_window3 = canvas.create_window(400,650, anchor = 'center', window = button_big_attack)


def buttons_attack2(window, b1, b2, b3, mon_heros, cible, canvas, image_hero):
    frame_attack = Frame(window)
    button_small_attack = Button(window, text = "Attaque faible")
    button_medium_attack = Button(window, text = "Attaque moyenne")
    button_big_attack = Button(window, text = "Attaque puissante")
    button_small_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack : do_button_small_attack(b1, b2, b3, mon_heros, cible, canvas, window)
    button_medium_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack : do_button_medium_attack(b1, b2, b3, mon_heros, cible, canvas, window)
    button_big_attack['command']= lambda b1=button_small_attack, b2=button_medium_attack, b3=button_big_attack : do_button_big_attack( b1, b2, b3, mon_heros, cible, canvas, window, image_hero)
    button_small_attack.pack()
    button_medium_attack.pack()
    button_big_attack.pack()


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


def display_buttons_action(window, canvas, mon_heros, cible, image_hero):
    """ Crée trois boutons 'Attendre', 'Se soigner' et 'Attaquer
    canvas : canevas
    mon_heros et cible : personnages
    window : fenêtre d'affichage """
    global rectangle_hero_pv, rectangle_monstre_pv, rectangle_energy
    button_waiting = Button(window, text = "Attendre")
    button_healing = Button(window, text = "Se soigner")
    button_attacking = Button(window, text = "Attaquer")
    button_healing['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : do_button_healing(b1, b2, b3, mon_heros, cible, canvas)
    button_waiting['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : do_button_waiting(b1, b2, b3, mon_heros, cible, canvas)
    button_attacking['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : buttons_attack(window, b1, b2, b3, mon_heros, cible, canvas)
    button_window1 = canvas.create_window(400,590, anchor = 'nw', window = button_healing)
    button_window2 = canvas.create_window(400,620, anchor = 'nw', window = button_waiting)
    button_window3 = canvas.create_window(400,650, anchor = 'nw', window = button_attacking)


def display_buttons_action2(canvas, mon_heros, cible, image_hero):
    windowb = Tk()
    button_waiting = Button(windowb, text = "Attendre")
    button_healing = Button(windowb, text = "Se soigner")
    button_attacking = Button(windowb, text = "Attaquer")
    button_healing['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : do_button_healing(b1, b2, b3, mon_heros, cible, canvas)
    button_waiting['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : do_button_waiting(b1, b2, b3, mon_heros, cible, canvas)
    button_attacking['command']= lambda b1=button_healing, b2=button_waiting, b3=button_attacking : buttons_attack(window, b1, b2, b3, mon_heros, cible, canvas, image_hero)
    button_waiting.pack()
    button_healing.pack()
    button_attacking.pack()
    windowb.mainloop


def right_image(mon_perso, action):
    """Renvoie l'image, ainsi que sa position optimale (liste [abscisse, ordonnée])"""
    if type(mon_perso) == Heros:
        if mon_perso.pv == 0:
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
    mon_heros.argent += 50
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

def tour_du_heros_affichage(window, canvas, mon_heros, mon_monstre, image_hero):
    """Cette fonction réalise le tour du héros en lui affichant les différentes actions possibles. Elle met aussi à jour les barres de vie et d'énergie et les renvoie. """ 
    display_buttons_action(window, canvas, mon_heros, mon_monstre, image_hero)
    image_mon_heros, position_mon_heros = right_image(mon_heros, None)
    image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    window.update()
    


def tour_du_monstre(window, canvas, mon_heros, mon_monstre):
    """Cette fonction réalise le tour du monstre : faire l'attaque en mettant à jour l'affichage, et les barres de vie et d'énergie."""
    global rectangle_monstre_pv, rectangle_hero_pv, rectangle_energy
    global image_monstre
    window.after(1000)
    canvas.delete(image_monstre)
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, 'reflechit')
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    window.update()
    window.after(2000)
    canvas.delete(image_monstre)
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, 'attaque')
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    window.update()
    mon_monstre.monster_attack(mon_heros)
    window.after(1000)
    canvas.delete(image_monstre)
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    window.update()
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


def tour_de_jeu(window, canvas, mon_heros, mon_monstre, score, message_score):
    image_mon_monstre, position_mon_monstre_mort = right_image(mon_monstre, None)
    window.image_mon_monstre = image_mon_monstre
    image_monstre = canvas.create_image(position_mon_monstre_mort[0], position_mon_monstre_mort[1], image=image_mon_monstre)
    canvas.delete(image_monstre)
    if mon_monstre.is_dead():
        image_mon_monstre_mort, position_mon_monstre_mort = right_image(mon_monstre, "mort")
        image_monstre = canvas.create_image(position_mon_monstre_mort[0], position_mon_monstre_mort[1], image=image_mon_monstre_mort)
        message_mort_monstre = canvas.create_text(500, 200, anchor = 'nw',font = ('Helvetica', -30), text=DEAD_MONSTER_MSG)
        window.update()
        window.after(3000)
        canvas.delete(message_mort_monstre)
        canvas.delete(image_monstre)
        canvas.delete(message_score)
        window.update()
        score, mon_monstre = endless_monster_affichage(mon_heros, mon_monstre, score, window, canvas)
        message_score = canvas.create_text(500, 5, anchor = 'n',font = ('Helvetica', -15), text='score : ' + str(score))
        rectangle_monstre_pv = monster_pv_bar(canvas, mon_monstre.pv_max, mon_monstre.pv)
        window.update()
    image_mon_heros, position_mon_heros = right_image(mon_heros, None)
    image_hero = canvas.create_image(position_mon_heros[0],position_mon_heros[1], image = image_mon_heros)
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    window.update()
    image_monstre = tour_du_monstre(window, canvas, mon_heros, mon_monstre, image_monstre)
    canvas.delete(image_monstre)
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
    window.image_mon_monstre = image_mon_monstre
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    window.update()
    tour_du_monstre(window, canvas, mon_heros, mon_monstre)
    if not mon_heros.is_dead():
        display_buttons_action(window, canvas, mon_heros, mon_monstre)
        image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
        window.update()
        tour_suivant = Button(window, text = 'tour suivant', command = lambda : tour_de_jeu(window, canvas, mon_heros, mon_monstre, score, message_score))
        button_tour_suivant = canvas.create_window(500, 200, window = tour_suivant)
    else :
        return window
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    window.update()
    display_buttons_action2(canvas, mon_heros, mon_monstre, image_hero)
    image_mon_monstre, position_mon_monstre = right_image(mon_monstre, None)
    image_monstre = canvas.create_image(position_mon_monstre[0],position_mon_monstre[1], image = image_mon_monstre)
    window.update()

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
tour_de_jeu(window, canvas, mon_heros, mon_monstre, score, message_score)

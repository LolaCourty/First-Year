# Projet 

## Description

Combats Pokémon Like Infinis
Il s'agit de combat en tour par tour. Le joueur contrôle un héros, l'ordinateur contrôle un monstre. Le héros et le monstre jouent chacun leur tour (dans l'ordre des initiatives décroissantes. En cas d'égalité d'initiative, l'ordre est tiré aléatoirement à chaque tour de jeu.) Le héros à le choix entre attaquer, se soigner et ne rien faire, alors que le monstre attaque à chaque tour de jeu. Il existe trois types d'attaque, de différent cout et puissance.

Lors de sa création, le héros possède :

Points de vie : 100
Energie : 100
Argent : 0
Par tour, 20 points d’énergie
Attaques (épéiste, mage, archer) :
-    Eraflure : coût 10 en énergie, points d’attaque compris entre 5 et 15.
-    Entaille : coût 30 en énergie, points d’attaque compris entre 20 et 30.
-    Hémorragie : coût 50 en énergie, points d’attaque compris entre 35 et 55.
Se soigner : 20 PV.
Attendre : 15 points d’énergie (en plus des 20 points d’office)
Pour chaque monstre tué, le héros gagne une certaine somme d'argent lui permettant de se soigner ou d'acheter des améliorations.

## Comment lancer le jeu

Pour lancer le jeu en mode console, taper dans la console la commande suivante : 
```bash
python run_console.py
```

Pour lancer le jeu en mode graphique, taper dans la console la commande suivante :
```bash
python run_graphique.py
```

Au besoin, installer playsound avec la commande :
```bash
pip install playsound
```

## Membres de l'équipe et Rôle

Hugues CHARDIN : Méthodes
Lola COURTY : Interface graphique
Gabriel MARTIN : Interface graphique
Morgane ROUBY : Initialisation des classes + Paramétrisation
Soufiane SEBBAN : Tests

## Conventions

Les classes sont nommées selon la nommenclature : MaClasse
Les fonctions et méthodes selon la nommenclature : ma_fonction / ma_methode
Les paramètres / données du jeu sont stockés dans le fichier parametres.py et nommés selon la nommenclature : MON_PARAMETRE

# Objectifs et Jalons

Le MVP sera constitué d'une première version du jeu en mode console, sans question de placement.
Dans un second temps nous pourrons implémenter une interface graphique et un système de déplacements (avec points de mouvements et portés des attaques).

### Sprint 0 : Organisation
	> Réflexion autour de la conception
	> Organisation du projet
	> Mise en place du git, délégué de groupe, etc.

## Objectif 1 : Le jeu en mode console (MVP)

### Sprint 1 : Les données du jeu
	> Fonctionnalité 1 : Classes Personnage, Héros, Monstre

### Sprint 2 : Actions des joueurs
	> Fonctionnalité 2 : Attaquer
	> Fonctionnalité 3 : Se soigner
	> Fonctionnalité 4 : Attendre

### Sprint 3 : Action aléatoire de l'ordinateur
	> Fonctionnalité 5 : Un tour aléatoire de l'ordinateur

### Sprint 4 : Début et fin de jeu
	> Fonctionnalité 6 : Initialisation du jeu
	> Fonctionnalité 7 : Fin du jeu (mort)

### Sprint 5 : Une première version console
	> Fonctionnalité 8 : Faire jouer le joueur
    > Fonctionnalité 9 : Enchaîner les monstres

## Objectif 2 : Une interface graphique

### Sprint 6 : Une première interface très basique
    > Fonctionnalité 11 : Afficher le terrain et les personnages/adversaires
    > Fonctionnalité 12 : Afficher les données (PV, énergie, score)

### Sprint 8 : Jouer
    > Fonctionnalité 13 : Faire jouer le joueur
    > Fonctionnalité 14 : Faire jouer l'ordinateur

### Sprint 7 : Esthétique de jeu
    > Fonctionnalité 15 : Ajout d'images pour attaques, soins
    > Fonctionnalité 16 : Playlist
    > Fonctionnalité 17 : Ajouter une jauge de distance (nombre de positions fixes) pour débloquer certaines attaques

## Objectif 3 : Nouvelles fonctionnalités (optionnelles)

### Sprint 8 : Améliorer l'ergonomie
    > Fonctionnalité 18 : Menu accueil + statistiques (meilleur score)
    > Fonctionnalité 19 : Menu pause
    > Fonctionnalité 20 : Augmenter le niveau des monstres + amélioration des équipements

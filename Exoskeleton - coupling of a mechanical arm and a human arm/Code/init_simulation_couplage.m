%%% Initialisation des paramètres pour la simulation du système couplé

%Paramètres
cond_ini = [-pi/4; pi/4; -pi/4; 0]; %Postions angulaires initiales (theta1, theta2, theat3), ajout d'un 0 pour le système matriciel
cond_ini_vitesse = [0; 0; 0; 0];
couples = [0; 0; 0; 0]; %Entrées
L0 = 1; 
L1 = 1; 
L2 = 1; 
m1 = 1;
m2 = 1;
m3 = 1; 
L3 = 1; 
l3 = 0.5*L3;
l1 =0.5*L1;
l2 = 0.5*L2;
inertie = [10; 10; 10]; %en kg.m^2
inertie_a = [0 0 0 0; 0 0 0 0; 0 0 0 0; 0 0 0 0]; %Inertie des actionneurs
parametres = [m1; m2; m3; L1; L2; L3; l1; l2; l3; L0];


 
    



%
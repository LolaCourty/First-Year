%%% Bras 
b = 12; %longueur entre l'épaule et le coude
a = 10; %longueur entre le coude et le poignet
cond_ini = [10; 10; 10; 0]; %trois angles pour l'épaule, un pour le coude

theta_x = out.simout3.signals.values;

%Déplacement du coude
x_ec = out.simout.signals.values;
y_ec = out.simout1.signals.values;
z_ec = out.simout2.signals.values;
ax1 = nexttile;
plot(ax1, theta_x, x_ec, 'r');
hold on;
plot(ax1, theta_x, y_ec, 'b');
hold on; 
plot(ax1, theta_x, z_ec, 'g');
legend('x_{ec}', 'y_{ec}', 'z_{ec}');
title('Théta_x varie entre 10 et 240 degrés');
ax2 = nexttile;
plot3(ax2, x_ec, y_ec, z_ec);
title('Déplacement du coude pour une variation de théta_x')
grid on ;

%Déplacement du poignet par rapport au coude
x_cm = out.simout4.signals.values;
y_cm = out.simout5.signals.values;
z_cm = out.simout6.signals.values;
ax3 = nexttile;
plot(ax3, theta_x, x_cm, 'r');
hold on;
plot(ax3, theta_x, y_cm, 'b');
hold on; 
plot(ax3, theta_x, z_cm, 'g');
legend('x_{cm}', 'y_{cm}', 'z_{cm}');
ax4 = nexttile;
plot3(ax4, x_cm, y_cm, z_cm);
title('Déplacement du poignet par rapport au coude (phi = 0)')
grid on ;

%Déplacement du poignet par rapport à l'épaule
x_em = out.simout7.signals.values;
y_em = out.simout8.signals.values;
z_em = out.simout9.signals.values;
ax5 = nexttile;
plot(ax5, theta_x, x_em, 'r');
hold on;
plot(ax5, theta_x, y_em, 'b');
hold on; 
plot(ax5, theta_x, z_em, 'g');
legend('x_{ec}', 'y_{ec}', 'z_{ec}');
ax6 = nexttile;
plot3(ax6, x_em, y_em, z_em)
title("Déplacement du poignet par rapport à l'épaule (phi = 0)")


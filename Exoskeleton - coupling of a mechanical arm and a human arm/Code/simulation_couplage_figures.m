%%% Figures et animation issues de la simulation du système couplé

figure
tiledlayout(2,1);

%Effort au niveau de la liaison type pivot-glissière
ax1 = nexttile;
temps = out.simout3.time;
effort = out.simout3.signals.values;
plot(ax1, temps, effort);
xlabel('Temps (s)')
ylabel('Effort (N)');
title('Effort au niveau de la liaison type pivot-glissière')
grid on

%Positions angulaires en fonction du temps
ax2 = nexttile;

theta1 = out.simout.signals.values;
theta2 = out.simout1.signals.values;
theta3 = out.simout2.signals.values;
theta1 = squeeze(theta1);
theta2 = squeeze(theta2);
theta3 = squeeze(theta3);
plot(ax2, temps, theta1);
xlabel('Temps (s)')
hold on;
plot(ax2, temps, theta2+theta1);
hold on;
plot(ax2, temps, theta3);
legend('Theta1 (rad)','Theta1 + théta2 (rad)','Theta3 (rad)');
title('Positions angulaires')


%Initialisation de la figure animée
x1= L1*cos(cond_ini(1));
y1 = L1*sin(cond_ini(1));
x2 =  L1*cos(cond_ini(1)) + L2*cos(cond_ini(1)+cond_ini(2));
y2 = L1*sin(cond_ini(1)) + L2*sin(cond_ini(1) + cond_ini(2));
x3 = L0;
y3 =0;
x4 = L0 + L3*cos(cond_ini(3));
y4 = L3*sin(cond_ini(3));
x5 = x3 + 3*L3*cos(cond_ini(3));
y5 = y3 + 3*L3*sin(cond_ini(3));
figure 
hold on
a = plot([0 x1], [0 y1], 'b');
b = plot([x1 x2], [y1 y2], 'r'); 
c = plot([x3 x4], [y3 y4]);
d = plot([x3 x5], [y3 y5], 'g');
axis ([-2.5,2.5,-3,0])

%Animation
for i=1:size(theta1)
    x1= L1*cos(theta1(i));
    y1 = L1*sin(theta1(i));
    x2 =  L1*cos(theta1(i)) + L2*cos(theta1(i)+theta2(i));
    y2 = L1*sin(theta1(i)) + L2*sin(theta1(i) + theta2(i));
    x3 = L0;
    y3 =0;
    x4 = L0 + L3*cos(theta3(i));
    y4 = L3*sin(theta3(i));
    x5 = x3 + 3*L3*cos(theta3(i));
    y5 = y3 + 3*L3*sin(theta3(i));
    set(a, 'XData',[0 x1], 'YData', [0 y1]);
    set(b, 'XData',[x1 x2], 'YData', [y1 y2]); 
    set(c, 'XData',[x3 x4], 'YData', [y3 y4]);
    set(d, 'XData',[x3 x5], 'YData', [y3 y5]);
    drawnow;
end 
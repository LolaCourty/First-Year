%%% Paramètres 
b = 31.62; %longueur entre l'épaule et le coude
a = 43.18; %longueur entre le coude et le poignet
cond_ini = [10; 10; 10; 30]; %trois angles pour l'épaule, un pour le coude
theta_x_min = -60;
theta_x_max = 170;
theta_y_min = 0;
theta_y_max = 170;
theta_z_min = -90;
theta_z_max = 140;
phi_min = 0;
phi_max = 150;
pas = 20;

X = [];
Y = [];
Z = [];
for theta_x=theta_x_min:pas:theta_x_max
    for theta_y=theta_y_min:pas:theta_y_max
        for theta_z=theta_z_min:pas:theta_z_max
            for phi = phi_min:pas:phi_max
                x_ec = -b*sin(theta_y);
                y_ec =  b*sin(theta_x)*cos(theta_y);
                z_ec = -b*cos(theta_x)*cos(theta_y);
                x_cm = -a*cos(phi)*sin(theta_y)-a*sin(phi)*cos(theta_y)*sin(theta_z);
                y_cm = a*cos(phi)*sin(theta_x)*cos(theta_y)+a*sin(phi)*cos(theta_x)*cos(theta_z)-a*sin(phi)*sin(theta_x)*sin(theta_y)*sin(theta_z);
                z_cm = -a*cos(phi)*cos(theta_x)*cos(theta_y)+a*sin(phi)*sin(theta_x)*cos(theta_z)+a*sin(phi)*cos(theta_x)*sin(theta_y)*sin(theta_z);
                X = [X x_ec+x_cm];
                Y = [Y y_ec+y_cm];
                Z = [Z z_ec+z_cm];
            end
        end
    end 
end 
plot3(X, Y, Z, 'o')
xlabel('X')
ylabel('Y')
zlabel('Z')



                
                
                

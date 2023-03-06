temps = out.simout.time;
x = out.simout.signals.values;
ax1 = nexttile;
x = squeeze(x);
y = out.simout1.signals.values;
y = squeeze(y);
plot(x, y, 'b');
xlabel('x');
ylabel('y');
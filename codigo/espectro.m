load wavelenght.dat
load transmitancia.dat
format long

x=wavelenght;
y=transmitancia;

figure(1);
plot(x,y);
xlabel('Longitud de Onda \lambda (nm)'), ylabel('Transmitancia T');
title('Espectro de transmitancia película delgada');
grid on;
hold on;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[MaximosLocales,LongitudDeOnda] = findpeaks(y,x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
z=-y;
[MinimosLocales,LongitudDeOnda] = findpeaks(z,x)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[up,low]=envelope(y,10,'peak');
hold on;
plot(x,up,x,low) %'linewidth',1.5)
axis ([300 1100 0 1])
legend('T','T_M','T_m')
hold on;
xline(1055);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
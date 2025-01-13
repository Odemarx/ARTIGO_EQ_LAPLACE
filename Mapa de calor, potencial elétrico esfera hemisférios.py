#!/usr/bin/env python
# coding: utf-8

#MAPA CALOR POTENCIAL ELÉTRICO NO PLANO ZY LINHAS EQUIPOTENCIAIS--------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Definir constantes
V = 1
a = 1
N = 6  # Número de termos da série

# Definir a função potencial
def potential(r, theta):
    result = 0
    for l in range(0, N, 2):
        P = legendre(l + 1)
        coef = (-1)**(l//2) * np.math.factorial(l) / (2**l * np.math.factorial(l//2)**2 * a**(l + 1))
        term = ((2*l + 1) * r**l / (2**l * a**l)) * P(np.cos(theta))
        result += coef * term
    return V * result

# Grid de pontos no plano zy
r = np.linspace(0.01, a, 100)
theta = np.linspace(0, np.pi, 100)
R, Theta = np.meshgrid(r, theta)

# Calcular potencial
Phi_values = np.vectorize(potential)(R, Theta)

# Convertendo coordenadas esféricas para coordenadas cartesianas no plano zy
Z = R * np.cos(Theta)
Y = R * np.sin(Theta)

# Plotar o mapa de calor no plano zy
plt.figure(figsize=(10, 8))
contour_filled = plt.contourf(Y, Z, Phi_values, cmap='viridis', levels=100)
plt.colorbar(contour_filled, label='Potencial Φ(r, θ)')

# Adicionar linhas de superfícies equipotenciais destacadas
contour_lines = plt.contour(Y, Z, Phi_values, colors='white', linewidths=1.5)
plt.clabel(contour_lines, inline=True, fontsize=10, fmt='%.2f')

# Adicionar o disco isolante
plt.axhline(y=0, color='red', linestyle='--', linewidth=2, label='Disco Isolante')

plt.xlabel('y')
plt.ylabel('z')
plt.title('Mapa de Calor do Potencial no Plano zy com Linhas Equipotenciais Destacadas')
plt.legend()
plt.grid(True)
plt.show()


#MAPA CALOR POTENCIAL ELÉTRICO NO PLANO ZX---------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Definir constantes
V = 1
a = 1
N = 6  # Número de termos da série

# Definir a função potencial
def potential(r, theta):
    result = 0
    for l in range(0, N, 2):
        P = legendre(l + 1)
        coef = (-1)**(l//2) * np.math.factorial(l) / (2**l * np.math.factorial(l//2)**2 * a**(l + 1))
        term = ((2*l + 1) * r**l / (2**l * a**l)) * P(np.cos(theta))
        result += coef * term
    return V * result

# Grid de pontos no plano zx
r = np.linspace(0.01, a, 100)
theta = np.linspace(0, np.pi, 100)
R, Theta = np.meshgrid(r, theta)

# Calcular potencial
Phi_values = np.vectorize(potential)(R, Theta)

# Convertendo coordenadas esféricas para coordenadas cartesianas no plano zx
Z = R * np.cos(Theta)
X = R * np.sin(Theta) * np.cos(0)  # 'x' no plano zx é 0, então simplificamos para a mesma coordenada 'X'

# Plotar o mapa de calor no plano zx
plt.figure(figsize=(10, 8))
plt.contourf(X, Z, Phi_values, cmap='viridis', levels=100)
plt.colorbar(label='Potencial Φ(r, θ)')
plt.xlabel('x')
plt.ylabel('z')
plt.title('Mapa de Calor do Potencial no Plano zx')
plt.grid(True)
plt.show()


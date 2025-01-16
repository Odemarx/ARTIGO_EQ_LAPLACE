#!/usr/bin/env python
# coding: utf-8

# MAPA DE CALOR DO POTENCIAL ELÉTRICO NO PLANO ZY E ZX COM LINHAS EQUIPOTENCIAIS
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Definir constantes
V = 1
a = 1
N = 6  # Número de termos da série

# Definir a função potencial
def potential(r, theta, N, a, V):
    result = 0
    for l in range(0, N, 2):
        P = legendre(l + 1)
        coef = (-1)**(l//2) * np.math.factorial(l) / (2**l * np.math.factorial(l//2)**2 * a**(l + 1))
        term = ((2*l + 1) * r**l / (2**l * a**l)) * P(np.cos(theta))
        result += coef * term
    return V * result

# Função para plotar o mapa de calor
def plot_heatmap(plane, r_range, theta_range, N, a, V):
    r = np.linspace(*r_range, 100)
    theta = np.linspace(*theta_range, 100)
    R, Theta = np.meshgrid(r, theta)
    
    # Calcular o potencial
    Phi_values = np.vectorize(lambda r, theta: potential(r, theta, N, a, V))(R, Theta)
    
    # Coordenadas esféricas para cartesianas
    Z = R * np.cos(Theta)
    if plane == "ZY":
        X = R * np.sin(Theta)
        xlabel, ylabel = "y", "z"
    elif plane == "ZX":
        X = R * np.sin(Theta) * np.cos(0)
        xlabel, ylabel = "x", "z"
    else:
        raise ValueError("Plano inválido. Escolha entre 'ZY' ou 'ZX'.")
    
    # Plotar
    plt.figure(figsize=(10, 8))
    contour_filled = plt.contourf(X, Z, Phi_values, cmap='viridis', levels=100)
    plt.colorbar(contour_filled, label='Potencial Φ(r, θ)')
    
    # Linhas equipotenciais
    contour_lines = plt.contour(X, Z, Phi_values, colors='white', linewidths=1.5)
    plt.clabel(contour_lines, inline=True, fontsize=10, fmt='%.2f')
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f'Mapa de Calor do Potencial no Plano {plane}')
    plt.grid(True)
    plt.show()

# Plotar mapas nos planos ZY e ZX
plot_heatmap("ZY", (0.01, a), (0, np.pi), N, a, V)
plot_heatmap("ZX", (0.01, a), (0, np.pi), N, a, V)

#!/usr/bin/env python
# coding: utf-8

# In[43]:


#CAMPO ELÉTRICO INTERNO AO CILINDRO 3D-----------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, art3d
import scipy.special as sp

# Define a função vetorial
def cyl_vector_field(rho, phi, z):
    R = 2  # Define valor 2 para o raio do cilindro
    h = 6  # Define valor 1 para a altura do cilindro
    U_0 = 1  # Define valor 1 para o potencial
    lmax = 10  # Valor máximo de l (número de termos do somatório)

    Erho = 0  # Componente do campo na direção radial

    # Cria um laço de soma para definir a função vetorial campo elétrico
    for l in range(1, lmax + 1):
        k = ((2 * l + 1) * np.pi / h)
        jv_0 = sp.jv(0, k)  # Função de Bessel de ordem zero e argumento k

        # Derivada de ordem "1" da função de Bessel de ordem zero
        jvp_0_n = sp.jvp(0, k, 1)

        # Forma explícita da componente radial do campo elétrico
        Erho += 4 * U_0 / ((2 * l + 1) * np.pi * sp.jv(0, k * R)) * sp.jvp(0, k * rho, 1) *                 np.sin((2 * l + 1) * np.pi / h * z)

    Ephi = 0  # Componente do campo na direção azimutal

    Ez = 0  # Componente do campo na direção z
    for l in range(1, lmax + 1):
        k = ((2 * l + 1) * np.pi / h)
        jv_0 = sp.jv(0, k)  # Função de Bessel de ordem zero

        # Forma explícita da componente em z do campo elétrico
        Ez += 4 * U_0 / (h * sp.jv(0, k * R)) * sp.jv(0, k * rho) * np.cos((2 * l + 1) * np.pi / h * z)

    # A função definida retorna os valores para cada componente do campo
    return -Erho, -Ephi, -Ez

# Define a grade espacial em coordenadas cilíndricas de acordo com os intervalos desejados
Rho, Phi, Z = np.meshgrid(np.linspace(0, 2, 8),
                          np.linspace(0, 2 * np.pi, 3),
                          np.linspace(0, 6, 8))

# Converte as coordenadas cilíndricas para cartesianas
X = Rho * np.cos(Phi)
Y = Rho * np.sin(Phi)

# Avalia a função vetorial definida em cada ponto do espaço
Erho, Ephi, Ez = cyl_vector_field(Rho, Phi, Z)

# Define a variável vazia para a plotagem da Figura
fig = plt.figure()

# Cria a Figura a ser plotada e o sistema de referência em 3D
ax = fig.add_subplot(111, projection='3d')

# Plotagem das flechas de campo em função das coordenadas cartesianas
ax.quiver(X, Y, Z, Erho, Ephi, Ez, length=0.5, color="red", normalize=True, arrow_length_ratio=0.6)

# Adiciona a superfície cilíndrica fechada
R = 2
h = 6
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, h, 50)

# Coordenadas para a lateral do cilindro
U, V = np.meshgrid(u, v)
x_cylinder = R * np.cos(U)
y_cylinder = R * np.sin(U)
z_cylinder = V

# Coordenadas para as tampas do cilindro
theta = np.linspace(0, 2 * np.pi, 50)
x_top = R * np.cos(theta)
y_top = R * np.sin(theta)
z_top = np.ones_like(theta) * h

x_bottom = R * np.cos(theta)
y_bottom = R * np.sin(theta)
z_bottom = np.zeros_like(theta)

# Plotagem da superfície cilíndrica e das tampas
ax.plot_surface(x_cylinder, y_cylinder, z_cylinder, color='cornflowerblue', alpha=0.2)
ax.plot(x_top, y_top, z_top, color='cornflowerblue')
ax.plot(x_bottom, y_bottom, z_bottom, color='cornflowerblue')
ax.view_init(elev=30, azim=-60)
ax.set_xlabel('X')  # Insere a legenda da direção x
ax.set_ylabel('Y')  # Insere a legenda da direção y
ax.set_zlabel('Z')  # Insere a legenda da direção z

ax.set_zlim(0, 7)  # Define os limites da direção z

plt.show()


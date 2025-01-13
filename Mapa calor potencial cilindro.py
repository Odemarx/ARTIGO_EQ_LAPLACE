#!/usr/bin/env python
# coding: utf-8

#MAPA DE CALOR DO POTENCIAL ELÉTRICO NO PLANO ZX------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn

# Parâmetros do cilindro
h = 5.0  # Altura do cilindro
R = 1.0  # Raio do cilindro
U_0 = 1.0  # Potencial constante
L = 20  # Número de termos na soma

# Função para calcular o potencial elétrico
def potencial(rho, z, h, R, U_0, L):
    potencial_total = 0
    for l in range(L):
        k = (2*l + 1) * np.pi / h
        J0_rho = jn(0, k * rho)
        sin_z = np.sin(k * z)
        J0_R = jn(0, (2*l + 1) * np.pi / h * R)
        coef = 4 * U_0 / ((2*l + 1) * np.pi * J0_R)
        potencial_total += coef * J0_rho * sin_z
    return potencial_total

# Criação das coordenadas
rho = np.linspace(-R, R, 100)  # Coordenada radial
z = np.linspace(0, h, 100)    # Coordenada vertical
Rho, Z = np.meshgrid(rho, z)  # Criação da grade

# Cálculo do potencial
Phi = potencial(Rho, Z, h, R, U_0, L)

# Plotagem
plt.figure(figsize=(8, 6))
plt.contourf(Rho, Z, Phi, cmap='inferno', levels=100)
plt.colorbar(label='Potencial elétrico Phi(rho, z)')
plt.xlabel('rho')
plt.ylabel('z')
plt.title('Mapa de Calor do Potencial Elétrico no Plano zx')
plt.show()


#MAPA DE CALOR DO POTENCIAL ELÉTRICO NO PLANO XY---------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn

# Parâmetros do cilindro
h = 5.0  # Altura do cilindro
R = 1.0  # Raio do cilindro
U_0 = 1.0  # Potencial constante
L = 20  # Número de termos na soma

# Função para calcular o potencial elétrico
def potencial(rho, z, h, R, U_0, L):
    potencial_total = 0
    for l in range(L):
        k = (2*l + 1) * np.pi / h
        J0_rho = jn(0, k * rho)
        sin_z = np.sin(k * z)
        J0_R = jn(0, (2*l + 1) * np.pi / h * R)
        coef = 4 * U_0 / ((2*l + 1) * np.pi * J0_R)
        potencial_total += coef * J0_rho * sin_z
    return potencial_total

# Criação das coordenadas cartesianas
x = np.linspace(-R, R, 100)
y = np.linspace(-R, R, 100)
X, Y = np.meshgrid(x, y)

# Transformação para coordenadas cilíndricas
rho = np.sqrt(X**2 + Y**2)
z = h / 2  # Considerando o meio do cilindro para visualizar a superfície lateral

# Calcula o potencial
Phi = potencial(rho, z, h, R, U_0, L)

# Máscara para a região interna do cilindro
mask = rho <= R

# Aplicar a máscara ao potencial
Phi_masked = np.where(mask, Phi, np.nan)

# Plotagem
plt.figure(figsize=(10, 8))
contourf = plt.contourf(X, Y, Phi_masked, cmap='inferno', levels=100, alpha=0.7)
plt.colorbar(label='Potencial elétrico Phi(rho, z)')

# Adicionando a circunferência do cilindro
circle = plt.Circle((0, 0), R, color='black', fill=False, linestyle='-', linewidth=3)
plt.gca().add_patch(circle)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradiente de Cores do Potencial Elétrico no Plano xy com Circunferência do Cilindro')

# Configurar limites e mostrar o gráfico
plt.xlim(-R-0.2, R+0.2)
plt.ylim(-R-0.2, R+0.2)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()


#MAPA DE CALOR DO POTENCIAL ELÉTRICO NO PLANO ZY----------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn

# Parâmetros do cilindro
h = 5.0  # Altura do cilindro
R = 1.0  # Raio do cilindro
U_0 = 1.0  # Potencial constante
L = 20  # Número de termos na soma

# Função para calcular o potencial elétrico
def potencial(rho, z, h, R, U_0, L):
    potencial_total = 0
    for l in range(L):
        k = (2*l + 1) * np.pi / h
        J0_rho = jn(0, k * rho)
        sin_z = np.sin(k * z)
        J0_R = jn(0, (2*l + 1) * np.pi / h * R)
        coef = 4 * U_0 / ((2*l + 1) * np.pi * J0_R)
        potencial_total += coef * J0_rho * sin_z
    return potencial_total

# Criação das coordenadas
z = np.linspace(0, h, 100)    # Coordenada vertical
rho = np.linspace(-R, R, 100)  # Coordenada radial
Rho, Z = np.meshgrid(rho, z)  # Criação da grade

# Cálculo do potencial
Phi = potencial(Rho, Z, h, R, U_0, L)

# Plotagem
plt.figure(figsize=(8, 6))
plt.contourf(Rho, Z, Phi, cmap='inferno', levels=100)
plt.colorbar(label='Potencial elétrico Phi(rho, z)')
plt.xlabel('rho')
plt.ylabel('z')
plt.title('Mapa de Calor do Potencial Elétrico no Plano zy')
plt.show()


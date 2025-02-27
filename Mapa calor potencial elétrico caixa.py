#!/usr/bin/env python
# coding: utf-8

#MAPA DE CALOR POTENCIAL NO PLANO ZX----------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Definir constantes
U = 1
U_prime = 1
a = 1
b = 1
c = 1
N = 10  # Número de termos na soma

# Definir a função potencial
def potential(x, y, z):
    result = 0
    for n in range(1, N + 1):
        for m in range(1, N + 1):
            k = np.sqrt((n * np.pi / a)**2 + (m * np.pi / b)**2)
            term1 = (16 * U_prime * np.cosh(k * z)) / ((2 * n - 1) * (2 * m - 1) * np.pi**2)
            term2 = (16 * (U - U_prime * np.cosh(k * c)) * np.sinh(k * z)) / ((2 * n - 1) * (2 * m - 1) * np.pi**2 * np.sinh(k * c))
            result += np.sin(n * np.pi * x / a) * np.sin(m * np.pi * y / b) * (term1 + term2)
    return result

# Grid de pontos dentro do paralelepípedo
x = np.linspace(0, a, 50)
z = np.linspace(0, c, 50)
X, Z = np.meshgrid(x, z)
Y = b / 2  # Fixar y em b/2

# Calcular o potencial
Phi_values = np.vectorize(potential)(X, Y, Z)

# Plotar o mapa de calor no plano zx
plt.figure(figsize=(8, 6))
plt.contourf(X, Z, Phi_values, cmap='plasma', levels=100)
plt.colorbar(label='Potencial Φ(x, z)')
plt.xlabel('x')
plt.ylabel('z')
plt.title('Mapa de Calor do Potencial no Plano zx (y = b / 2)')
plt.grid(True)
plt.show()


#MAPA DE CALOR POTENCIAL NO PLANO ZY---------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Definir constantes
U = 1
U_prime = 1
a = 1
b = 1
c = 1
N = 10  # Número de termos na soma

# Definir a função potencial
def potential(x, y, z):
    result = 0
    for n in range(1, N + 1):
        for m in range(1, N + 1):
            k = np.sqrt((n * np.pi / a)**2 + (m * np.pi / b)**2)
            term1 = (16 * U_prime * np.cosh(k * z)) / ((2 * n - 1) * (2 * m - 1) * np.pi**2)
            term2 = (16 * (U - U_prime * np.cosh(k * c)) * np.sinh(k * z)) / ((2 * n - 1) * (2 * m - 1) * np.pi**2 * np.sinh(k * c))
            result += np.sin(n * np.pi * x / a) * np.sin(m * np.pi * y / b) * (term1 + term2)
    return result

# Grid de pontos dentro do paralelepípedo
y = np.linspace(0, b, 50)
z = np.linspace(0, c, 50)
Y, Z = np.meshgrid(y, z)
X = a / 2  # Fixar x em a/2

# Calcular o potencial
Phi_values = np.vectorize(potential)(X, Y, Z)

# Plotar o mapa de calor no plano zy
plt.figure(figsize=(8, 6))
plt.contourf(Y, Z, Phi_values, cmap='plasma', levels=100)
plt.colorbar(label='Potencial Φ(y, z)')
plt.xlabel('y')
plt.ylabel('z')
plt.title('Mapa de Calor do Potencial no Plano zy (x = a / 2)')
plt.grid(True)
plt.show()

#MAPA DE CALOR POTENCIAL NO PLANO XY------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Definir constantes
U = 1
U_prime = 1
a = 1
b = 1
c = 1
N = 10  # Número de termos na soma

# Definir a função potencial
def potential(x, y, z):
    result = 0
    for n in range(1, N + 1):
        for m in range(1, N + 1):
            k = np.sqrt((n * np.pi / a)**2 + (m * np.pi / b)**2)
            term1 = (16 * U_prime * np.cosh(k * z)) / ((2 * n - 1) * (2 * m - 1) * np.pi**2)
            term2 = (16 * (U - U_prime * np.cosh(k * c)) * np.sinh(k * z)) / ((2 * n - 1) * (2 * m - 1) * np.pi**2 * np.sinh(k * c))
            result += np.sin(n * np.pi * x / a) * np.sin(m * np.pi * y / b) * (term1 + term2)
    return result

# Grid de pontos dentro do paralelepípedo
x = np.linspace(0, a, 50)
y = np.linspace(0, b, 50)
X, Y = np.meshgrid(x, y)
Z = c / 2  # Fixar z em c/2

# Calcular o potencial
Phi_values = np.vectorize(potential)(X, Y, Z)

# Plotar o mapa de calor no plano xy
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Phi_values, cmap='plasma', levels=100)
plt.colorbar(label='Potencial Φ(x, y)')

# Adicionar as linhas de equipotenciais
contour_lines = plt.contour(X, Y, Phi_values, colors='cyan', linewidths=2, levels=np.linspace(np.min(Phi_values), np.max(Phi_values), 10))

# Adicionar rótulos às linhas de equipotenciais
plt.clabel(contour_lines, inline=True, fontsize=10, fmt='%.2f', colors='cyan')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Mapa de Calor do Potencial no Plano xy (z = c / 2)')
plt.grid(True)
plt.show()


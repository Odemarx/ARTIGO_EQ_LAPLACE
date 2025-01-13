#!/usr/bin/env python
# coding: utf-8

# In[3]:


#CAMPO ELÉTRICO INTERNO A CAIXA NO PLANO XY---------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Definições dos parâmetros
U = 1
U_prime = 1
a = 1
b = 1
c = 1
z = c / 2

# Função k_{nm}
def k_nm(n, m):
    return np.sqrt((n * np.pi / a) ** 2 + (m * np.pi / b) ** 2)

# Intervalos e malha
x = np.linspace(0, a, 50)
y = np.linspace(0, b, 20)
X, Y = np.meshgrid(x, y)

# Inicialização dos campos vetoriais
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)
Ez = np.zeros_like(X)

# Cálculo dos componentes do campo vetorial
for n in range(1, 6):  # Limitar a soma para fins de visualização
    for m in range(1, 6):
        k = k_nm(n, m)
        cosh_kz = np.cosh(k * z)
        sinh_kz = np.sinh(k * z)
        sinh_c = np.sinh(k * c)
        
        term1 = 16 * U_prime * cosh_kz / ((2 * n - 1) * (2 * m - 1) * np.pi ** 2)
        term2 = 16 * (U - U_prime * cosh_kz * np.sinh(k * z)) / ((2 * n - 1) * (2 * m - 1) * np.pi ** 2 * sinh_c)
        term3 = 16 * U_prime * k * sinh_kz / ((2 * n - 1) * (2 * m - 1) * np.pi ** 2)
        term4 = 16 * (U - U_prime * k * np.cosh(k * c) * np.cosh(k * z)) / ((2 * n - 1) * (2 * m - 1) * np.pi ** 2 * sinh_c)

        Ex += (n * np.pi / a) * np.cos(n * np.pi * X / a) * np.sin(m * np.pi * Y / b) * (term1 + term2)
        Ey -= (m * np.pi / b) * np.sin(n * np.pi * X / a) * np.cos(m * np.pi * Y / b) * (term1 + term2)
        Ez -= np.sin(n * np.pi * X / a) * np.sin(m * np.pi * Y / b) * (term3 + term4)

# Cálculo da magnitude
magnitude = np.sqrt(Ex**2 + Ey**2)

# Normalização dos vetores
Ex_normalized = Ex / (magnitude + 1e-10)  # Adiciona um pequeno valor para evitar divisão por zero
Ey_normalized = Ey / (magnitude + 1e-10)

# Gradiente de intensidade
intensity = magnitude

# Plotagem do campo vetorial normalizado com gradiente de intensidade
plt.figure(figsize=(10, 8))
plt.quiver(X, Y, Ex_normalized, Ey_normalized, intensity, scale=25, cmap='plasma', pivot='middle')
plt.colorbar(label='Magnitude Normalizada')
plt.title('Campo Vetorial Normalizado no Plano XY com $z = c/2$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


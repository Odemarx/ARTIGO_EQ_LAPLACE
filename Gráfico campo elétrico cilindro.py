#!/usr/bin/env python
# coding: utf-8

# In[67]:


#CAMPO ELÉTRICO INTERNO AO CILINDRO PLANO Z\RHO--------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, jvp

# Parâmetros
U0 = 1
R = 1
h = 5
lmax = 20

# Criar malha
rho = np.linspace(-R, R, 40)
z = np.linspace(0, h, 40)
Rho, Z = np.meshgrid(rho, z)

# Função para calcular o campo elétrico
def campo_eletrico(Rho, Z, lmax):
    E_rho = np.zeros_like(Rho)
    E_z = np.zeros_like(Rho)
    for l in range(lmax):
        factor = 4 * U0 / ((2*l+1) * np.pi * jv(0, (2*l+1)*np.pi*R/h))
        E_rho += -factor * jvp(0, (2*l+1)*np.pi*Rho/h) * np.sin((2*l+1)*np.pi*Z/h)
        E_z += -factor * jv(0, (2*l+1)*np.pi*Rho/h) * np.cos((2*l+1)*np.pi*Z/h) / h
    return E_rho, E_z

# Calcular o campo elétrico
E_rho, E_z = campo_eletrico(Rho, Z, lmax)

# Normalizar os vetores
E_norm = np.sqrt(E_rho**2 + E_z**2)
E_rho_norm = E_rho / E_norm
E_z_norm = E_z / E_norm

# Visualizar o campo com escala, título e gradiente de cor
plt.quiver(Rho, Z, E_rho_norm, E_z_norm, E_norm, cmap='jet', scale=40)
plt.colorbar(label='Intensidade do campo elétrico E(z,ρ)')
plt.xlabel('ρ')
plt.ylabel('z')
plt.title('Campo Elétrico interno ao cilindro no plano zρ')
plt.show()


# In[66]:


#CAMPO ELÉTRICO INTERIOR AO CILINDRO NO PLANO XY--------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import j0, j1

# Definindo os parâmetros
U0 = 1  # Ajuste conforme necessário
R = 1
h = 5  # Altura do cilindro (ajuste conforme necessário)
max_l = 10  # Número máximo de termos na soma
z = h/2  # Plano z para o plot

# Criando a malha
rho = np.linspace(-R, R, 40)  
phi = np.linspace(0, 2*np.pi, 40)
Rho, Phi = np.meshgrid(rho, phi)

# Calculando o campo elétrico
def E_rho(rho, z, l):
    return -4*U0/(2*l+1)/np.pi/j0((2*l+1)*np.pi/h*R)*j1((2*l+1)*np.pi/h*rho)*np.sin((2*l+1)*np.pi/h*z)

def E_z(rho, z, l):
    return -4*U0/h/j0((2*l+1)*np.pi/h*R)*j0((2*l+1)*np.pi/h*rho)*np.cos((2*l+1)*np.pi/h*z)

# Calculando as componentes do campo para o plano z especificado
Ex, Ey = 0, 0
for l in range(max_l):
    Ex += E_rho(Rho, z, l) * np.cos(Phi)
    Ey += E_rho(Rho, z, l) * np.sin(Phi)

# Calculando a magnitude do campo elétrico
E_magnitude = np.sqrt(Ex**2 + Ey**2)

# Normalizando os vetores
Ex_norm = Ex / E_magnitude
Ey_norm = Ey / E_magnitude

# Plotando o campo vetorial com gradiente de cores
plt.figure(figsize=(8, 6))
plt.quiver(Rho*np.cos(Phi), Rho*np.sin(Phi), Ex_norm, Ey_norm, E_magnitude, 
          cmap='jet', scale=45, pivot='mid')  # Ajustar scale conforme necessário
plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo Elétrico interior ao cilindro no plano XY')
plt.colorbar(label='Intensidade do campo elétrico E(z=h/2,ρ)')
plt.grid(True)
plt.xlim(-R, R)  # Ajustar os limites dos eixos
plt.ylim(-R, R)
plt.show()


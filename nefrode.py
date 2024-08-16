import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, cos, sin, pi
from sympy import plot_parametric

t = symbols('t')

def x_nephroid(t):
    return 1/2 * (3*cos(t) - cos(3*t))

def y_nephroid(t):
    return 1/2 * (3*sin(t) - sin(3*t))

def x_involute(t):
    return 4 * cos(t)**3

def y_involute(t):
    return 3*sin(t) + sin(3*t)

def x_cayley(t):
    return 4 * cos(t)**3 * (1 - 3/2 * sin(t)**2)

def y_cayley(t):
    return 4 * sin(t)**3 * (1 - 3/2 * cos(t)**2)

# Crear una figura con 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 7))

# Graficar la nefroide original y su involuta
p1 = plot_parametric(x_nephroid(t), y_nephroid(t), (t, 0, 2*pi), line_color='blue', show=False, label='Nefroide')
p1._backend.ax = ax1
p1._backend.process_series()

p2 = plot_parametric(x_involute(t), y_involute(t), (t, 0, 2*pi), line_color='red', show=False, label='Involuta (Nefroide)')
p2._backend.ax = ax1
p2._backend.process_series()

ax1.set_title('Nefroide y su Involuta')
ax1.legend()
ax1.set_aspect('equal')

# Graficar la nefroide y su involuta en un rango más amplio
p3 = plot_parametric(x_nephroid(t), y_nephroid(t), (t, 0, 4*pi), line_color='blue', show=False, label='Nefroide')
p3._backend.ax = ax2
p3._backend.process_series()

p4 = plot_parametric(x_involute(t), y_involute(t), (t, 0, 4*pi), line_color='red', show=False, label='Involuta (Nefroide)')
p4._backend.ax = ax2
p4._backend.process_series()

ax2.set_title('Nefroide y su Involuta (Rango Amplio)')
ax2.legend()
ax2.set_aspect('equal')

# Graficar la séxtica de Cayley
p5 = plot_parametric(x_cayley(t), y_cayley(t), (t, 0, 2*pi), line_color='green', show=False, label='Séxtica de Cayley')
p5._backend.ax = ax3
p5._backend.process_series()

ax3.set_title('Séxtica de Cayley')
ax3.legend()
ax3.set_aspect('equal')

plt.tight_layout()
plt.show()
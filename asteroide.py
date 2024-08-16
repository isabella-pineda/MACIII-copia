import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, cos, sin, pi
from sympy import plot_parametric

t = symbols('t')

def x(t):
    return cos(t)**3

def y(t):
    return sin(t)**3

def xi(t):
    return 1/8 * (3*cos(t) - cos(3*t))

def yi(t):
    return 1/8 * (3*sin(t) + sin(3*t))

# Crear una figura con 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Graficar el asteroide original
p1 = plot_parametric(x(t), y(t), (t, 0, 2*pi), line_color='blue', show=False, label='Asteroide')
p1._backend.ax = ax1
p1._backend.process_series()

# Graficar la involuta del asteroide
p2 = plot_parametric(xi(t), yi(t), (t, 0, 2*pi), line_color='red', show=False, label='Involuta')
p2._backend.ax = ax1
p2._backend.process_series()

ax1.set_title('Asteroide y su Involuta')
ax1.legend()
ax1.set_aspect('equal')

# Graficar el asteroide y su involuta en un rango más amplio
p3 = plot_parametric(x(t), y(t), (t, 0, 4*pi), line_color='blue', show=False, label='Asteroide')
p3._backend.ax = ax2
p3._backend.process_series()

p4 = plot_parametric(xi(t), yi(t), (t, 0, 4*pi), line_color='red', show=False, label='Involuta')
p4._backend.ax = ax2
p4._backend.process_series()

ax2.set_title('Asteroide y su Involuta (Rango Amplio)')
ax2.legend()
ax2.set_aspect('equal')

plt.tight_layout()
plt.show()
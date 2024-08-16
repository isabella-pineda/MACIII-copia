import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, plot_parametric

t = symbols('t')
a = 1  # Puedes cambiar este valor si lo deseas

def x_parabola(t):
    return t**2

def y_parabola(t):
    return a * t**3

def x_involute(t):
    return (t**2)/3 - 8/(27*a**2)

def y_involute(t):
    return -(4*t)/(9*a)

# Crear una figura con 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Graficar la parábola semicúbica y su involuta
p1 = plot_parametric(x_parabola(t), y_parabola(t), (t, -2, 2), line_color='blue', show=False, label='Parábola Semicúbica')
p1._backend.ax = ax1
p1._backend.process_series()

p2 = plot_parametric(x_involute(t), y_involute(t), (t, -2, 2), line_color='red', show=False, label='Involuta')
p2._backend.ax = ax1
p2._backend.process_series()

ax1.set_title('Parábola Semicúbica y su Involuta')
ax1.legend()
ax1.set_aspect('equal')

# Graficar en un rango más amplio
p3 = plot_parametric(x_parabola(t), y_parabola(t), (t, -4, 4), line_color='blue', show=False, label='Parábola Semicúbica')
p3._backend.ax = ax2
p3._backend.process_series()

p4 = plot_parametric(x_involute(t), y_involute(t), (t, -4, 4), line_color='red', show=False, label='Involuta')
p4._backend.ax = ax2
p4._backend.process_series()

ax2.set_title('Parábola Semicúbica y su Involuta (Rango Amplio)')
ax2.legend()
ax2.set_aspect('equal')

plt.tight_layout()
plt.show()
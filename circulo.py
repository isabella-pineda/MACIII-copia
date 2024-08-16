#Circulo

from sympy import symbols, cos, sin, pi
from sympy import plot_parametric

t = symbols('t')
a = 1  # Radio del círculo. Puedes cambiar este valor si lo deseas.

def x(t):
    return a * cos(t)

def y(t):
    return a * sin(t)

def xi(t):
    return a * (cos(t) + t*sin(t))

def yi(t):
    return a * (sin(t) - t*cos(t))

# Graficar el círculo original
p1 = plot_parametric(x(t), y(t), (t, 0, 2*pi), line_color='blue', show=False, label='Círculo')

# Graficar la involuta del círculo
p2 = plot_parametric(xi(t), yi(t), (t, 0, 4*pi), line_color='red', show=False, label='Involuta')

# Combinar los gráficos
p1.extend(p2)

# Mostrar el gráfico combinado
p1.show()

# Graficar en un rango más amplio
p3 = plot_parametric(x(t), y(t), (t, 0, 6*pi), line_color='blue', show=False, label='Círculo')
p4 = plot_parametric(xi(t), yi(t), (t, 0, 6*pi), line_color='red', show=False, label='Involuta')

p3.extend(p4)
p3.show()
#Cicloide 

from sympy import symbols, cos, sin, exp, pi
from sympy import plot_parametric

t = symbols('t')

def x(t):
    return t - sin(t)

def y(t):
    return 1 - cos(t)

def xi(t):
    return t + sin(t)

def yi(t):
    return 3 + cos(t)

# Graficar la cicloide original
p1 = plot_parametric(x(t), y(t), (t, -6*pi, 6*pi), line_color='blue', show=False, label='Cicloide')

# Graficar la involuta de la cicloide
p2 = plot_parametric(xi(t), yi(t), (t, -6*pi, 6*pi), line_color='red', show=False, label='Involuta')

# Combinar los gráficos
p1.extend(p2)

# Mostrar el gráfico combinado
p1.show()

# Graficar en un rango más amplio
p3 = plot_parametric(x(t), y(t), (t, -50, 50), line_color='blue', show=False, label='Cicloide')
p4 = plot_parametric(xi(t), yi(t), (t, -50, 50), line_color='red', show=False, label='Involuta')

p3.extend(p4)
p3.show()

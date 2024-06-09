import numpy as np
import matplotlib.pyplot as plt

# Berechnung der Lagrange-Basis-Polynome
def lagrange_basis(x, xi, i):
    n = len(xi) - 1
    basis = 1
    for j in range(n + 1):
        if j != i:
            basis *= (x - xi[j]) / (xi[i] - xi[j])
    return basis

# Berechnung der Lebesgue-Funktion
def lebesgue_function(x, xi):
    n = len(xi) - 1
    lebesgue = np.zeros_like(x)
    for i in range(n + 1):
        lebesgue += np.abs(lagrange_basis(x, xi, i))
    return lebesgue

# Stützstellen berechnen
def aquidistante_stutzstellen(n):
    return np.linspace(-1, 1, n + 1)

def tschebyscheff_stutzstellen(n):
    return np.cos((2 * np.arange(n + 1) + 1) * np.pi / (2 * (n + 1)))

# Werte für n
ns = [8, 20]

# Plotten der Lebesgue-Funktion
x = np.linspace(-1, 1, 400)

plt.figure(figsize=(12, 8))
for i, n in enumerate(ns):
    # Äquidistante Stützstellen
    x_aqui = aquidistante_stutzstellen(n)
    lebesgue_aqui = lebesgue_function(x, x_aqui)

    # Tschebyscheff-Stützstellen
    x_tscheb = tschebyscheff_stutzstellen(n)
    lebesgue_tscheb = lebesgue_function(x, x_tscheb)
    
    # Plotten
    plt.subplot(2, 2, 2 * i + 1)
    plt.plot(x, lebesgue_aqui, label=f'Äquidistant, n={n}')
    plt.scatter(x_aqui, np.zeros_like(x_aqui), color='red')
    plt.title(f'Lebesgue-Funktion (Äquidistant, n={n})')
    plt.xlabel('x')
    plt.ylabel('$\Lambda_n(x)$')
    plt.legend()
    
    plt.subplot(2, 2, 2 * i + 2)
    plt.plot(x, lebesgue_tscheb, label=f'Tschebyscheff, n={n}')
    plt.scatter(x_tscheb, np.zeros_like(x_tscheb), color='blue')
    plt.title(f'Lebesgue-Funktion (Tschebyscheff, n={n})')
    plt.xlabel('x')
    plt.ylabel('$\Lambda_n(x)$')
    plt.legend()

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def aitken_neville_schema(x, f, xi):
    n = len(x)
    Q = np.zeros((n, n))
    for i in range(n):
        Q[i, 0] = f[i]
    
    for j in range(1, n):
        for i in range(n - j):
            Q[i, j] = ((xi - x[i + j]) * Q[i, j - 1] + (x[i] - xi) * Q[i + 1, j - 1]) / (x[i] - x[i + j])
    
    return Q[0, n - 1]

def compute_all_aitken_neville_polynomials(x, y):
    n = len(x)
    xi = sp.Symbol('xi')
    P = [[None for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        P[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            P[i][j] = ((xi - x[i + j]) * P[i][j - 1] + (x[i] - xi) * P[i + 1][j - 1]) / (x[i] - x[i + j])
    
    return P

if __name__ == '__main__':
    x = np.array([-1, 0, 2, 3])
    y = np.array([8, -2, 2, 4])

    # Berechnung aller Aitken-Neville-Polynome
    P = compute_all_aitken_neville_polynomials(x, y)
    
    # Darstellung der Polynome
    xi_vals = np.linspace(-1, 3, 1000)
    
    plt.figure()
    for j in range(1, len(x)):
        for i in range(len(x) - j):
            P_ij = sp.lambdify(sp.Symbol('xi'), P[i][j], 'numpy')
            yi_vals = P_ij(xi_vals)
            plt.plot(xi_vals, yi_vals, '--', label=f'P[{i},{j}]')
    
    # Stützpunkte hinzufügen
    plt.plot(x, y, 'o', label='Stützpunkte', color='black')
    
    # Interpoliertes Polynom berechnen und darstellen
    yi = np.array([aitken_neville_schema(x, y, val) for val in xi_vals])
    plt.plot(xi_vals, yi, '-', label='Interpoliertes Polynomial', color='blue')
    
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title('Aitken-Neville Polynomiale und Interpolation')
    plt.grid(True)
    plt.show()

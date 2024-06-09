import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def divided_differences(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])

    return coef[0, :]

def newton_polynomial(coef, x_data):
    xi = sp.Symbol('xi')
    n = len(coef)
    poly = coef[0]
    term = 1
    for i in range(1, n):
        term *= (xi - x_data[i-1])
        poly += coef[i] * term
    return sp.simplify(poly)

def polynomial_diff(p1, p2):
    return sp.simplify(p1 - p2)

def f(x):
    return np.tan(x)

if __name__ == '__main__':
    x = np.array([-1.5, -0.75, 0, 0.75, 1.5])
    y = f(x)

    # Berechnung der dividierten Differenzen
    coef = divided_differences(x, y)
    
    # Symbolische Berechnung der Polynome
    polynomials = [newton_polynomial(coef[:k+1], x[:k+1]) for k in range(len(coef))]
    
    # Berechnung der Differenzen
    differences = [polynomial_diff(polynomials[k], polynomials[k-1]) for k in range(1, len(polynomials))]
    
    # Plotten der Polynome und Differenzen
    xi_vals = np.linspace(-1.5, 1.5, 400)
    plt.figure(figsize=(14, 10))
    
    for k in range(1, len(polynomials)):
        plt.subplot(3, 1, k)
        
        Pk_1_func = sp.lambdify(sp.Symbol('xi'), polynomials[k-1], 'numpy')
        Pk_func = sp.lambdify(sp.Symbol('xi'), polynomials[k], 'numpy')
        deltaPk_func = sp.lambdify(sp.Symbol('xi'), differences[k-1], 'numpy')
        
        Pk_1_vals = Pk_1_func(xi_vals)
        Pk_vals = Pk_func(xi_vals)
        deltaPk_vals = deltaPk_func(xi_vals)
        
        plt.plot(xi_vals, Pk_1_vals, 'b--', label=f'P_{k-1}')
        plt.plot(xi_vals, Pk_vals, 'g-', label=f'P_{k}')
        plt.plot(xi_vals, deltaPk_vals, 'r-.', label=f'ΔP_{k}')
        
        # Nullstellen von ΔP_k markieren
        deltaPk_zeros = sp.solvers.solve(differences[k-1], sp.Symbol('xi'))
        for zero in deltaPk_zeros:
            if zero.is_real:
                plt.axvline(x=float(zero), color='r', linestyle=':', label=f'Nullstelle ΔP_{k}')
        
        plt.plot(x, y, 'ko', label='Stützpunkte')
        plt.xlabel('x')
        plt.ylabel('P(x)')
        plt.title(f'Polynome P_{k-1}, P_{k} und ΔP_{k}')
        plt.legend()
        plt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    # Symbolische Ausgabe des interpolierten Polynoms
    print("Interpolated Polynomial (Newton's divided differences):")
    sp.pprint(polynomials[-1])

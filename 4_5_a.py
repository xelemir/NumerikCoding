"""
In der Vorlesung haben wir gesehen, dass wir mit richtiger Wahl der Stutzstellen die Qualit ¨ ¨at
der Polynominterpolation stark beeinflussen k¨onnen. In dieser Aufgabe vergleichen wir zwei
M¨oglichkeiten fur ¨ n + 1 Stutzstellen auf dem Intervall [ ¨ -1, 1]:

• Aquidistante St ¨ utzstellen

• und die Nullstellen des Tschebyscheff-Polynoms Tn+1:
    
a) Die Restgliedformel wird uns noch lehren: Das Stutzstellenpolynom Φ ¨ n soll betragsm¨aßig
m¨oglichst klein sein. Fertigen Sie fur ¨ n = 8 und n = 20 je ein Bild an, das die beiden
Stutzstellenpolynome ( ¨ ¨aquidistant und Tschebyscheff) zeigt.


"""

import numpy as np
import matplotlib.pyplot as plt

# Funktion zur Berechnung des Stützstellenpolynoms
def stutzstellenpolynom(x, stutzstellen):
    P = 1
    for xi in stutzstellen:
        P *= (x - xi)
    return P

# Stützstellen berechnen
def aquidistante_stutzstellen(n):
    return np.linspace(-1, 1, n + 1)

def tschebyscheff_stutzstellen(n):
    return np.cos((2 * np.arange(n + 1) + 1) * np.pi / (2 * (n + 1)))

# Werte für n
ns = [8, 20]

# Plotten der Stützstellenpolynome
x = np.linspace(-1, 1, 400)

plt.figure(figsize=(12, 8))
for i, n in enumerate(ns):
    # Äquidistante Stützstellen
    x_aqui = aquidistante_stutzstellen(n)
    P_aqui = stutzstellenpolynom(x, x_aqui)

    # Tschebyscheff-Stützstellen
    x_tscheb = tschebyscheff_stutzstellen(n)
    P_tscheb = stutzstellenpolynom(x, x_tscheb)
    
    # Plotten
    plt.subplot(2, 2, 2 * i + 1)
    plt.plot(x, P_aqui, label=f'Äquidistant, n={n}')
    plt.scatter(x_aqui, np.zeros_like(x_aqui), color='red')
    plt.title(f'Äquidistante Stützstellen (n={n})')
    plt.xlabel('x')
    plt.ylabel('$P(x)$')
    plt.legend()
    
    plt.subplot(2, 2, 2 * i + 2)
    plt.plot(x, P_tscheb, label=f'Tschebyscheff, n={n}')
    plt.scatter(x_tscheb, np.zeros_like(x_tscheb), color='blue')
    plt.title(f'Tschebyscheff-Stützstellen (n={n})')
    plt.xlabel('x')
    plt.ylabel('$P(x)$')
    plt.legend()

plt.tight_layout()
plt.show()

import math
import matplotlib.pyplot as plt

def f(x):
    return math.sin(x)

def df(x):
    return math.cos(x)

x = 2
k_values = range(1, 16)  # k von 1 bis 15
errors = []

for k in k_values:
    h = 10**(-k)
    forward_difference = (f(x + h) - f(x)) / h
    error = abs(df(x) - forward_difference)
    errors.append(error)

plt.figure(figsize=(10, 6))
plt.plot(k_values, errors)
plt.xlabel('k (Exponent of h: 10^(-k))')
plt.ylabel('log10 |f\' - Dhf|')
plt.yscale('log')  # logarithmische Skala auf der y-Achse
plt.title('Absolute Fehler in Abhängigkeit von k')
plt.grid(True)
plt.show()

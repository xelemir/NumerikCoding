import math
import sys

def f(x):
    return math.sin(x)

x = 2
eps = sys.float_info.epsilon
k = 1
h = 10**(-k)

while h >= eps:
    vorwaerts_differenzenquotient = (f(x + h) - f(x)) / h
    print(f"For h = 10^(-{k}): Dhf(x) = {vorwaerts_differenzenquotient}")
    k += 1
    h = 10**(-k)

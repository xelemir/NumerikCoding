import numpy as np

# Define the interpolation points and the given polynomial P_2,2
x_points = [-2, -1, 0, 1]
n = len(x_points)

# Initialize P with zeros, we'll fill it as we compute values
P = np.zeros((n, n), dtype=object)

# Define P_2,2 explicitly since it is given
def P_2_2(x):
    return x**2 + x + 1

# Compute the function values at given points based on P_2_2
f_values = [P_2_2(x) for x in x_points]

# Fill the first column of P with these function values
for i in range(n):
    P[i, 0] = f_values[i]

# Use Aitken-Neville's recurrence formula to fill the rest of P
for k in range(1, n):
    for i in range(k, n):
        P[i, k] = lambda x, i=i, k=k: ((x - x_points[i - k]) * P[i, k - 1](x) - (x - x_points[i]) * P[i - 1, k - 1](x)) / (x_points[i] - x_points[i - k])

# Define a function to print the results in a readable format
def print_P_matrix(P, x_points):
    print("P matrix:")
    for i in range(len(x_points)):
        for j in range(len(x_points)):
            if P[i, j] != 0:
                if callable(P[i, j]):
                    print(f"P[{i},{j}](x) = {P[i, j](x_points[j])}")
                else:
                    print(f"P[{i},{j}] = {P[i, j]}")
            else:
                print(f"P[{i},{j}] = 0")
        print()

# Print the matrix
print_P_matrix(P, x_points)

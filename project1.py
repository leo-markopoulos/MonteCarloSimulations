# -*- coding: utf-8 -*-
"""project1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Alw6QKlWhuEWneNn09pLmY_OJMbcHUZL
"""

import random
import matplotlib.pyplot as plt

# Function to estimate Pi using Monte Carlo simulation
def monte_carlo_pi(num_samples):
    inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point is inside the unit circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    # Estimate Pi
    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate, x_inside, y_inside, x_outside, y_outside

# Number of samples for the simulation
num_samples = 10000

# Perform Monte Carlo simulation
pi_estimate, x_inside, y_inside, x_outside, y_outside = monte_carlo_pi(num_samples)

# Plot the results
plt.figure(figsize=(6, 6))
plt.scatter(x_inside, y_inside, color='blue', s=1, label='Inside Circle')
plt.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f'Monte Carlo Simulation for Pi Estimation\nEstimated Pi: {pi_estimate}')
plt.legend()
plt.show()

print(f"Estimated Pi: {pi_estimate}")
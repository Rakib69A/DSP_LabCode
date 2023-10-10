import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the numerator and denominator coefficients
numerator = [1, 0, 0, 1]
denominator = [1, 0, 2, 0, 1]

# Create a transfer function using scipy.signal.TransferFunction
system = signal.TransferFunction(numerator, denominator)

# Display the transfer function
print("Transfer Function:")
print(system)

# Calculate and plot the pole-zero map
plt.figure(figsize=(6, 6))
plt.title("Pole-Zero Map")
plt.grid(True)
plt.scatter(system.zeros.real, system.zeros.imag, marker='o', color='b', label='Zeros')
plt.scatter(system.poles.real, system.poles.imag, marker='x', color='r', label='Poles')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.show()

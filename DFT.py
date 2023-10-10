import numpy as np
import matplotlib.pyplot as plt

# Input the length of the sequence
N = int(input('Enter the length of sequence: '))

# Input the sequence
x = np.array([complex(z) for z in input('Enter the sequence (space-separated values): ').split()])

# Create time indices n and frequency indices k
n = np.arange(N)
k = np.arange(N)

# Calculate wN (twiddle factor)
wN = np.exp(-1j * 2 * np.pi / N)

# Create matrices for nk and wNnk
nk = np.outer(n, k)
wNnk = wN ** nk

# Compute the DFT Xk
Xk = np.dot(x, wNnk)

# Display Xk
print('Xk =')
print(Xk)

# Calculate magnitude and phase
mag = np.abs(Xk)
phase = np.angle(Xk)

# Plot magnitude
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.stem(k, mag)
plt.grid(True)
plt.xlabel('k')
plt.ylabel('Magnitude')
plt.title('Magnitude of Fourier Transform')

# Plot phase
plt.subplot(2, 1, 2)
plt.stem(k, phase)
plt.grid(True)
plt.xlabel('k')
plt.ylabel('Phase')
plt.title('Phase of Fourier Transform')

plt.tight_layout()
plt.show()

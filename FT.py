import numpy as np
import matplotlib.pyplot as plt

# Define parameters
N = 250
ts = 0.0002
t = np.arange(N) * ts
frequencies = np.arange(801)  # Frequency range from 0 to 800

# Generate the signal
x = np.cos(2 * np.pi * 100 * t) + np.cos(2 * np.pi * 500 * t) + np.cos(2 * np.pi * 800 * t)

# Plot the original signal
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Compute the Fourier Transform using numerical integration (Trapezoidal rule)
X = np.zeros(len(frequencies), dtype=complex)
for k, f in enumerate(frequencies):
    X[k] = np.trapz(x * np.exp(-1j * 2 * np.pi * f * t), t)

# Plot the magnitude spectrum
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(X))
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.tight_layout()
plt.show()

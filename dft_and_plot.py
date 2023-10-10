import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    X = np.fft.fft(x)
    return X

# Create a sample signal
Fs = 1000  # Sampling frequency
T = 1.0 / Fs  # Time period
N = 1000  # Number of data points
t = np.linspace(0.0, N * T, N, endpoint=False)  # Time vector
freq = 5  # Frequency of the signal
x = np.sin(2 * np.pi * freq * t)  # Sample sine wave signal

# Compute the DFT
X = dft(x)

# Calculate the frequency values corresponding to the DFT result
frequencies = np.fft.fftfreq(N, T)

# Plot the magnitude and phase of the DFT
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(frequencies[:N // 2], np.abs(X[:N // 2]))
plt.title('Magnitude of DFT')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.subplot(2, 1, 2)
plt.plot(frequencies[:N // 2], np.angle(X[:N // 2]))
plt.title('Phase of DFT')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (radians)')

plt.tight_layout()
plt.show()

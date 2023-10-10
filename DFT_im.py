import numpy as np
import matplotlib.pyplot as plt

# Clear any existing plots
plt.close('all')

Fa = 10
T = 1 / Fa
t = np.arange(0, T, T / 99)
y = 5 * np.sin(2 * np.pi * Fa * t) + 2 * np.sin(2 * np.pi * 2 * Fa * t) + 2 * np.sin(2 * np.pi * 3 * Fa * t)
plt.figure(1)
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Continuous Signal')
plt.grid(True)

Fs = 640
Ts = 1 / Fs
N = int(T / Ts)
n = np.arange(0, N)
yy = 5 * np.sin(2 * np.pi * Fa * n * Ts) + 2 * np.sin(2 * np.pi * 2 * Fa * n * Ts) + 2 * np.sin(2 * np.pi * 3 * Fa * n * Ts)
plt.figure(2)
plt.stem(n, yy)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('Discrete Signal')
plt.grid(True)

b = np.zeros(N, dtype=complex)
for k in range(N):
    for n in range(N):
        ff = yy[n] * np.exp(-1j * 2 * np.pi * (k - 1 - (N / 2)) * (n - 1 - (N / 2)) / N)
        b[k] += ff

plt.figure(3)
f = Fs * np.fft.fftshift(np.arange(-N / 2, N / 2)) / N
plt.stem(f, np.abs(b))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')
plt.axis([-30, 30, 0, 160])
plt.grid(True)

plt.show()

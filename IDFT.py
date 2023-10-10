import numpy as np
import matplotlib.pyplot as plt

# Input the sequence X(k)
Xk = np.array([float(x) for x in input('Enter X(k) (space-separated values): ').split()], dtype=np.complex128)

# Ensure Xk is a column vector
N = len(Xk)
Xk = Xk.reshape(-1, 1)

# Initialize the output sequence xn
xn = np.zeros((N, 1), dtype=np.complex128)

k = np.arange(N)

for n in range(N):
    xn[n] = np.sum(np.exp(1j * 2 * np.pi * k * n / N) * Xk)

xn /= N  # Normalize by dividing by N

# Display and plot the result
print('x(n)=')
print(xn)

plt.figure(figsize=(8, 4))
plt.subplot(2, 1, 1)
plt.plot(np.real(xn))
plt.grid(True)
plt.xlabel('n')
plt.ylabel('Magnitude')
plt.title('IDFT OF A SEQUENCE')

plt.subplot(2, 1, 2)
plt.stem(k, np.real(xn))
plt.grid(True)
plt.xlabel('n')
plt.ylabel('Magnitude')
plt.title('IDFT OF A SEQUENCE (Stem Plot)')

plt.tight_layout()
plt.show()

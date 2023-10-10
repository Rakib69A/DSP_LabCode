from scipy import signal
import numpy as np

# Define the discrete-time signal f(n)
def f(n):
    return 2**n + 2**n * (n - 1)

# Compute the Z-transform of f(n)
system = signal.dlti(f(np.arange(10)), [1], dt=1)
zpgd = system.to_zpk()

# Access zeros, poles, and gain separately
zeros = zpgd.zeros
poles = zpgd.poles
gain = zpgd.gain

# Display the Zeros, Poles, and Gain
print(f"Zeros: {zeros}")
print(f"Poles: {poles}")
print(f"Gain: {gain}")

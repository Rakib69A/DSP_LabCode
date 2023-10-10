import numpy as np
import matplotlib.pyplot as plt


A = input('Amplitude of Transmitting signal: ')
print('\n')
#xxxxxxxxxxxxxxTransmitting Signal Generationxxxxxx
f = 100
T=1/f
t=np.arange(0,2*T,T/100)
A = 1 # set the amplitude for(e.g., 1 for simplicity)
y = A*np.sin(2*np.pi*f*t)

plt.figure(1)
plt.plot(t,y,linewidth=3)
plt.ylabel('Amplitude (volt)')
plt.xlabel('Time (sec)')
plt.title('Transmitting signal')
plt.show()

#xxxxxxxxxxxxxxxxxxxxxx Sampling xxxxxxxxxxxxxxxxxx
Ts = T/20
Fs = 1/Ts
n = np.arange(1,int(2*T/Ts)+1)
y1 = A* np.sin(2*np.pi*f*n*Ts)

plt.figure(2)
plt.stem(n,y1)
plt.ylabel('Amplitude(volt)')
plt.xlabel('Discrete Time')
plt.title('Discrete Time Signal(Signal After Plotting)')
plt.show()

#XXXXXXXXXXXXXXXXXXXXXXXXXXXX Additional of DC Level XXXXXXXXXXXXXXXXXXXXXXX
# Compute y2 by adding A to y1
y2 = A + y1

# Plot y2
plt.figure(3)
plt.stem(n, y2)
plt.ylabel('Amplitude (volt)')
plt.xlabel('Discrete time')
plt.title('DC Level + Discrete Time signal Signal')
plt.show()

# XXXXXXXXXXXXXXXXXXXXXXXXXXXX Quantization Signal XXXXXXXXXXXXXXXXXXXXXXXXX
# Quantize y2 by rounding to the nearest integer
y3 = np.round(y2)

# Plot quantized signal y3
plt.figure(4)
plt.stem(n, y3)
plt.ylabel('Amplitude (volt)')
plt.xlabel('Discrete time')
plt.title('Quantized signal')
plt.show()

# Convert y3 to binary representation
y4 = [bin(int(x))[2:].zfill(8) for x in y3]

# Display binary representation
Bi = y4
print(Bi)

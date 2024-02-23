import numpy as np
import matplotlib.pyplot as plt

N = 11

def f(x):
    return np.sin(np.pi * x / N)

x_values = np.linspace(0, 10, 1000)

y_values = f(x_values)

plt.plot(x_values , y_values)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
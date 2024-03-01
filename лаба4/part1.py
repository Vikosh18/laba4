import matplotlib.pyplot as plt
import math

N = 11

def f(x):
    return math.sin(math.pi * x / N)

x_values = [i/100 for i in range(1001)]
y_values = [f(x) for x in x_values]

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['f(x)'])
plt.grid(True)
plt.show()

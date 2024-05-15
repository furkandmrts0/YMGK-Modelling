import numpy as np
import matplotlib.pyplot as plt

def plot_ikeda_attractor(x0=0.1, y0=0.1, u=0.9, iterations=10000):
    def ikeda_map(x, y, u):
        t = 0.4 - 6 / (1 + x**2 + y**2)
        x_next = 1 + u * (x * np.cos(t) - y * np.sin(t))
        y_next = u * (x * np.sin(t) + y * np.cos(t))
        return x_next, y_next

    x_values = [x0]
    y_values = [y0]
    for _ in range(iterations):
        x, y = ikeda_map(x_values[-1], y_values[-1], u)
        x_values.append(x)
        y_values.append(y)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, '.', markersize=0.5)
    plt.title('Ikeda Chaotic Attractor')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Kullanımı
plot_ikeda_attractor()

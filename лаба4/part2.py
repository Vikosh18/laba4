import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot

def simulate_dice_roll(N, asymmetric=False):
    if asymmetric:
        dice1 = np.random.randint(1, N + 1)
        dice2 = np.random.choice(np.arange(1, N + 1), p=np.arange(1, N + 1) / np.sum(np.arange(1, N + 1)))
    else:
        dice1 = np.random.randint(1, N + 1)
        dice2 = np.random.randint(1, N + 1)
    return dice1 + dice2

def generate_histogram(N, asymmetric=False):
    results = [simulate_dice_roll(N, asymmetric) for _ in range(10000)]
    histogram_data = np.histogram(results, bins=np.arange(2, 2 * N + 2))
    return histogram_data

def plot_histogram(histogram_data):
    fig = go.Figure(data=[go.Bar(x=histogram_data[1][:-1], y=histogram_data[0])])
    fig.update_layout(title="результат кидків кубиків",
                      xaxis_title="Сума результатів",
                      yaxis_title="Частота")
    return plot(fig, output_type='div')

N = 6 + 3  
histogram_symmetric = generate_histogram(N)
histogram_asymmetric = generate_histogram(N, asymmetric=True)

plot_symmetric = plot_histogram(histogram_symmetric)
plot_asymmetric = plot_histogram(histogram_asymmetric)

with open('histogram_symmetric.html', 'w', encoding='utf-8') as file:
    file.write(plot_symmetric)

with open('histogram_asymmetric.html', 'w', encoding='utf-8') as file:
    file.write(plot_asymmetric)
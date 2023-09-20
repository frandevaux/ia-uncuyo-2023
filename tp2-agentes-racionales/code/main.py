import random
from agent import Agent
from environment import Environment
import matplotlib.pyplot as plt
import numpy as np

# Define los tamaños de los entornos y las tasas de suciedad
environment_sizes = [2, 4, 8, 16, 32, 64, 128]
dirt_rates = [0.1, 0.2, 0.4, 0.8]
repeating_amount = 10
results = []

# Genera datos
for i, size in enumerate(environment_sizes):
    row = []

    for j, dirt_rate in enumerate(dirt_rates):
        moves = []
        points = []

        for _ in range(repeating_amount):
            env = Environment(size, size, dirt_rate)
            agent = Agent(env, random.randint(0, env.sizeX-1), random.randint(0, env.sizeY-1), True)
            moves.append(1000 - agent.remaining_actions)
            points.append(agent.points)

        avgMoves = sum(moves) / len(moves)
        avgPoints = sum(points) / len(points)
        row.append([avgPoints, avgMoves])

    results.append(row)

# Gráficos de barras
fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()

colors = ['#9E7BCB', '#8B67AF', '#7A5495', '#69427B']
bar_width = 0.2
x_positions = np.arange(len(environment_sizes))

for i, dirt_rate in enumerate(dirt_rates):
    movements = [result[i][1] for result in results]
    points = [result[i][0] for result in results]

    ax.bar(x_positions + i * bar_width, movements, bar_width, label=f'Tasa de suciedad {dirt_rate}', color=colors[i])
    ax2.bar(x_positions + i * bar_width, points, bar_width, label=f'Tasa de suciedad {dirt_rate}', color=colors[i])

ax.set_xlabel('Tamaño del Entorno')
ax.set_ylabel('Movimientos Promedio')
ax.set_title('Movimientos Promedio por Tamaño y Suciedad (Agente Aleatorio)')
ax.set_xticks(x_positions + bar_width * (len(dirt_rates) - 1) / 2)
ax.set_xticklabels(environment_sizes)
ax.legend()

ax2.set_xlabel('Tamaño del Entorno')
ax2.set_ylabel('Puntos Promedio')
ax2.set_title('Puntos Promedio por Tamaño y Suciedad (Agente Aleatorio)')
ax2.set_xticks(x_positions + bar_width * (len(dirt_rates) - 1) / 2)
ax2.set_xticklabels(environment_sizes)
ax2.legend()
ax2.set_ylim(0, 250)

fig.savefig('movimientos_promedio_aleatorio.png')
fig2.savefig('puntos_promedio_aleatorio.png')


plt.tight_layout()
plt.show()

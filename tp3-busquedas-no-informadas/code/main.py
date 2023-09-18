from environment import Environment
from agent import Agent

env= Environment(50, (0,0), (49,49))
agent = Agent(env)
    # Realizar la búsqueda a lo ancho y obtener el camino
camino_encontrado = agent.bfs()
env.print_environment(camino_encontrado)



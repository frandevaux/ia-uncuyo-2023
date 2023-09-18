from environment import Environment
from agent import Agent

env = Environment(10, (0, 0), (9, 9))
agent = Agent(env)
camino_encontrado = agent.ldfs(20)
print("Camino encontrado: ", camino_encontrado)
env.print_environment(camino_encontrado)

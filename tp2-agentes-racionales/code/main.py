from environment import Environment
from agent import Agent
from random import randint


env = Environment(3, 3, 0.25)
env.print_environment()
agent = Agent(env, randint(0, env.sizeX-1), randint(0, env.sizeY-1))

print()
print("Numero de acciones restantes: ", agent.remaining_actions)
print("Puntos: ", agent.points)
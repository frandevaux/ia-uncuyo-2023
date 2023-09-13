from environment import Environment
from slot import Slot
from agent import Agent

env= Environment(100, (0,0), (99,99))

env.print_environment()

agent = Agent(env)
agent.bfs()
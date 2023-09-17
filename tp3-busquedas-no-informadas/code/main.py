from environment import Environment
from slot import Slot
from agent import Agent

env= Environment(15, (0,0), (10,10))

env.print_environment()

agent = Agent(env)
bfs = agent.bfs()
env.print_environment(None, bfs)



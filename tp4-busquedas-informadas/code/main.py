from environment import Environment
from agent import Agent

env = Environment(100, (0, 0), (99, 99))
agent = Agent(env)

"""print( "Busqueda a lo ancho: ")
result = agent.bfs()
print("Cantidad de nodos visitados: ", result[1])
print("Longitud del camino: ", len(result[0]))
env.print_environment(result[0])

print( "Busqueda en profundidad: ")
result = agent.dfs()
print("Cantidad de nodos visitados: ", result[1])
print("Longitud del camino: ", len(result[0]))
env.print_environment(result[0])

print( "Busqueda en profundidad limitada: ")
result = agent.ldfs(1000)
print("Cantidad de nodos visitados: ", result[1])
print("Longitud del camino: ", len(result[0]))
env.print_environment(result[0])
"""
print( "Busqueda con A*: ")
result = agent.astar()
print("Cantidad de nodos visitados: ", result[1])
print("Longitud del camino: ", len(result[0]))
env.print_environment(result[0])

print( "Busqueda de costo uniforme: ")
result = agent.ucs()
print("Cantidad de nodos visitados: ", result[1])
print("Longitud del camino: ", len(result[0]))
env.print_environment(result[0])


### Pregunta 2.10: Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.

#### a. Can a simple reflex agent be perfectly rational for this environment? Explain.

No, un agente reflexivo simple no puede ser perfectamente racional en este entorno. La falta de conocimiento completo del estado del entorno y la ausencia de memoria para recordar lugares previamente visitados impiden que el agente tome decisiones óptimas y podría incurrir en repeticiones innecesarias o pérdida de puntos al no poder planificar la mejor ruta.

#### b. What about a reflex agent with state? Design such an agent.

Un agente reflexivo con estado podría mejorar su desempeño en entornos parcialmente observables al recordar los casilleros que ya ha visitado. Sin embargo, incluso con esta memoria, seguiría enfrentando limitaciones en términos de eficiencia y toma de decisiones óptimas en entornos no totalmente observables, ya que aún carecería de un conocimiento completo del entorno para calcular la ruta más eficiente y tomar decisiones perfectamente racionales.

#### c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?

Si el agente tuviera información sobre el estado de cada casillero en el entorno y memoria de los casilleros por los que ya pasó, se podría diseñar un agente reflexivo con estado que fuera perfectamente racional. Esto le permitiría calcular la ruta más eficiente para limpiar todos los casilleros y evitar pasar dos veces por el mismo, lo que aumentaría su eficiencia en la tarea de limpieza.

---

### Pregunta 2.11: Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right .)

#### a. Can a simple reflex agent be perfectly rational for this environment? Explain.

Un agente reflexivo simple puede ser perfectamente racional para este entorno si no se penaliza por movimientos adicionales, ya que puede limpiar los casilleros a medida que los visita, eventualmente logrando limpiar todo el entorno, incluso sin conocer su estado inicial.

#### b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.

Basándonos en la información proporcionada en los ejercicios realizados, parece que un agente reflexivo simple tiende a superar a un agente aleatorio en la mayoría de los casos. Si bien en entornos pequeños su rendimiento puede ser comparable, a medida que el entorno se vuelve más complejo, el agente aleatorio tiende a quedar rezagado frente al agente reflexivo. Por lo tanto, en términos de rendimiento general, un agente reflexivo simple parece ser una elección más efectiva que un agente aleatorio.

#### c. Can you design an environment in which your randomized agent will perform poorly? Show your results.

Un agente que opera de manera aleatoria puede experimentar un bajo desempeño en un entorno donde la probabilidad de encontrar un casillero sucio sea extremadamente baja, así como en entornos de gran tamaño, como se ilustra en los ejercicios D y E. En tales situaciones, donde la probabilidad de encontrar casilleros sucios es mínima y el entorno es amplio, el agente aleatorio enfrenta desafíos adicionales al intentar localizar y limpiar la suciedad, lo que finalmente se traduce en un rendimiento insatisfactorio.

#### d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?

Sí, un agente que puede recordar las cosas puede funcionar mejor que uno que solo reacciona al momento, ya que evita repetir las mismas acciones. Sin embargo, en lugares muy grandes, todavía podría realizar multiples movimientos antes de encontrar lo que necesita. A pesar de esto, el agente que recuerda es una elección más inteligente en comparación con el agente simple, ya que usa lo que sabe para tomar decisiones más sensatas.

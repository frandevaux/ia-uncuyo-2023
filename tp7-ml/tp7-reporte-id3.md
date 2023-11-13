## Parte C - Reporte sobre ID3

### A. Resultados de la evaluación sobre dataset tennis.csv

    'outlook': {
        'overcast': 'yes',
        'rainy': {
            'windy': {
                False: 'yes',
                True: 'no'
            }
        },
        'sunny': {
            'humidity': {
                'high': 'no',
                'normal': 'yes'
            }
        }
    }

### B. Información de estrategias aplicadas en datos de tipo real.

Las características de los árboles de decisión nos permiten trabajar de forma flexible con datos categóricos y con datos númericos reales. A continuación, se detallan algunas de las tácticas comúnmente utilizadas con datos de tipo real:

- **Bifurcación basada en umbrales numéricos:** En el ámbito de los árboles de decisión, los nodos tienen la capacidad de realizar divisiones fundamentadas en umbrales numéricos para abordar variables continuas. Por ejemplo, un nodo podría segmentar los datos en dos ramas según si una característica numérica supera o iguala un umbral predeterminado.

- **Criterios de impureza:** Los árboles de decisión emplean criterios de impureza, como la ganancia de información, el índice de Gini o el error cuadrático medio, para determinar la manera de dividir los datos en cada nodo. Estos criterios son aplicables tanto a variables categóricas como a variables numéricas.

- **Podas y ajustes:** Con el propósito de prevenir el sobreajuste, se pueden implementar estrategias de poda y ajuste en los árboles de decisión. La poda regula la profundidad del árbol, y es posible establecer umbrales para decidir cuándo detener la división de un nodo basándose en la impureza o la ganancia de información.

- **Algoritmos específicos:** Algunos algoritmos de árboles de decisión, como CART (Classification and Regression Trees), están específicamente diseñados para manejar eficientemente variables numéricas. Estos algoritmos pueden determinar automáticamente los umbrales óptimos para la división de variables numéricas.

- **Transformación de variables:** Previo a la construcción del árbol, es factible aplicar transformaciones a variables numéricas, tales como discretización o normalización, con el fin de mejorar la capacidad del árbol para identificar patrones.

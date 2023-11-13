import numpy as np
import pandas as pd
import pprint

# Función que calcula entropía de un conjunto de datos
def entropy(data):
    if len(data) == 0:
        return 0
    p = data.value_counts(normalize=True)
    return -np.sum(p * np.log2(p))

# Función de calculo de ganancia de información dado un atributo
def gain(data, attribute, class_name):
    total_entropy = entropy(data[class_name])
    values = data[attribute].unique()
    weighted_entropy = 0

    for i in values:
        subset = data[data[attribute] == i]
        weighted_entropy += len(subset) / len(data) * entropy(subset[class_name])

    return total_entropy - weighted_entropy

# Función para encontrar el valor más común en una clase en un conjunto de datos
def common_value(data, class_name):
    return data[class_name].value_counts().idxmax()

# Función para construir un árbol de decisión a partir de la ganancia de información
def decision_tree_creator(examples, attributes, parents, class_name):
    if len(examples) == 0:
        return common_value(parents, class_name)
    elif len(examples[class_name].unique()) == 1:
        return examples[class_name].iloc[0]
    elif len(attributes) == 0:
        return common_value(examples, class_name)
    else:
        best_attribute = max(attributes, key=lambda a: gain
    (examples, a, class_name))
        tree = {best_attribute: {}}
        attributes.remove(best_attribute)
        for value in examples[best_attribute].unique():
            subset = examples[examples[best_attribute] == value]
            subtree = decision_tree_creator(subset, attributes.copy(), examples, class_name)
            tree[best_attribute][value] = subtree
        return tree

# Cargar datos desde un archivo csv
data = pd.read_csv("https://raw.githubusercontent.com/sjwhitworth/golearn/master/examples/datasets/tennis.csv")

# Definir atributos y clase
class_name = "play"
attributes = ["outlook", "temp", "humidity", "windy"]

# Construir el árbol de decisión
decision_tree = decision_tree_creator(data, attributes, data, class_name)

# Imprimir el árbol
pprint.pprint(decision_tree)
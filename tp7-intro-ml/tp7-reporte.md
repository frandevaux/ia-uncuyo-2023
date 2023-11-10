## TP7-Intro - Francisco Devaux

### Ejercicios ISLR

### 1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

#### (a) The sample size n is extremely large, and the number of predictors p is small.

En esta situación, comúnmente anticiparíamos que la eficacia de un metodo inflexible sea superior a la de uno flexible. Con un conjunto de datos de gran magnitud, los métodos flexibles pueden identificar patrones intricados, aunque existe el riesgo de sobreajustarse. Optar por un método menos adaptable podría ser más conveniente, ya que podría tener menos propensión a ajustarse excesivamente a sutilezas en los datos.

#### (b) The number of predictors p is extremely large, and the number of observations n is small.

En esta situación, sería razonable esperar que la efectividad de un enfoque flexible supere a la de uno inflexible. Cuando hay un gran número de predictores y una muestra pequeña, un método flexible podría tener una mayor capacidad para capturar relaciones complejas en los datos, a diferencia de un método inflexible que podría no ser lo bastante complejo para modelar la variabilidad.

#### (c) The relationship between the predictors and response is highly non-linear.

En esta instancia, podríamos anticipar que el desempeño de un enfoque flexible sea superior al de uno inflexible. Los métodos flexibles, como los modelos no lineales, tienen la capacidad de capturar relaciones no lineales de manera más eficaz, mientras que los enfoques inflexibles podrían enfrentar dificultades para representar patrones no lineales.

#### (d) The variance of the error terms, i.e. σ^2 = Var(ϵ), is extremely high.

Debido a que el error irreducible es considerablemente alto, no sería apropiado emplear un método excesivamente flexible, ya que podría sobreajustarse al ruido en lugar de identificar patrones genuinos. En términos generales, el uso de métodos flexibles tiende a incrementar la varianza. Por ende, la recomendación sería buscar un método que sea flexible pero al mismo tiempo más restringido, con el objetivo de reducir la varianza sin aumentar excesivamente el sesgo.

### 2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

#### (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors aﬀect CEO salary.

Tipo de Problema: Regresión.

Interés Principal: Inferencia, entender la relación entre los factores y el salario del CEO.

n = 500

p = 4

#### (b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.

Tipo de Problema: Clasificación.

Interés Principal: Predicción, determinar si el nuevo producto será un éxito o un fracaso.

n = 20

p = 15

#### (c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.

Tipo de Problema: Regresión.

Interés Principal: Predicción, determinar el % de cambio en la tasa de cambio USD/Euro en función de los cambios semanales en los mercados bursátiles mundiales.

n = 52

p = 4

### 5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

Beneficios de un enfoque altamente adaptable:

- Identificación de Relaciones Complejas: Un método flexible, como la implementación de un modelo sofisticado, como una red neuronal profunda o un árbol de decisiones con una gran cantidad de nodos, tiene la capacidad de detectar relaciones intrincadas y no lineales en los datos.

- Mayor Exactitud: En casos en los cuales la conexión subyacente entre los predictores y la respuesta es complicada, un modelo adaptable puede ofrecer una precisión superior al ajustarse de manera más ajustada a los datos de entrenamiento.

- Flexibilidad: Los modelos flexibles tienen la capacidad de ajustarse eficazmente a patrones diversos y cambiantes en los datos, lo que los convierte en opciones apropiadas para sistemas dinámicos o en constante evolución.

Este tipo de enfoques podría ser la elección preferida en situaciones en las que la relación entre los predictores y la respuesta es compleja y no lineal, cuando se dispone de conjuntos de datos amplios y variados, o en análisis exploratorios donde la prioridad es la predicción en lugar de la interpretación.

En contraste, un enfoque menos flexible podría ser preferido cuando la interpretabilidad es fundamental, como en áreas donde las explicaciones del modelo son indispensables, en situaciones con datos escasos (para prevenir el sobreajuste), o cuando hay restricciones en los recursos computacionales.

### 6. Describe the diﬀerences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a non-parametric approach)? What are its disadvantages?

Los modelos paramétricos y no paramétricos se distinguen por las suposiciones que realizan acerca de la forma de la relación funcional entre los predictores y la respuesta. Mientras que los modelos paramétricos presuponen una estructura específica para la función (como en el caso de las regresiones lineales), lo que implica la estimación de un número limitado de parámetros, los modelos no paramétricos no hacen suposiciones acerca de la forma de la función y tienen la capacidad de adaptarse a patrones más complejos, lo que conlleva a la estimación de un mayor número de elementos.

La decisión entre adoptar un enfoque paramétrico o no paramétrico está sujeta a diversos factores. Se prefiere la utilización de modelos paramétricos cuando las suposiciones estructuradas son aplicables y hay restricciones en la disponibilidad de datos. Estos modelos presentan la ventaja de ser más eficientes desde el punto de vista computacional y más fácilmente interpretables. En cambio, los modelos no paramétricos resultan ideales cuando se busca una mayor flexibilidad y no se tienen conocimientos previos sobre las relaciones funcionales.

En el contexto de la regresión o clasificación, un enfoque adaptable tiene la ventaja de disminuir el sesgo al aproximarse a situaciones de la vida real, lo que puede resultar en un menor error. No obstante, este enfoque también tiene el inconveniente de aumentar la varianza, lo que implica que las estimaciones podrían variar significativamente al aplicarse a un conjunto de datos diferente. Cuando el patrón real no es lineal y hay suficientes observaciones, un enfoque flexible tiende a generar resultados superiores. En cambio, si asumimos que el patrón es lineal, podría preferirse un método menos adaptable, como la regresión lineal, debido a su menor sesgo.

### 7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.

| Obs. | X1  | X2  | X3  | Y     |
| ---- | --- | --- | --- | ----- |
| 1    | 0   | 3   | 0   | Red   |
| 2    | 2   | 0   | 0   | Red   |
| 3    | 0   | 1   | 3   | Red   |
| 4    | 0   | 1   | 2   | Green |
| 5    | -1  | 0   | 1   | Green |
| 6    | 1   | 1   | 1   | Red   |

### Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.

#### (a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0.

| **Observación** | **Distancia Euclidiana** |
| --------------- | ------------------------ |
| 1               | 3                        |
| 2               | 2                        |
| 3               | \(\sqrt{10}\)            |
| 4               | \(\sqrt{5}\)             |
| 5               | \(\sqrt{2}\)             |
| 6               | \(\sqrt{3}\)             |

#### (b) What is our prediction with K = 1? Why?

La predicción es Y = Green porque la 4ta observación tiene la distancia Euclidiana más corta (1).

#### (c) What is our prediction with K = 3? Why?

La predicción es Y = Red porque 2 de sus 3 vecinos más cercanos tienen la clase Red.

#### (d) If the Bayes decision boundary in this problem is highly non-linear, then would we expect the best value for K to be large or small? Why?

En el caso de una frontera de decisión de Bayes altamente no lineal, se anticipa que un valor óptimo para K sería reducido. La razón de esto radica en que un valor pequeño de K posibilita que el algoritmo identifique patrones más locales, evitando depender excesivamente de la estructura global de los datos. En contraste, un valor grande de K tendería a suavizar excesivamente la frontera de decisión, lo que podría resultar en la pérdida de los detalles no lineales presentes en los datos.

### Desafío Arbolado Kaggle

#### A. Proceso de preprocesamiento:

Se eliminaron las variables:

- id
- nombre_seccion
- diametro_tronco
- ultima_modificacion
- area_seccion
- seccion

_Solucionamos problema de desbalanceo con Undersampling:_

Tomamos un sample para tener un conjunto de arboles sin inclinación peligrosa que tenga la misma cantidad de elementos que aquellos con peligrosidad.
Unimos ambos conjuntos y lo volvemos nuestro set de entrenamiento.

#### B. Resultados obtenidos sobre el conjunto de validación

![validation](image-1.png)

#### C. Resultados obtenidos en Kaggle

![kaggle](image.png)

#### D. Descripción detallada del algoritmo propuesto

El algoritmo implementado se basa en un modelo de Random Forest utilizando la librería ranger. La configuración del modelo se realizó cuidadosamente, utilizando los siguientes parámetros:

num.trees = 400
mtry = 2

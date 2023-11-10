library(ranger)
library(dplyr)
library(readr)

data_train <- read_csv("./data/arbolado-mza-dataset.csv", col_types = cols(
  id = col_integer(),
  especie = col_character(),
  ultima_modificacion = col_character(),
  altura = col_character(),
  circ_tronco_cm = col_double(),
  diametro_tronco = col_character(),
  long = col_double(),
  lat = col_double(),
  seccion = col_integer(),
  nombre_seccion = col_character(),
  area_seccion = col_double(),
  inclinacion_peligrosa = col_integer()
))

data_test <- read_csv("./data/arbolado-mza-dataset-test.csv", col_types = cols(
  id = col_integer(),
  especie = col_character(),
  ultima_modificacion = col_character(),
  altura = col_character(),
  circ_tronco_cm = col_double(),
  diametro_tronco = col_character(),
  long = col_double(),
  lat = col_double(),
  seccion = col_integer(),
  nombre_seccion = col_character(),
  area_seccion = col_double()
))

# Eliminar las columnas que deseas del conjunto de entrenamiento (data_train)
data_train <- data_train %>% select(-id, -nombre_seccion, -diametro_tronco, -ultima_modificacion, -area_seccion, -seccion)

# Separar los datos en dos grupos según el valor de inclinacion_peligrosa
data_no_inclinacion <- data_train %>% filter(inclinacion_peligrosa == 0)
data_si_inclinacion <- data_train %>% filter(inclinacion_peligrosa == 1)

# Seleccionar una cantidad de ejemplos de la clase inclinación peligrosa igual a 0
sampled_data_no_inclinacion <- data_no_inclinacion %>%
  sample_n(size = nrow(data_si_inclinacion), replace = TRUE)

# Combinar los dos grupos seleccionados para crear un conjunto de entrenamiento balanceado
balanced_trainset <- bind_rows(sampled_data_no_inclinacion, data_si_inclinacion)

# Convertir la variable objetivo en factor
balanced_trainset$inclinacion_peligrosa <- as.factor(balanced_trainset$inclinacion_peligrosa)

# Entrenar el modelo con los datos balanceados utilizando ranger
arbolado.r <- ranger(inclinacion_peligrosa ~ ., data = balanced_trainset, num.trees = 400, mtry = 2)
arbolado.r

# Realizar predicciones de probabilidad
preds_tree_probs <- predict(arbolado.r, data_test, type = 'response')

# Convertir las probabilidades de factor a numérico
preds_tree <- as.numeric(preds_tree_probs$predictions) - 1

# Crear un marco de datos de resultados y guardarlos en un archivo CSV
submission <- data.frame(id = data_test$id, inclinacion_peligrosa = preds_tree)
readr::write_csv(submission, "./envios/arbolado-mza-dataset-envio-ranger15.csv")
head(submission)

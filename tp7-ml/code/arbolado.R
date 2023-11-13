library(dplyr)


# Cargar el archivo CSV
# datos <- read.csv("arbolado-mza-dataset.csv")


# Creacion de los csv de prueba y validacion

# # Definir el tamaño de la muestra (80%)
# tamano_muestra <- round(nrow(datos) * 0.8)
# 
# # Crear una muestra aleatoria de filas
# muestra <- sample(1:nrow(datos), tamano_muestra)
# 
# # Dividir los datos en dos conjuntos: 80% y 20%
# conjunto_80 <- datos[muestra, ]
# conjunto_20 <- datos[-muestra, ]
# 
# # Guardar los dos conjuntos en archivos CSV separados
# write.csv(conjunto_80, "arbolado-mendoza-dataset-train.csv", row.names = FALSE)
# write.csv(conjunto_20, "arbolado-mendoza-dataset-validation.csv", row.names = FALSE)

# Cargar el archivo de entrenamiento

train <- read.csv("arbolado-mendoza-dataset-train.csv")
#inclinacion_peligrosa

# Definicion de colores
colorAzulClaro <- "#3498db"
colorNaranjaClaro <- "#e67e22"


# Tabla de frecuencias
tabla_frecuencias_inclinacion <- table(train$inclinacion_peligrosa)
print(tabla_frecuencias_inclinacion)

# Histograma

barplot(tabla_frecuencias, beside = TRUE, legend.text = TRUE, col = c(colorAzulClaro, colorNaranjaClaro),
        main = "Comparación de Inclinación Peligrosa por Sección", xlab = "Inclinación Peligrosa",
        ylab = "Frecuencia")


# Crear una tabla de frecuencias cruzadas entre 'inclinacion_peligrosa' y 'seccion'
tabla_frecuencias_seccion <- table(train$inclinacion_peligrosa, train$seccion)

print(tabla_frecuencias_seccion)

# Crear un gráfico de barras
barplot(tabla_frecuencias_seccion, beside = TRUE, legend.text = TRUE, col = c(colorAzulClaro, colorNaranjaClaro),
        main = "Comparación de Inclinación Peligrosa por Sección", xlab = "Inclinación Peligrosa",
        ylab = "Frecuencia")

# Agregar una leyenda
legend("topright", legend = rownames(tabla_frecuencias_seccion), fill = c(colorAzulClaro, colorNaranjaClaro))


# Calcular el promedio de 'inclinacion_peligrosa' por 'seccion'
promedios_inclinacion_seccion <- aggregate(inclinacion_peligrosa ~ seccion, data = train, FUN = mean)

# Crear un gráfico de barras de los promedios
barplot(promedios_inclinacion_seccion$inclinacion_peligrosa, names.arg = promedios_inclinacion_seccion$seccion, col = c(colorAzulClaro),
        main = "Promedio de Inclinación Peligrosa por Sección", xlab = "Sección",
        ylab = "Promedio de Inclinación Peligrosa")


# Matricula 2x2 para mostrar histogramas
par(mfrow=c(2,2))  

hist(train_data$circ_tronco_cm, main="Histograma (5 bins)", xlab="circ_tronco_cm", breaks=5)
hist(train_data$circ_tronco_cm, main="Histograma (10 bins)", xlab="circ_tronco_cm", breaks=10)
hist(train_data$circ_tronco_cm, main="Histograma (20 bins)", xlab="circ_tronco_cm", breaks=20)
hist(train_data$circ_tronco_cm, main="Histograma (30 bins)", xlab="circ_tronco_cm", breaks=30)

# Histograma de circ_tronco_cm dependiendo de inclinación_peligrosa
ggplot(train_data, aes(x = circ_tronco_cm, fill = inclinacion_peligrosa)) +
  geom_histogram(binwidth = 10, position = "identity") +
  labs(title = "Histograma de circ_tronco_cm separado por inclinación_peligrosa", 
       x = "circ_tronco_cm",
       y = "Frecuencia") +
  scale_fill_manual(values = c("si" = "red", "no" = "green")) +
  theme_minimal()

# Restaurar la configuración original
par(mfrow = c(1, 1))

# Crear la nueva variable circ_tronco_cm_cat
train_data <- train_data %>% 
  mutate(circ_tronco_cm_cat = cut(circ_tronco_cm, 
                                  breaks = c(0, 60, 180, 250, Inf),
                                  labels = c("bajo", "medio", "alto", "muy alto"),
                                  include.lowest = TRUE))

# Guardar el nuevo dataframe en un archivo CSV
write_csv(train_data, "./data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv")


train_data <- read.csv("data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv")

# Función que agrega nueva columna con valores aleatorios entre 0 y 1
generate_random_prediction_prob <- function(data) {
  # Generar valores aleatorios entre 0 y 1
  data$prediction_prob <- runif(nrow(data))
  return(data)
}

# Llama a la función con data.frame como argumento
train_data <- generate_random_prediction_prob(train_data)

# Función que clasifica de forma aleatoria a partir de la columna prediction_prob
random_classifier <- function(data) {
  data$prediction_class <- ifelse(data$prediction_prob > 0.5, 1, 0)
  return(data)
}

# Cargar el archivo "arbolado-mendoza-dataset-validation.csv" como un data.frame
validation_data <- read.csv("data/arbolado-mendoza-dataset-validation.csv")

# Llama a la función creada con data.frame como argumento
validation_data <- generate_random_prediction_prob(validation_data)

# Aplicar la función random_classifier al data.frame validation_data
validation_data <- random_classifier(validation_data)

head(validation_data)

# Función para calcular la matriz de confusión
calculate_confusion_matrix <- function(actual, predicted) {
  TP <- sum(actual == 1 & predicted == 1)
  TN <- sum(actual == 0 & predicted == 0)
  FP <- sum(actual == 0 & predicted == 1)
  FN <- sum(actual == 1 & predicted == 0)
  
  confusion_matrix <- data.frame(TP = TP, TN = TN, FP = FP, FN = FN)
  
  return(confusion_matrix)
}

# Utilizar funcion para calcular la matriz de confusion
confusion_matrix <- calculate_confusion_matrix(validation_data$inclinacion_peligrosa, validation_data$prediction_class)

# Ver la matriz de confusión
print(confusion_matrix)


# Definición de la función biggerclass_classifier
biggerclass_classifier <- function(data) {
  # Calcular la clase mayoritaria
  majority_class <- ifelse(sum(data$inclinacion_peligrosa == "si") > sum(data$inclinacion_peligrosa == "no"), 1, 0)
  
  # Asignar la clase mayoritaria a la columna prediction_class
  data$prediction_class <- majority_class
  
  return(data)
}

# Llamar a la función biggerclass_classifier con data.frame como argumento
validation_data <- biggerclass_classifier(validation_data)

# Utilizar la función para calcular la matriz de confusión con validation data
confusion_matrix <- calculate_confusion_matrix(validation_data$inclinacion_peligrosa, validation_data$prediction_class)

# Imprimir la matriz de confusión
print(confusion_matrix)


# Función para calcular Accuracy
calculate_accuracy <- function(confusion_matrix) {
  accuracy <- (confusion_matrix$TP + confusion_matrix$TN) / (confusion_matrix$TP + confusion_matrix$TN + confusion_matrix$FP + confusion_matrix$FN)
  return(accuracy)
}

# Función para calcular Precision
calculate_precision <- function(confusion_matrix) {
  precision <- confusion_matrix$TP / (confusion_matrix$TP + confusion_matrix$FP)
  return(precision)
}

# Función para calcular Sensitivity
calculate_sensitivity <- function(confusion_matrix) {
  sensitivity <- confusion_matrix$TP / (confusion_matrix$TP + confusion_matrix$FN)
  return(sensitivity)
}

# Función para calcular Specificity
calculate_specificity <- function(confusion_matrix) {
  specificity <- confusion_matrix$TN / (confusion_matrix$TN + confusion_matrix$FP)
  return(specificity)
}

# Función para calcular Negative Predicted Value
calculate_negative_predicted <- function(confusion_matrix) {
  negative_predicted <- confusion_matrix$TN / (confusion_matrix$TN + confusion_matrix$FN)
  return(negative_predicted)
}

# Función para crear folds
create_folds <- function(df, k) {
  shuffled_data = df[sample(1:nrow(df)), ] 
  
  # Calcular el tamaño de cada fold

  fold_size <- nrow(shuffled_data) %/% k
  fold_sizes <- rep(fold_size, k)
  
  # Ajustar el tamaño de los folds
  remaining_rows <- nrow(shuffled_data) %% k
  fold_sizes[1:remaining_rows] <- fold_sizes[1:remaining_rows] + 1
  
  # Crear los folds
  folds <- split(shuffled_data, rep(1:k, fold_sizes))
  
  # Convertir los folds en una lista
  fold_list <- as.list(folds)
  
  return(fold_list)
}

# Definir la función cross_validation
cross_validation <- function(df, k) {
  folded_data <- create_folds(df, k)
  
  result <- data.frame(
    Accuracy = numeric(),
    Precision = numeric(),
    Sensitivity = numeric(),
    Specificity = numeric()
  )
  for (i in 1:length(folded_data)) {
    validation_set <- folded_data[[i]]
    trainings_sets <- folded_data[-i]
    
    training_df <- do.call(rbind, trainings_sets)
    train_formula <- formula(inclinacion_peligrosa ~ altura + diametro_tronco)
    tree_model <- rpart(train_formula, data = training_df)
    p <- predict(tree_model, validation_set, type = "class")
    
    true_labels <- validation_set$inclinacion_peligrosa
    confusion_matrix <- calculate_confusion_matrix(true_labels, p)
    
    accuracy <- calculate_accuracy(confusion_matrix)
    precision <- calculate_precision(confusion_matrix)
    sensitivity <- calculate_sensitivity(confusion_matrix)
    specificity <- calculate_specificity(confusion_matrix)
    
    row_metrics <- data.frame(
      Accuracy = accuracy,
      Precision = precision,
      Sensitivity = sensitivity,
      Specificity = specificity
    )
    
    result <- rbind(result, row_metrics)
  }
  
  print(result)
  return(result)
}

# Cargar el archivo "arbolado-mendoza-dataset-validation.csv" como un data.frame
data <- read_csv("./data/arbolado-mendoza-dataset-validation.csv")
data$inclinacion_peligrosa = as.factor(data$inclinacion_peligrosa)

# Llamar a la función cross_validation con data.frame como argumento
result_df <- cross_validation(data, 10)
result_df

# Calcular la desviación estándar de cada columna
std_dev <- apply(data, 2, sd, na.rm = TRUE)

# Crear un nuevo dataframe con las medias y desviaciones estándar
summary_data <- data.frame(
  Metrica = c("Accuracy", "Precision", "Sensitivity", "Specificity"),
  Media = means,
  Desviacion_Estandar = std_dev
)

# Imprimir el dataframe
summary_data

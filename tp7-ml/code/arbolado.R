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





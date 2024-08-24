# *Análisis del Desbalance de Clases en la Predicción de Severidad de Accidentes*

Este proyecto analiza cómo la falta de datos en ciertas clases impacta el rendimiento de los modelos de clasificación, 
específicamente en la predicción de la severidad de accidentes de tráfico. Se entrenó un modelo de clasificación para predecir la severidad de los accidentes, categorizada en cuatro niveles.

## Resumen de resultados
El modelo mostró un claro sesgo hacia la clase mayoritaria (Severidad 2), logrando alta precisión y recall en esta categoría. 
Sin embargo, su rendimiento en las clases menos representadas (Severidad 1, 3 y 4) fue significativamente menor. Esto sugiere que el desbalance de clases, 
junto con el uso de una muestra limitada de datos para el entrenamiento, afectó la capacidad del modelo para generalizar correctamente en las clases minoritarias.

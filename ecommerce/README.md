# *Prediccion del tiempo de envio*

El dataset original cuenta con datos para entrenamiento y testeo, para este ejemplo se tomaron unicamente aquellos de la carpeta /train debido a que en /test hacen falta columnas relevantes para el tema a tratar.

Se entrena un modelo de Random Forest para predecir el tiempo de envio de una orden (en horas), los metricas de evaluacion finales del modelo son:

  - MAE: 2.3597167172806426

  - RMSE: 21.89904009541277

Que como se puede apreciar en la grafica de dispersion al final del notebook, en general predice bien los tiempos de entrega con un error promedio aproximado de 2.36 horas, pero cuando hay errores en la prediccion
estas suelen ser grandes.

Para mejorar esa precision se podria intentar mejorar el modelo ajustando hiperparametros, seleccionando otras caracteristicas, o probando con modelos más complejos.

import pandas as pd

# Leer solo una parte del archivo, las primeras 500,000 filas
lines = 250000
ruta = '../../data/US_Accidents_March23.csv'
df_subset = pd.read_csv(ruta, nrows=lines)

# Guardar este subset en un nuevo archivo CSV
df_subset.to_csv('data/accidentes_reducido.csv', index=False)


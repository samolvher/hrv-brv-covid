import numpy as np
import pandas as pd
from scipy.stats import norm

# Función para aplicar la transformación de Fisher Z
def fisher_z_transform(r):
    r = np.clip(r, -0.9999, 0.9999)
    return 0.5 * np.log((1 + r) / (1 - r))

# Cargar las matrices de correlación de los dos grupos (archivos CSV)
grupo_A = pd.read_csv("correlacion_pearson_A.csv", index_col=0)
grupo_B = pd.read_csv("correlacion_pearson_B.csv", index_col=0)

# Tamaños de muestra de cada grupo
n_A = 15  # Número de sujetos en Grupo A
n_B = 9  # Número de sujetos en Grupo B

# Aplicar transformación Fisher Z a ambas matrices
Z_A = grupo_A.applymap(fisher_z_transform)
Z_B = grupo_B.applymap(fisher_z_transform)

# Calcular la matriz de valores Z de la prueba de diferencia
Z_diff = (Z_A - Z_B) / np.sqrt((1 / (n_A - 3)) + (1 / (n_B - 3)))

# Calcular los p-valores
p_values = 2 * (1 - norm.cdf(np.abs(Z_diff)))  # Prueba bilateral

# Convertir en DataFrame antes de guardar
Z_diff_df = pd.DataFrame(Z_diff, index=grupo_A.index, columns=grupo_A.columns)
p_values_df = pd.DataFrame(p_values, index=grupo_A.index, columns=grupo_A.columns)

# Guardar los resultados en archivos CSV
Z_diff_df.to_csv("matriz_Z_fisher.csv")
p_values_df.to_csv("matriz_p_values.csv")

# Mostrar las primeras filas como vista previa
print("Matriz de valores Z de Fisher:")
print(Z_diff_df.head())
print("\nMatriz de p-valores:")
print(p_values_df.head())


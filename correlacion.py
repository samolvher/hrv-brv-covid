import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('archivo_de_variables-b.csv') 

#Columnas a analizar
columns = ["Mean_RR_HRV", "Mean_HR_HRV", "SDNNN_HRV", "RMSSD_HRV", "pNN50_HRV",
           "Frec_Picos_HRV", "Poder_nu_HRV", "Mean_RR_BRV", "Mean_HR_BRV",
           "SDNNN_BRV", "RMSSD_BRV", "pNN50_BRV", "Frec_Picos_BRV", "Poder_nu_BRV",
           "Puntaje"]

#Filtrar solo columnas numéricas
df = df[columns].apply(pd.to_numeric, errors='coerce').dropna()

#Función para calcular Pearson, p-valor y error estándar
def pearson_corr(x, y):
    r, p = stats.pearsonr(x, y)  # Correlación y p-valor
    stderr = np.sqrt((1 - r**2) / (len(x) - 2))  # Error estándar
    return r, p, stderr

#Crear matrices vacías para guardar resultados
corr_matrix = pd.DataFrame(index=columns, columns=columns)
pval_matrix = pd.DataFrame(index=columns, columns=columns)
stderr_matrix = pd.DataFrame(index=columns, columns=columns)
combined_matrix = pd.DataFrame(index=columns, columns=columns)  # Matriz combinada

#Calcular correlación, p-valor y error estándar para cada par de variables
for col1 in columns:
    for col2 in columns:
        if col1 == col2:
            corr_matrix.loc[col1, col2] = 1  # Autocorrelación = 1
            pval_matrix.loc[col1, col2] = 0  # p-valor no aplica
            stderr_matrix.loc[col1, col2] = 0  # Error estándar no aplica
            combined_matrix.loc[col1, col2] = "1.000 (p=0, e=0)"
        else:
            df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
            r, p, stderr = pearson_corr(df[col1], df[col2])
            corr_matrix.loc[col1, col2] = r
            pval_matrix.loc[col1, col2] = p
            stderr_matrix.loc[col1, col2] = stderr
            combined_matrix.loc[col1, col2] = f"{r:.3f} (p={p:.3g}, e={stderr:.3f})"

#Guardar resultados en CSV
corr_matrix.to_csv("correlacion_pearson_B.csv")
pval_matrix.to_csv("pvalores_pearson_B.csv")
stderr_matrix.to_csv("error_std_pearson_B.csv")
combined_matrix.to_csv("matriz_completa_pearson_B.csv")  # Matriz combinada con todo

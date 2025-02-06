from scipy.io import loadmat
import pandas as pd
import os

nombre_csv_final = "nombre_archivo_final" #indicar nombre de archivo final
directorio = 'directorio/grupos/grupo_b' #indicar directorio donde se encuentran archivos .mat

archivos = os.listdir(directorio)

#realiza un csv por una señal del participante

for archivo in archivos:
    if os.path.splitext(archivo)[1] == ".mat":
        archivo = os.path.splitext(archivo)[0]
        data = loadmat(f"{directorio}/{archivo}.mat")
        df = pd.DataFrame(data["data"])
        df.to_csv(f"csv_files/{archivo}.csv", index = False, header = False, columns = [1]) #0 para ECG, 1 para respiracion, correspondiente a la columna

#conjunta la señal de todos los participantes en un solo csv

#busca los csv dentro de la carpeta csv_files
directorio = "csv_files"
files = [os.path.join(directorio, file) for file in os.listdir(directorio) if '.csv' in file]

#recorta los registros largos conforme al registro mas corto, para que haya una normalizacion
ecgs = list(map(pd.read_csv, files))
registro_min = min(len(ecg) for ecg in ecgs) #guarda el n° de registro más corto
registros_recortados = [ecg[:registro_min] for ecg in ecgs]

#concatena los registros de todos los participantes en un solo CSV de forma horizaontal, donde columna1 = participante1, columna2 = participante2,..., columnaN = participanteN
df = pd.concat(registros_recortados, axis = 1)
df.to_csv(f"{nombre_csv_final}.csv", index = False, header = False)

#Elimina los csv individuales de cada participante (de la señal señalada)
archivos = os.listdir('csv_files')
for archivo in archivos:
    if os.path.splitext(archivo)[1] == ".csv":
        os.remove(f"csv_files/{archivo}")
# Análisis y Comparación de Señales de ECG y Ciclos Respiratorios

Scripts de Python utilizados para el análisis de datos y señales del Proyecto Terminal "Diferencias cognitivas y psicofisiológicas a largo plazo en sujetos que estuvieron infectados por SARS-CoV2 antes y después de ser vacunados" adherido al Departamento de Ciencias de la Salud de la Universidad Autónoma Metropolitana Unidad Lerma.

### Librerías requeridas

 - Numpy
 - Pandas
 - Scipy
 - Pyplot

A continuación se indican la funcionalidad por cada archivo.


## convert_mat2csv

Este archivo ayuda a convertir cada archivo .mat (obtenido del registro de las señales con el equipo BIOPAC MP36) de cada participante por 2 csv, cada csv respectivo a un tipo de señal (ECG/Frecuencia Respiratoria), donde cada columna representa un participante. 

## uni_analysis

El script muestra el ECG o ciclo respiratorio (según coloques el CSV) e identifica los picos RR de ECG y el pico en las crestas del ciclo respiratorio según los parámetros que se ingresen en la función de *find_peaks*, para posteriormente mostrar el tacograma de variabilidad de frecuencia (diferencia entre picos). Esto lo realiza por cada participante, por lo que hay que indicar la columna a analizar/mostrar.

## correlacion

Una vez obtenidas las variables del dominio de tiempo y frecuencia de los tacograma y reunidas en un solo archivo CSV, se procede a realizar la correlación entre variables, dicha correlación se hace con el coeficiente de Pearson juntos con sus p-valor y error estándar. En el proyecto presente se tiene 15 variables (7 de ECG, 7 de frecuencia respiratoria, y una de la evaluación neuropsicológica), creando finalmente una matriz de correlación de 15x15, junto las matrices de p-valores y errores estándar.

## fisher

Una vez obtenida las matrices de correlación por cada grupo, se realiza la transformada de Fisher y su p-valor para encontrar el nivel de diferencias entre grupos y su significancia dado los p-valores. Creando finalmente 2 matrices, una matriz de valores Z (que muestra las diferencias entre grupos), y otra matriz de valores p.


from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt

archivo = "nombre_archivo_seniales"

datos = np.loadtxt(f"{archivo}.csv", delimiter=',')

Fs = 2000 #frecuencia de muestreo
tiempo = np.arange(0, len(datos)) / Fs #vector de tiempo

volt1, loc1 = find_peaks(datos[:, 0], height=-0.2, distance=1000) #ECG: h=0.2, d=1000 frecResp: 0.075 3200

#creacion de figura Picos 
plt.figure()

#subplot
plt.subplot(2, 1, 1) 
plt.plot(tiempo, datos[:, 0], linewidth=1.3) 
plt.plot(tiempo[volt1], loc1["peak_heights"], "*", linewidth=1.3)
plt.title('Titulo gráfica de señales') 
plt.xlabel('Tiempo [s]') 
plt.ylabel('Amplitud [mV]') 
plt.grid(True) 

#plt.show()

HRV_y1 = np.diff(volt1/Fs) #variacion de frecuencia 
HRV_x1 = np.cumsum(HRV_y1)


#creacion de figura HVR/RRV
plt.figure()

#subplot
plt.subplot(2, 1, 1) 
plt.plot(HRV_x1, HRV_y1*1000, "o-", label="Original", linewidth=1.3)
plt.title('Titulo de Tacograma') 
plt.xlabel('Tiempo [s]') 
plt.ylabel('Diferencia Picos [ms]') 
plt.grid(True) 

plt.show()



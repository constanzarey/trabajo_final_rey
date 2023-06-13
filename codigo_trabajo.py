#import library.
import scipy.stats as ss
import statsmodels.stats.power as smp
import numpy as np
from statsmodels.stats.power import TTestIndPower
import pandas as pd
import matplotlib.pyplot as plt


#%% FILTRADO DE DATOS DEL DATASET
path = './Peso_seco.xlsx'
datos = pd.read_excel(path, sheet_name = 'Hoja4')
#print(datos)
datos_final = datos.dropna()
filtrado = datos_final[datos_final['Estante']== 'Estante1']
#print(filtrado)

#%% ¿COMO SE DISTRIBUYEN LOS DATOS?
#visualizar como se distribuyen los datos.
peso_seco = datos_final['Peso seco'].dropna()
plt.hist(peso_seco, bins=50)  
plt.title('Histograma de peso seco')  # Título del histograma
plt.xlabel('Peso seco (mg/planta)')  # Etiqueta del eje x
plt.ylabel('Frecuencia')
plt.show()

descripcion = datos_final.describe()
print(descripcion)


#%% EVALUAR ASIMETRIA Y CURTOSIS DE LA DISTRIBUCION.
#Para eso se calcula el valor de los coeficientes que determinan la asimetria y curtosis de la distribucion.
#ASIMETRIA

skewness = peso_seco.skew(axis=0, skipna=True, numeric_only=False)
print(skewness)
#2.027382050998325
#Un coeficiente de asimetria de Fisher mayor a cero indica asimetria positiva.

kurtosis = peso_seco.kurt(axis=0, skipna=True, numeric_only=False)
print(kurtosis)
#7.103412786645373
#Un coeficiente de curtosis menor a 0 indica que el histograma tiende a un gran apuntamiento alrededor del valor central, lo que corresponde a una distribución leptocurtica.

#%% ESTIMACION DE INTERVALOS DE CONFIANZA.

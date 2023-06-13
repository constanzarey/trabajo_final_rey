#import library.
import scipy.stats as ss
import statsmodels.stats.power as smp
import numpy as np
from statsmodels.stats.power import TTestIndPower
import pandas as pd
import matplotlib.pyplot as plt


#%% FILTRADO DE DATOS DEL DATASET
path = './Peso_seco.xlsx'
datos = pd.read_excel(path, sheet_name = 'Hoja3')
#print(datos)
datos_final = datos.dropna()
filtrado = datos_final[datos_final['Estante']== 'Estante1']
#print(filtrado)

#%% ¿COMO SE DISTRIBUYEN LOS DATOS?
#visualizar como se distribuyen los datos.
peso_seco = datos_final['Peso seco'].dropna()
plt.hist(peso_seco, bins=10)  
plt.title('Histograma de peso seco')  # Título del histograma
plt.xlabel('Peso seco (gr/planta)')  # Etiqueta del eje x
plt.ylabel('Frecuencia')
plt.show()

#%% EVALUAR ASIMETRIA Y CURTOSIS DE LA DISTRIBUCION.
#Para eso se calcula el valor de los coeficientes que determinan la asimetria y curtosis de la distribucion.
#ASIMETRIA

skewness = peso_seco.skew(axis=0, skipna=True, numeric_only=False)
print(skewness)
#0.1745536156801608
#Un coeficiente de asimetria de Fisher mayor a cero indica asimetria positiva.

kurtosis = peso_seco.kurt(axis=0, skipna=True, numeric_only=False)
print(kurtosis)
#-0.7593116032768186
#Un coeficiente de curtosis menor a 0 indica que el histograma tiende a ser aplanado, lo que corresponde a una distribución platicúrtica.
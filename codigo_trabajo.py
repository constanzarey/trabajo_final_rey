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
#print(filtrado)

#%% ¿COMO SE DISTRIBUYEN LOS DATOS? MEDIDAS CARACTERISTICAS DE UNA DISTRIBUCION.
#visualizar como se distribuyen los datos totales.
peso_seco = datos_final['Peso seco'].dropna()
plt.hist(peso_seco, bins=50)  
plt.title('Histograma de peso seco total')  # Título del histograma
plt.xlabel('Peso seco (mg/planta)')  # Etiqueta del eje x
plt.ylabel('Frecuencia')
plt.show()

#Descripcion de los datos totales.

descripcion_estadistica = peso_seco.describe()

control = datos_final[datos_final['Tratamiento']== 'control']
gfp = datos_final[datos_final['Tratamiento']== '2011 GFP']
AK21 = datos_final[datos_final['Tratamiento']== 'AK21']
AK83 = datos_final[datos_final['Tratamiento']== 'AK83']
B401 = datos_final[datos_final['Tratamiento']== 'B401']
SmaAK21 = datos_final[datos_final['Tratamiento']== 'SmaAK21']
SmaAK83 = datos_final[datos_final['Tratamiento']== 'SmaAK83']
SmaB401 = datos_final[datos_final['Tratamiento']== 'SmaB401']


#Evaluacion de parametros de centralizacion de la distribucion.
#MEDIA
media_control = control.mean(numeric_only=True)
#7.936364
media_gfp = gfp.mean(numeric_only=True)
#38.7125
media_AK21 = AK21.mean(numeric_only=True)
#35.629167
media_AK83 = AK83.mean(numeric_only=True)
#19.354167
media_B401 = B401.mean(numeric_only=True)
#29.273913
media_SmaAK21 = SmaAK21.mean(numeric_only=True)
#35.629167
media_SmaAK83 = SmaAK83.mean(numeric_only=True)
#19.354167
media_SmaB401 = SmaB401.mean(numeric_only=True)
#29.273913



#Evaluacion de la mediana de los datos para cada condicion.

mediana_control = control.median(numeric_only=True)
#8.4
mediana_gfp = gfp.median(numeric_only=True)
#38.4
mediana_AK21 = AK21.median(numeric_only=True)
#33.8
mediana_AK83 = AK83.median(numeric_only=True)
#19.4
mediana_B401 = B401.median(numeric_only=True)
#25.1
mediana_SmaAK21 = SmaAK21.median(numeric_only=True)
#33.8
mediana_SmaAK83 = SmaAK83.median(numeric_only=True)
#19.4
mediana_SmaB401 = SmaB401.median(numeric_only=True)
#25.1


#Evaluacion de la moda de los datos para cada condicion.
#chequear si me anda
moda_control = control.mode(numeric_only=True)
moda_gfp = gfp.mode(numeric_only=True)
moda_AK21 = AK21.mode(numeric_only=True)
moda_AK83 = AK83.mode(numeric_only=True)
moda_B401 = B401.mode(numeric_only=True)
moda_SmaAK21 = SmaAK21.mode(numeric_only=True)
moda_SmaAK83 = SmaAK83.mode(numeric_only=True)
moda_SmaB401 = SmaB401.mode(numeric_only=True)

#Parametros de dispersion.

ri_total = peso_seco.quantile(0.75) - peso_seco.quantile(0.25)
#print(ri_total)
#24.799999999999997 (especifica el rango de valores)

ri_control = control.quantile(0.75, numeric_only = True) - control.quantile(0.25, numeric_only = True)
#print(ri_control)
#3.5
ri_gfp = gfp.quantile(0.75, numeric_only = True) - gfp.quantile(0.25, numeric_only = True)
#print(ri_gfp)
#25.6


#%% EVALUAR ASIMETRIA Y CURTOSIS DE LA DISTRIBUCION
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

#%% ESTIMACION DE INTERVALOS DE CONFIANZA



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

control = datos_final[datos_final['Tratamiento']== 'control']
gfp = datos_final[datos_final['Tratamiento']== '2011 GFP']
AK21 = datos_final[datos_final['Tratamiento']== 'AK21']
AK83 = datos_final[datos_final['Tratamiento']== 'AK83']
B401 = datos_final[datos_final['Tratamiento']== 'B401']
SmaAK21 = datos_final[datos_final['Tratamiento']== 'SmaAK21']
SmaAK83 = datos_final[datos_final['Tratamiento']== 'SmaAK83']
SmaB401 = datos_final[datos_final['Tratamiento']== 'SmaB401']

#medias

media_control = control.mean()
media_gfp = gfp.mean()
media_AK21 = AK21.mean()
media_AK83 = AK83.mean()
media_B401 = B401.mean()
media_SmaAK21 = SmaAK21.mean()
media_SmaAK83 = SmaAK83.mean()
media_SmaB401 = SmaB401.mean()

print('La media del peso seco del control es:', media_control, 
      'La media del peso seco de las muestras inoculadas con 2011GFP es:' , media_gfp,
      'La media del peso seco de las muestras inoculadas con AK21 es:', media_AK21,
      'La media del peso seco de las muestras inoculadas con AK83 es', media_AK83,
      'La media del peso seco de las muestras inoculadas con B401 es', media_B401,
      'La media del peso seco de las muestras inoculadas con Sma(AK21) es:' ,media_AK21,
      'La media del peso seco de las muestras inoculadas con Sma(AK83) es:', media_AK83,
      'La media del peso seco de las muestras inoculadas con Sma(B401) es:', media_B401
      )



#%% EVALUAR ASIMETRIA Y CURTOSIS DE LA DISTRIBUCION.control = datos_final[datos_final['Tratamiento']== 'control']
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

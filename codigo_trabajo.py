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
#plt.show()

#Descripcion de los datos totales.

descripcion_estadistica = peso_seco.describe()

control = datos_final[datos_final['Tratamiento']== 'control']
gfp = datos_final[datos_final['Tratamiento']== '2011 GFP']
AK21 = datos_final[datos_final['Tratamiento']== 'AK21']
AK83 = datos_final[datos_final['Tratamiento']== 'AK83']
B401 = datos_final[datos_final['Tratamiento']== 'B401']
SmaAK21 = datos_final[datos_final['Tratamiento']== 'Sma(AK21)']
SmaAK83 = datos_final[datos_final['Tratamiento']== 'Sma(AK83)']
SmaB401 = datos_final[datos_final['Tratamiento']== 'Sma(B401)']


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
#35.211111
media_SmaAK83 = SmaAK83.mean(numeric_only=True)
#45.538095
media_SmaB401 = SmaB401.mean(numeric_only=True)
#45.631818


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
#27.1
mediana_SmaAK83 = SmaAK83.median(numeric_only=True)
#26.2
mediana_SmaB401 = SmaB401.median(numeric_only=True)
#39.65


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
#24.799999999999997 (especifica el rango de valores)

ri_control = control.quantile(0.75, numeric_only = True) - control.quantile(0.25, numeric_only = True)
#3.5
ri_gfp = gfp.quantile(0.75, numeric_only = True) - gfp.quantile(0.25, numeric_only = True)
#25.6
ri_AK21 = AK21.quantile(0.75, numeric_only = True) - AK21.quantile(0.25, numeric_only = True)
#19.025
ri_AK83 = AK83.quantile(0.75, numeric_only = True) - AK83.quantile(0.25, numeric_only = True)
#7.525
ri_B401 = B401.quantile(0.75, numeric_only = True) - B401.quantile(0.25, numeric_only = True)
#16.35
ri_SmaAK21 = SmaAK21.quantile(0.75, numeric_only = True) - SmaAK21.quantile(0.25, numeric_only = True)
#24.65
ri_SmaAK83 = SmaAK83.quantile(0.75, numeric_only = True) - SmaAK83.quantile(0.25, numeric_only = True)
#51.5
ri_SmaB401 = SmaB401.quantile(0.75, numeric_only = True) - SmaB401.quantile(0.25, numeric_only = True)
#26.725


#DESVIACION TIPICA
desv_total = peso_seco.std(axis=None)
#print(desv_total)
#23.88598342973365

desv_control = control.std(axis=None, numeric_only=True)
desv_gfp = gfp.std(axis=None, numeric_only= True)
desv_AK21 = AK21.std(axis=None, numeric_only=True)
desv_AK83 = AK83.std(axis=None,  numeric_only=True)
desv_B401 = B401.std(axis=None,  numeric_only=True)
desv_SmaAK21 = SmaAK21.std(axis=None,  numeric_only=True)
desv_SmaAK83 = SmaAK83.std(axis=None,  numeric_only=True)
desv_SmaB401 = SmaB401.std(axis=None,  numeric_only=True)

#print([desv_control, desv_gfp, desv_AK21, desv_AK83, desv_B401, desv_SmaAK21, desv_SmaAK83, desv_SmaB401])
#[2.26958, 16.434463, 16.916405, 6.067446, 14.853381, 23.23896, 41.03822, 25.120062]

#VARIANZA.

var_total = peso_seco.var(axis=None)
#print(var_total)
#570?????

var_control = control.var(axis=None, numeric_only=True)
var_gfp = gfp.var(axis=None, numeric_only= True)
var_AK21 = AK21.var(axis=None, numeric_only=True)
var_AK83 = AK83.var(axis=None,  numeric_only=True)
var_B401 = B401.var(axis=None,  numeric_only=True)
var_SmaAK21 = SmaAK21.var(axis=None,  numeric_only=True)
var_SmaAK83 = SmaAK83.var(axis=None,  numeric_only=True)
var_SmaB401 = SmaB401.var(axis=None,  numeric_only=True)

#print([var_control, var_gfp, var_AK21, var_AK83, var_B401, var_SmaAK21, var_SmaAK83, var_SmaB401])
#[5.150996, 270.091576, 286.164764, 36.813895, 220.622925, 540.049281, 1684.135476, 631.017511]

    # ''' Como no conozco la varianza poblacional y el n es menor a 30, uso dist t de student'''
     #se utilizará la distribución t de student porque no conocemos la varianza poblacional y el n<30

     #Se calcula como:

     #Intervalo de confianza = x +/- t * (s / √n)

'''¿Los datos se distribuyen de manera normal? Para responder utilizo el test de normalidad.
 Planteo dos hipotesis:
 -H0: los datos se distribuyen normalmente.
 -H1:los datos no se distribuyen normalmente.'''

print(ss.normaltest(peso_seco, axis=0, nan_policy='propagate'))
#NormaltestResult(statistic=94.3678816604075, pvalue=3.2231080362482276e-21)}
#el p-valor es menor a 0.05, por lo tanto rechazo la H0 y acepto la hipotesis alternativa, es decir que los datos no se distribuyen de manera normal.

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



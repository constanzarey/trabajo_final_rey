#import library.
import scipy.stats as ss
import statsmodels.stats.power as smp
import numpy as np
from statsmodels.stats.power import TTestIndPower
from statsmodels.stats.power import tt_ind_solve_power
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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
SmaAK21 = datos_final[datos_final['Tratamiento']== 'Sma(AK21)']
SmaAK83 = datos_final[datos_final['Tratamiento']== 'Sma(AK83)']
SmaB401 = datos_final[datos_final['Tratamiento']== 'Sma(B401)']


#Evaluacion de parametros de centralizacion de la distribucion.
#MEDIA
media_peso_total = datos_final.mean(numeric_only=True)
#31.96
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

print('La media del peso seco total es:', media_peso_total,
      'La media del peso seco para el tratamiento control el:', media_control,
      'La media del peso seco para el tratamiento gfp:', media_gfp,
      'La media del peso seco para el tratamiento AK21 es:', media_AK21,
      'La media del peso seco para el tratamiento AK83:', media_AK83,
      'La media del peso seco para el tratamiento B401 es:', media_B401,
      'La media del peso seco para el tratamiento SmaAK21 es:', media_SmaAK21,
      'La media del peso seco para el tratamiento SmaAK83 es:', media_SmaAK83,
      'La media del peso seco para el tratamiento SmaB401 es:', media_SmaB401)



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
#print('La mediana del peso seco para el tratamiento control es:')


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

desv_total = datos_final.std(axis=None, numeric_only=True)
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
#570

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
#En este caso, podemos calcular el IC de los datos totales con distribucion normal ya que el n > 30. 
#se calcula como:
#IC = x+/- t * (s/√n )
#loc es el promedio de los datos
#scale es el desvio estandar.


ic_95_datos_total = ss.norm.interval(confidence= 0.95, loc= media_peso_total, scale = ss.sem(peso_seco))
#(array([28.46068031]), array([35.47864554]))

#Para el resto de los datos correspondiente a cada tratamiento, asumi distribucion t de student dado que el n es menor a 30 y la varianza poblacional es desconocida.
ic_95_datos_control = ss.t.interval(confidence= 0.95, df= len(control['Peso seco'].index) -1, loc = media_control, scale = ss.sem(control['Peso seco']))
ic_95_datos_gfp = ss.t.interval(confidence= 0.95, df= len(gfp['Peso seco'].index) -1, loc= media_gfp, scale = ss.sem(gfp['Peso seco']))
ic_95_datos_AK21 = ss.t.interval(confidence= 0.95, df= len(AK21['Peso seco'].index) -1, loc= media_AK21, scale = ss.sem(AK21['Peso seco']))
ic_95_datos_AK83 = ss.t.interval(confidence= 0.95, df= len(AK83['Peso seco'].index) -1, loc= media_AK83, scale = ss.sem(AK83['Peso seco']))
ic_95_datos_B401 = ss.t.interval(confidence= 0.95, df= len(B401['Peso seco'].index) -1, loc= media_B401, scale = ss.sem(B401['Peso seco']))
ic_95_datos_SmaAK21 = ss.t.interval(confidence= 0.95, df= len(SmaAK21['Peso seco'].index) -1, loc= media_SmaAK21, scale = ss.sem(SmaAK21['Peso seco']))
ic_95_datos_SmaAK83 = ss.t.interval(confidence= 0.95, df= len(SmaAK83['Peso seco'].index) -1, loc= media_SmaAK83, scale = ss.sem(SmaAK83['Peso seco']))
ic_95_datos_SmaB401 = ss.t.interval(confidence= 0.95, df= len(SmaB401['Peso seco'].index) -1, loc= media_SmaB401, scale = ss.sem(SmaB401['Peso seco']))

#print('El intervalo de confianza para los datos de peso seco del tratamiento control es:[', np.min(ic_95_datos_control), np.max(ic_95_datos_control),']')
#print('El intervalo de confianza para los datos de peso seco del tratamiento gfp es:[', np.min(ic_95_datos_gfp), np.max(ic_95_datos_gfp),']')
#print('El intervalo de confianza para los datos de peso seco del tratamiento AK21 es:[', np.min(ic_95_datos_AK21), np.max(ic_95_datos_AK21),']')
#print('El intervalo de confianza para los datos de peso seco del tratamiento AK83 es:[', np.min(ic_95_datos_AK83), np.max(ic_95_datos_AK83),']')
#print('El intervalo de confianza para los datos de peso seco del tratamiento B401 es:[', np.min(ic_95_datos_B401), np.max(ic_95_datos_B401),']')
#print('El intervalo de confianza para los datos de peso seco del tratamiento SmaAK21 es:[', np.min(ic_95_datos_SmaAK21), np.max(ic_95_datos_SmaAK21),']')
#print('El intervalo de confianza para los datos de peso seco del tratamiento SmaAK83 es:[', np.min(ic_95_datos_SmaAK83), np.max(ic_95_datos_SmaAK83),']')
#print('El intervalo de confianza para los datos de peso seco del tratamiento SmaB401 es:[', np.min(ic_95_datos_SmaB401), np.max(ic_95_datos_SmaB401),']')

'''
El intervalo de confianza para los datos de peso seco del tratamiento control es:[ 6.930088013333918 8.942639259393355 ]
El intervalo de confianza para los datos de peso seco del tratamiento gfp es:[ 31.772834875167433 45.652165124832564 ]
El intervalo de confianza para los datos de peso seco del tratamiento control es:[ 28.48599522929093 42.77233810404241 ]
El intervalo de confianza para los datos de peso seco del tratamiento control es:[ 16.792109129617586 21.91622420371575 ]
El intervalo de confianza para los datos de peso seco del tratamiento control es:[ 23.654647977328914 46.767574244893304 ]
El intervalo de confianza para los datos de peso seco del tratamiento control es:[ 26.857721593545204 64.21846888264527 ]
El intervalo de confianza para los datos de peso seco del tratamiento control es:[ 34.49420667305269 56.76942969058368 ]
'''

#%%#ESTIMACION DEL TAMAÑO MUESTRAL:
# Utilizo la media y la desviación estándar calculada previamente.
# Defino los parámetros de la prueba
#Tamaño del efecto lo defino como la diferencia entre valores promedio que debo obtener. Seguramente entre el control negativo y positivo este la mayor diferencia.
effect_size_peso = int(abs(media_control - media_gfp) / desv_total)
alpha = 0.05
power = 0.8

# Calcular el tamaño muestral necesario
n_peso = tt_ind_solve_power(effect_size=effect_size_peso, alpha=alpha, power=power, ratio=1.0, alternative='two-sided')
#print("El tamaño muestral requerido es:" , {n_peso})
#Tamaño muestral:16. 



#%%CONTRASTE DE HIPOTESIS.

#VERIFICACION DE SUPUESTOS:
#supuesto de normalidad. Test de normalidad.
'''H0: los datos se distribuyen normalmente.
   H1:los datos no se distribuyen normalmente.'''

print(ss.normaltest(peso_seco, axis=0, nan_policy='propagate'))
#NormaltestResult(statistic=94.3678816604075, pvalue=3.2231080362482276e-21)}
#el p-valor es menor a 0.05, por lo tanto rechazo la H0 y acepto la hipotesis alternativa, es decir que los datos no se distribuyen de manera normal.


lista_control= control['Peso seco'].tolist()
lista_gfp = gfp['Peso seco'].tolist()
lista_AK21 = AK21['Peso seco'].tolist()
lista_AK83 = AK83['Peso seco'].tolist()
lista_B401 = B401['Peso seco'].tolist()
lista_SmaAK21 = SmaAK21['Peso seco'].tolist()
lista_SmaAK83 = SmaAK83['Peso seco'].tolist()
lista_SmaB401 = SmaB401['Peso seco'].tolist()

#supuesto de homocedasticidad de varianzas. Test de Levene.
#H0 = homocedasticidad de varianzas en el peso seco de las muestras es debido al azar.
#H1 = homocedasticidad de varianzas en el peso seco de las muestras no es debido al azar.
print(ss.levene(lista_control, lista_gfp, center='median', proportiontocut=0.05))
#LeveneResult(statistic=32.61406676437943, pvalue=8.962316508662243e-07)


#Como ya una de las comparaciones me da que las varianzas no son similares, tengo que hacer un test no parametrico para comparar los grupos.


#Test no parametrico para comparar mas de tres grupos. Test de Kruskal-Wallis.
'''H0: las diferencias entre las muestras se deben al azar.
   H1:las diferencias entre las muestras no se deben al azar.'''
print(ss.kruskal(control, gfp, AK21, AK83, B401, SmaAK21, SmaAK83, SmaB401, nan_policy= 'propagate', axis=0, keepdims=False))
#KruskalResult(statistic=array([7.58756481e-02, 1.77000000e+02, 7.25729970e+01]), pvalue=array([9.99999112e-01, 8.37571234e-35, 4.45519986e-13]))  
#Dado el valor de pvalue (4e-13), rechazo hipotesis nula y acepto hipotesis alternativas. Existen diferencias significativas entre al menos dos muestras. 


#Para saber cuales de las comparaciones presentan diferencias significativas entre si, realice comparaciones de a pares entre las muestras hasta cubrir todas las combinaciones posibles.
#Planteo dos hipotesis:
'''
-H0: no hay diferencias significativas entre las muestras.
H1: si hay diferencias significatvias entre las muestras.
Aquellos casos donde el pvalue sea menor a 0.05, puedo descartar H0 y aceptar H1.
'''

#FUNCION PARA EVALUAR PVALUE Y GUARDAR AQUELLOS QUE DEN DIFERENCIAS SIGNIFICATIVAS (P-VALUE<0.05).
comparaciones_significativas = []

def select_variables(variables, lista):
    selected_variables = []

    for i, var in enumerate(variables):
        
        #var_name = var[0]  # Nombre de la variable
        var_value = var.pvalue # pvalue de la tupla
        
        if var_value <= 0.05:
            selected_variables.append((lista[i], var_value))
    
    df = pd.DataFrame(selected_variables, columns=['comparacion', 'pvalue'])
    df.set_index(df.index + 1, inplace=True)  # Ajustar el índice según la posición
    return df


#COMPARACIONES PAREADAS ENTRE LAS MUESTRAS:

control_gfp = ss.mannwhitneyu(lista_control, lista_gfp , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
control_AK21 = ss.mannwhitneyu(lista_control, lista_AK21 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
control_AK83 = ss.mannwhitneyu(lista_control, lista_AK83 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
control_B401 = ss.mannwhitneyu(lista_control, lista_B401 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
control_SmaAK21 = ss.mannwhitneyu(lista_control, lista_SmaAK21 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
control_SmaAK83 =ss.mannwhitneyu(lista_control, lista_SmaAK83 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
control_SmaB401 =ss.mannwhitneyu(lista_control, lista_SmaB401 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)

gfp_AK21 = ss.mannwhitneyu(lista_gfp, lista_AK21 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
gfp_AK83 = ss.mannwhitneyu(lista_gfp, lista_AK83 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
gfp_B401 = ss.mannwhitneyu(lista_gfp, lista_B401 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
gfp_SmaAK21 = ss.mannwhitneyu(lista_gfp, lista_SmaAK21 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
gfp_SmaAK83 = ss.mannwhitneyu(lista_gfp, lista_SmaAK83 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
gfp_SmaB401 = ss.mannwhitneyu(lista_gfp, lista_SmaB401 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)

AK21_AK83 = ss.mannwhitneyu(lista_AK21, lista_AK83 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
AK21_B401 = ss.mannwhitneyu(lista_AK21, lista_B401 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
AK21_SmaAK21= ss.mannwhitneyu(lista_AK21, lista_SmaAK21 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
AK21_SmaAK83= ss.mannwhitneyu(lista_AK21, lista_SmaAK83 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
AK21_SmaB401 = ss.mannwhitneyu(lista_AK21, lista_SmaB401 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)

AK83_B401 =  ss.mannwhitneyu(lista_AK83, lista_B401 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
AK83_SmaAK21 = ss.mannwhitneyu(lista_AK83, lista_SmaAK21 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
AK83_SmaAK83 = ss.mannwhitneyu(lista_AK83, lista_SmaAK83 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
AK83_SmaB401 = ss.mannwhitneyu(lista_AK83, lista_SmaB401 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)

B401_SmaAK21 = ss.mannwhitneyu(lista_B401, lista_SmaAK21 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
B401_SmaAK83 = ss.mannwhitneyu(lista_B401, lista_SmaAK83 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
B401_SmaB401 = ss.mannwhitneyu(lista_B401, lista_SmaB401 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)

SmaAK21_SmaAK83 = ss.mannwhitneyu(lista_SmaAK21, lista_SmaAK83 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
SmaAK21_SmaB401 = ss.mannwhitneyu(lista_SmaAK21, lista_SmaB401 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
SmaAK83_SmaB401= ss.mannwhitneyu(lista_SmaAK83, lista_SmaB401 , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)


total = select_variables([control_gfp, control_AK21, control_AK83, control_B401, control_SmaAK21, control_SmaAK83, control_SmaB401, gfp_AK21, gfp_AK83, gfp_B401, gfp_SmaAK21, gfp_SmaAK83, gfp_SmaB401, AK21_AK83, AK21_B401, AK21_SmaAK21, AK21_SmaAK83, AK21_SmaB401, AK83_B401, AK83_SmaAK21, AK83_SmaAK83, AK83_SmaB401, B401_SmaAK21, B401_SmaAK83, B401_SmaB401, SmaAK21_SmaAK83, SmaAK21_SmaB401, SmaAK83_SmaB401], 
                         ['control_gfp', 'control_AK21', 'control_AK83', 'control_B401', 'control_SmaAK21', 'control_SmaAK83', 'control_SmaB401', 'gfp_AK21', 'gfp_AK83', 'gfp_B401', 'gfp_SmaAK21', 'gfp_SmaAK83', 'gfp_SmaB401', 'AK21_AK83', 'AK21_B401', 'AK21_SmaAK21', 'AK21_SmaAK83', 'AK21_SmaB401', 'AK83_B401', 'AK83_SmaAK21', 'AK83_SmaAK83', 'AK83_SmaB401', 'B401_SmaAK21', 'B401_SmaAK83', 'B401_SmaB401','SmaAK21_SmaAK83', 'SmaAK21_SmaB401', 'SmaAK83_SmaB401'])
print(total)

'''
comparacion        pvalue
1       control_gfp  3.608813e-08
2      control_AK21  6.836416e-09
3      control_AK83  2.179180e-08
4      control_B401  1.282650e-08
5   control_SmaAK21  7.859956e-08
6   control_SmaAK83  1.411337e-06
7   control_SmaB401  1.324495e-06
8          gfp_AK83  1.121968e-05
9          gfp_B401  3.605200e-02
10        AK21_AK83  6.600991e-05
11        AK83_B401  8.054759e-03
12     AK83_SmaAK21  9.171183e-03
13     AK83_SmaAK83  1.796990e-02
14     AK83_SmaB401  3.735680e-05
15     B401_SmaB401  1.249955e-02
'''



#%%Realizar un análisis de dependencia de variables categóricas.

#Para eso se construyo tabla de contingencia, con dos columnas: Estante y Peso seco.
#H0: Las variables son independientes.
#H1: las variables no son independientes, es decir, hay relacion entre ellas.

#CONVERSION DE LOS DATOS NUMERICOS DE PESO SECO A DATOS CATEGORICOS, CON PUNTO DE CORTE DE 15MG/PLANTA.
datos_final_peso = list(datos_final['Peso seco'])
lista_2 =[]

for datos in datos_final_peso:
    if datos >= 15.0:
        #print('si')
        lista_2.append('Alto')
    if datos <= 15.0:
        #print('no')
        lista_2.append('Bajo')

#print(lista_2)

datos_final['Peso seco categorico'] = lista_2
print(datos_final)


#construccion de tabla de contingencia.

df2 = datos_final['Peso seco categorico'] + datos_final['Estante']
a= datos_final['Peso seco categorico'] == 'Alto'
b= datos_final['Estante'] == 'Estante1'

groups = df2.groupby([a,b]).count() 
print (groups)

'''Peso seco categorico  Estante
False                 False      21
                      True       23
True                  False      75
                      True       59'''


print(ss.chisquare(groups, ddof=0, axis=0))
#Power_divergenceResult(statistic=102.53932584269663, pvalue=4.420065487234606e-22)
#Dado que el p value es menor a 0.05, puedo rechazar H0 y aceptar que las variables no son independientes.


#%% EVALUACION DE CORRELACION LINEAL ENTRE DOS VARIABLES.

#dado que mi dataset no puede usarse para evaluar correlacion, elegi un segundo dataset para llevar a cabo este ultimo objetivo.


path = './Peso_seco.xlsx'
datos_correlacion = pd.read_excel(path, sheet_name = 'Hoja5')
print(datos_correlacion)

#Para saber que test utilizar, compruebo si los datos se distribuyen normalmente.
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2)

peso_seco_correlacion = datos_correlacion['Peso seco']
peso_nodulos_correlacion = datos_correlacion['Peso nodulos promedio']
ax0.hist(peso_seco_correlacion, bins=25, color= 'green')  
ax0.set_title('Histograma peso seco')
ax1.hist(peso_nodulos_correlacion, bins =25, color= 'red')
ax1.set_title('Histograma peso nodulos promedio')
#plt.title('Histograma de peso seco (dataset2)')  # Título del histograma
#plt.xlabel('Peso)')  # Etiqueta del eje x
#plt.ylabel('Frecuencia')
fig.tight_layout()
plt.show()

plt.scatter(peso_seco_correlacion, peso_nodulos_correlacion)
plt.xlabel('Peso seco')
plt.ylabel('Peso nodulos')
plt.title('Correlacion entre peso seco y peso nodulos')
plt.grid(True)
plt.show()

#En el grafico, parece que no tendrian una correlacion lineal ambas variables. Aun asi, planteo las hipotesis.

#Planteo hipotesis para ver si se cumple normalidad para los dos tipos de datos:
'''
-H0: los datos se distribuyen normalmente.
-H1: los datos no se distribuyen normalmente.'''

print(ss.normaltest(peso_seco_correlacion, axis=0, nan_policy='propagate'))
#NormaltestResult(statistic=10.161384799109037, pvalue=0.006215603844332242)
print(ss.normaltest(peso_nodulos_correlacion, axis=0, nan_policy='propagate'))
#NormaltestResult(statistic=32.788994682394886, pvalue=7.585081842245872e-08)

#segun ambos resultados ambos datos no se distribuyen normalmente.

#Es por eso que utilizo un test no parametrico para evaluar correlacion entre dos variables continuas (Test de correlacion de Spearman)

print(ss.spearmanr(peso_seco_correlacion, peso_nodulos_correlacion))
#SignificanceResult(statistic=0.15548804084084852, pvalue=0.4681458596212671)


#el valor del coeficiente de Spearman dio cercano a 0, por lo tanto, no habria correlacion lineal entre las dos variables. El pvalue indica la significancia del valor.
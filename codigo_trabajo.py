#import library.
import scipy.stats as ss
import statsmodels.stats.power as smp
import numpy as np
from statsmodels.stats.power import TTestIndPower
from statsmodels.stats.power import tt_ind_solve_power
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

#ic_95_datos_total = ss.norm.interval(alpha=0.95, loc= len(datos_final), scale=ss.sem(datos_final))
#print(ic_95_datos_total)






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

result_tukey = ss.tukey_hsd(lista_control, lista_gfp, lista_AK21, lista_AK83, lista_B401, lista_SmaAK21, lista_SmaAK83, lista_SmaB401)
#Deberia hacer un test para identificar cuales son las diferencias entre cada
'''Comparison  Statistic  p-value  Lower CI  Upper CI
 (0 - 1)    -30.776     0.000   -49.767   -11.785    #hay diferencias
 (0 - 2)    -27.693     0.000   -46.684    -8.702    #hay diferencias
 (0 - 3)    -11.418     0.590   -30.409     7.573    
 (0 - 4)    -21.338     0.018   -40.525    -2.150    #hay diferencias
 (0 - 5)    -27.275     0.002   -47.724    -6.826    #hay diferencias
 (0 - 6)    -37.602     0.000   -57.231   -17.972    #hay diferencias
 (0 - 7)    -37.695     0.000   -57.095   -18.296    #hay diferncias
 (1 - 0)     30.776     0.000    11.785    49.767    #hay diferencias
 (1 - 2)      3.083     1.000   -15.491    21.657    
 (1 - 3)     19.358     0.034     0.784    37.932    #hay diferencias
 (1 - 4)      9.439     0.783    -9.336    28.213    
 (1 - 5)      3.501     0.999   -16.561    23.563
 (1 - 6)     -6.826     0.958   -26.051    12.400
 (1 - 7)     -6.919     0.952   -25.911    12.072
 (2 - 0)     27.693     0.000     8.702    46.684    #hay diferencias
 (2 - 1)     -3.083     1.000   -21.657    15.491    
 (2 - 3)     16.275     0.133    -2.299    34.849
 (2 - 4)      6.355     0.968   -12.419    25.130
 (2 - 5)      0.418     1.000   -19.644    20.480
 (2 - 6)     -9.909     0.761   -29.135     9.317
 (2 - 7)    -10.003     0.740   -28.994     8.989
 (3 - 0)     11.418     0.590    -7.573    30.409
 (3 - 1)    -19.358     0.034   -37.932    -0.784   #hay diferencias
 (3 - 2)    -16.275     0.133   -34.849     2.299   
 (3 - 4)     -9.920     0.737   -28.694     8.855
 (3 - 5)    -15.857     0.236   -35.919     4.205
 (3 - 6)    -26.184     0.001   -45.410    -6.958   #hay diferencias
 (3 - 7)    -26.278     0.001   -45.269    -7.286   #hay diferencias
 (4 - 0)     21.338     0.018     2.150    40.525   #hay diferencias
 (4 - 1)     -9.439     0.783   -28.213     9.336
 (4 - 2)     -6.355     0.968   -25.130    12.419
 (4 - 3)      9.920     0.737    -8.855    28.694
 (4 - 5)     -5.937     0.986   -26.185    14.311
 (4 - 6)    -16.264     0.174   -35.684     3.156
 (4 - 7)    -16.358     0.157   -35.546     2.830
 (5 - 0)     27.275     0.002     6.826    47.724    #hay diferencias
 (5 - 1)     -3.501     0.999   -23.563    16.561
 (5 - 2)     -0.418     1.000   -20.480    19.644
 (5 - 3)     15.857     0.236    -4.205    35.919
 (5 - 4)      5.937     0.986   -14.311    26.185
 (5 - 6)    -10.327     0.788   -30.994    10.340
 (5 - 7)    -10.421     0.771   -30.870    10.028
 (6 - 0)     37.602     0.000    17.972    57.231    #hay diferencias
 (6 - 1)      6.826     0.958   -12.400    26.051
 (6 - 2)      9.909     0.761    -9.317    29.135
 (6 - 3)     26.184     0.001     6.958    45.410    #hay diferencias
 (6 - 4)     16.264     0.174    -3.156    35.684
 (6 - 5)     10.327     0.788   -10.340    30.994
 (6 - 7)     -0.094     1.000   -19.723    19.536
 (7 - 0)     37.695     0.000    18.296    57.095    #hay diferencias
 (7 - 1)      6.919     0.952   -12.072    25.911
 (7 - 2)     10.003     0.740    -8.989    28.994
 (7 - 3)     26.278     0.001     7.286    45.269    #hay diferencias
 (7 - 4)     16.358     0.157    -2.830    35.546
 (7 - 5)     10.421     0.771   -10.028    30.870
 (7 - 6)      0.094     1.000   -19.536    19.723'''

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


#Planteo hipotesis para ver si se cumple normalidad para los dos tipos de datos:
'''
-H0: los datos se distribuyen normalmente.
-H1: los datos no se distribuyen normalmente.'''

print(ss.normaltest(peso_seco_correlacion, axis=0, nan_policy='propagate'))
#NormaltestResult(statistic=10.161384799109037, pvalue=0.006215603844332242)
print(ss.normaltest(peso_nodulos_correlacion, axis=0, nan_policy='propagate'))
#NormaltestResult(statistic=32.788994682394886, pvalue=7.585081842245872e-08)

#segun ambos resultados ambos datos no se distribuyen normalmente.

#Es por eso que utilizo un test no parametrico para evaluar correlacion.


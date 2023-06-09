**Trabajo final del curso de Herramientas de Estadistica**
============================================================

***Estudiante: Constanza Rey***

### Marco teórico 
En el marco del presente curso, presento el trabajo practico final donde utilice las herramientas vistas para analizar los datos obtenidos en el marco de mi tesis doctoral. El mismo se centra en el estudio de una especie de rizobio (***Sinorhizobium meliloti***) y su par simbionte (alfalfa, ***Medicago sativa***). Se sabe que todas las cepas de ***S. meliloti*** presentan siempre al menos tres replicones grandes: un cromosoma y dos megaplasmidos tipo pSyms (pSymA y pSymB) y que el pSymA es uno de los mas variables entre cepas. Para poder determinar que genes son los que aportan la diversidad genetica a las cepas de este rizobio, nos propusimos estudiar los pSymAs de varias cepas de ***S. meliloti***.  Con ese fin, contruimos cepas hibridas de ***S. meliloti*** que comparten el mismo contexto genomico excepto cada uno de los pSymA, correspondientes a cada cepa. Las cepas hibridas generadas se nombran como: Sma(pSymA de cepa correspondiente), siendo por ejemplo la cepa hibrida con el pSymA AK21: Sma(AK21).


### Diseño y metodologia del experimento
Uno de los aspectos a evaluar para los hibridos obtenidos fue la eficiencia simbiotica. 
Con ese fin, diseñe un ensayo en alfalfa inoculando con las cepas a evaluar y utilizando 12 plantas por condicion. Cada set de plantas fue sometida a la inoculacion con una determinada cepa (excepto el control). Las cepas utilizadas fueron 2011GFP, que funciona como un control positivo, tres cepas diferentes (AK21, AK83 y B401) y los tres respectivos hibridos de cada cepa (SmaAK21, SmaAK83, SmaB401). Luego de un mes y medio, se obtiene la parte aerea de las plantas y cada una se coloca en sobres para dejarlas en estufa a 65°C durante una semana. Finalmente, se registraron los pesos obtenidos en una balanza analitica (peso seco).
Además, dado que en la camara de plantas observamos diferencias al crecer las plantas en un estante u otro, se registraron los estantes en el que colocamos cada una de las plantas. Nos aseguramos de que por estante haya al menos 12 plantas por condicion.


El dataset final consiste en una tabla con las siguientes columnas:
* Estante: Estante1, Estante2.
* Tratamiento (cepas inoculadas): control, 2011GFP, AK21, AK83, B401, Sma(AK21), Sma(AK83), Sma(B401).
* Peso seco (mg/planta): los pesos secos de cada planta registrados.


***Variable a evaluar***
   * Variable continua: peso seco de las plantas expresado en mg/planta.

## 1) ***DISTRIBUCION Y DESCRIPCION DE LOS DATOS***

Primero, evalue como se distribuyen los datos totales del peso seco. Para eso, filtre los datos de la columna peso seco y los grafique utilizando la biblioteca mathplotlib.

Los resultados obtenidos se muestran en la siguiente imagen:

<img src="./histograma_peso_seco.png" 
     width="50%" 
     height=auto />


En el histograma, se observa que los datos no se distribuirian normalmente. Aun asi, realizo mas adelante un contraste de hipotesis para evaluarlo estadisticamente.

En clase, mencionamos dos tipos de parametros que caracterizan a una distribucion: los parametros de *centralizacion* y los parametros de *dispersion*. Dentro de los parametros de centralizacion, se destacan la **media**, la **mediana** y la **moda**, los cuales los calcule en base a los pesos secos para cada una de las condiciones y para el total de datos.
Por otro lado, calcule el valor de ciertos parametros de dispersion como el **rango de valores**, **desviacion tipica** y **varianza**. Todos calculados tambien para cada condicion y total. 

Los resultados se resumieron en un unico dataframe para poder observarlos todos juntos.

```python
'''
  Tratamiento      Media  Mediana                                               Moda      RI  Desviacion tipica     Varianza
0       total  31.969663    25.65                               [[16.7, 20.4, 48.7]]  24.800          23.885983   570.540204
1     control   7.936364     8.40                           [[[4.9], [8.4], [10.1]]]   3.500           2.269581     5.150996
2         gfp  38.712500    38.40  [[[7.7], [16.9], [20.4], [21.3], [23.1], [23.3...  25.600          16.434463   270.091576
3        AK21  35.629167    33.80  [[[13.4], [16.7], [17.8], [19.3], [20.4], [22....  19.025          16.916405   286.164764
4        AK83  19.354167    19.40                                         [[[19.4]]]   7.525           6.067446    36.813895
5        B401  29.273913    25.10  [[[10.8], [12.3], [13.0], [14.7], [18.6], [18....  16.350          14.853381   220.622925
6     SmaAK21  35.211111    27.10                                         [[[16.7]]]  24.650          23.238960   540.049281
7     SmaAK83  45.538095    26.20  [[[6.3], [6.5], [12.9], [14.0], [17.2], [18.2]...  51.500          41.038220  1684.135476
8     SmaB401  45.631818    39.65  [[[4.8], [7.3], [13.7], [24.1], [32.6], [33.0]...  26.725          25.120062   631.017511
'''
```

Segun los resultados obtenidos en base a los parametros de dispersion (varianza) pareceria que el tratamiento SmaAK83 tuvo la mayor dispersion de los datos.


## 2) ***ASIMETRIA Y CURTOSIS***

Luego, analice la asimetria y curtosis de la distribucion de los datos de peso seco. Para eso, calcule el coeficiente de asimetria de Fisher y el coeficiente de curtosis.

- Coeficiente de asimetria:

```python
skewness = peso_seco.skew(axis=0, skipna=True, numeric_only=False)
```

El coeficiente de asimetria de Fisher dio un valor de 2.027382050998325. Esto indica que la distribucion de los datos presenta una **asimetria positiva**.

- Coeficiente de curtosis:

```python
kurtosis = peso_seco.kurt(axis=0, skipna=True, numeric_only=False)
```

El coeficiente de curtosis dio un valor de 7.103412786645373, lo cual indica que la distribución es **leptocurtica**.


## 3) ***ESTIMACION DE INTERVALOS DE CONFIANZA***

Para estimar los intervalos de confianza de los datos de peso seco para todas las muestras, asumi distribucion normal dado que el n>30. En este caso, calcule los intervalos de confianza definiendo ciertos parametros:
- confidence = 95% = 0.95
- loc = media 
- scale= desviacion estandar

```python
ic_95_datos_total = ss.norm.interval(confidence= 0.95, loc= media_peso_total, scale = ss.sem(peso_seco))
#(array([28.46068031]), array([35.47864554]))
```

El IC para los datos totales es [28.46, 35.47]. Esto quiere decir que: **hay un 95% de probabilidad de que el intervalo de confianza de [28.46, 35.47] contenga la media poblacional del peso seco de las plantas**.

A la hora de calcular los IC para cada uno de los tratamientos, asumi distribucion t de student dado que el n es menor a 30 y la varianza poblacional es desconocida. Aparte de los parametros definidos previamente, fue necesario agregar un parametro más:
- df = grados de libertad asociados a la distribucion t de student. Dicho valor lo calcule restando 1 a la cantidad de datos para cada tratamiento.
Los resultados se muestran a continuacion:

```python
#script de ejemplo utilizado para calcular el IC utilizando distribucion t de student:
ic_95_datos_control = ss.t.interval(confidence= 0.95, df= len(control['Peso seco'].index) -1, loc = media_control, scale = ss.sem(control['Peso seco']))

'''
El intervalo de confianza para los datos de peso seco del tratamiento control es:[ 6.930088013333918 8.942639259393355 ]
El intervalo de confianza para los datos de peso seco del tratamiento gfp es:[ 31.772834875167433 45.652165124832564 ]
El intervalo de confianza para los datos de peso seco del tratamiento AK21 es:[ 28.48599522929093 42.77233810404241 ]
El intervalo de confianza para los datos de peso seco del tratamiento AK83 es:[ 16.792109129617586 21.91622420371575 ]
El intervalo de confianza para los datos de peso seco del tratamiento B401 es:[ 22.850829472297793 35.69699661465873 ]
El intervalo de confianza para los datos de peso seco del tratamiento SmaAK21 es:[ 23.654647977328914 46.767574244893304 ]
El intervalo de confianza para los datos de peso seco del tratamiento SmaAK83 es:[ 26.857721593545204 64.21846888264527 ]
El intervalo de confianza para los datos de peso seco del tratamiento SmaB401 es:[ 34.49420667305269 56.76942969058368 ]
'''
```


## 4) ***ESTIMACION DEL TAMAÑO MUESTRAL***

El tamaño muestral se puede estimar definiendo previamente una serie de parametros:
>alpha = 0.05

>power = 0.8

>tamaño del efecto = int(abs(media_control - media_gfp) / desv_total)

>dos colas

El tamaño del efecto se define como la diferencia entre los valores promedio que espero obtener dividido la desviacion tipica total. En este caso, utilice la diferencia entre la media del peso seco del control y de la muestra inoculada con la cepa 2011 GFP, dado que entre estas dos muestras seguramente haya diferencia (la muestra gfp seria un control positivo).

De esta manera, el script final seria:
```python
n_peso = tt_ind_solve_power(effect_size=effect_size_peso, alpha=alpha, power=power, ratio=1.0, alternative='two-sided')
```

Como resultado, el minimo tamaño muestral que necesito para detectar diferencia entre grupos si es que existe seria 17 aproximadamente. En este caso, para cada condicion evaluada, cumplo con el tamaño muestral minimo requerido (en todos los casos tengo mas de 20 datos para cada tipo de muestra).


## 5) ***CONTRASTE DE HIPOTESIS***

Primero, realice test de hipotesis para verificar si se cumplen los supuestos de *normalidad* y *homocedasticidad de varianzas*.

a) Para verificar si los datos se distribuyen normalmente, realice un test de normalidad (Normal test), dado que brinda una buena
estimacion cuando se cuenta con menos de 5000 datos.
Se plantearon dos hipotesis:
- H0: los datos se distribuyen normalmente.
- H1: los datos no se distribuyen normalmente.
El script utilizado para realizar el test fue el siguiente:

```python
ss.normaltest(peso_seco, axis=0, nan_policy='propagate')
```

El resultado obtenido fue el siguiente: NormaltestResult(statistic=94.3678816604075, pvalue=3.2231080362482276e-21). El valor de p-value menor a 0.05, permite rechazar la H0 y aceptar la H1, es decir que ***los datos no se distribuyen normalmente**.

b) Para verificar similitud de varianzas, realice un test de Levene. Se plantearon dos hipotesis:
- H0: la homocedasticidad de varianzas en el peso seco de las muestras se debe al azar.
- H1: la homocedasticidad de varianzas en el peso seco de las muestras no se debe al azar.
Para realizar este test, compare los valores de peso seco obtenidos para el control y los obtenidos al inocular las plantas con la cepa 2011 GFP. 

El script utilizado fue:
```python
ss.levene(lista_control, lista_gfp, center='median', proportiontocut=0.05
```

El resultado obtenido fue el siguiente: LeveneResult(statistic=32.61406676437943, pvalue=8.962316508662243e-07). El valor de p-value menor a 0.05, permite rechazar H0 y aceptar H1, es decir que **las varianzas no son similares entre las muestras**. Dado que una de las comparaciones no cumple con la homocedasticidad de varianzas, no se cumple este supuesto.


### **Dado que los supuestos no se cumplen, debo realizar un test no parametrico para comparar los grupos.**

El objetivo es comparar los valores de peso seco obtenidos de las plantas control y aquellas inoculadas con 7 cepas de *S. meliloti*: 2011GFP, AK21, AK83, B401, Sma818R(pSymA AK21), Sma818R(pSymA AK83), Sma818R(pSymA B401). Las ultimas tres cepas mencionadas contienen un genoma compuesto por un cromosoma y pSymB similar y distinto pSymA. 

El test no parametrico utilizado para comparar los 8 grupos fue el test de Kruskal-Wallis, ya que permite comparar la mediana de mas de 3 grupos, cuando no se distribuyen de manera normal.
Las hipotesis planteadas fueron las siguientes:
-H0: las diferencias entre las muestras se deben al azar.
-H1:las diferencias entre las muestras no se deben al azar.

El script utilizado fue:

```python
ss.kruskal(control, gfp, AK21, AK83, B401, SmaAK21, SmaAK83, SmaB401, nan_policy= 'propagate', axis=0, keepdims=False)
```

El resultado obtenido fue:
>KruskalResult(statistic=array([7.58756481e-02, 1.77000000e+02, 7.25729970e+01]), pvalue=array([9.99999112e-01, 8.37571234e-35, 4.45519986e-13]))

### **Segun el p-value (4e-13) menor a 0.05, rechazo H0 y acepto H1, es decir que existen diferencias significativas entre al menos 2 muestras**

Para saber cuales son las comparaciones que presentan diferencias significativas, utilice un test no parametrico de Mann-Whitney. Con ese fin, compare de a pares en todas las combinaciones posibles los pesos secos correspondientes a los distintos tratamientos.
Planteo asi, dos hipotesis utilizadas para las comparaciones:
- H0: no hay diferencias significativas entre las muestras.
- H1: hay diferencias significativas entre las muestras.

A continuacion se muestra un ejemplo del script utilizado:

```python
control_gfp = ss.mannwhitneyu(lista_control, lista_gfp , use_continuity=True, alternative='two-sided', axis=0, method='auto', nan_policy='propagate', keepdims=False)
```

Para comparar los resultados obtenidos, genere una funcion que me filtre aquellas comparaciones cuyo pvalue sea menor a 0.05 (ya que rechazo H0 y acepto H1 de que las muestras presentan diferencias significativas) y las agregue a una lista. Con dicha lista, construi un dataframe para visualizar los datos.


```python
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
```

En la tabla, se observan cuales son las comparaciones que presentan diferencias significativas entre si. Es decir, habria diferencias significativas entre:
- Control y todas las muestras (lo cual era esperable dado que no hubo contaminacion).
- 2011GFP con AK83 y B401.
- AK21 con AK83.
- AK83 con B401, SmaAK21, SmaAK83 y SmaB401.
- B401 con SmaB401 (esto es interesante dado que parece ser que la cepa wt presenta un fenotipo simbiotico diferente a la cepa hibrida).

## Analisis de dependencia de variables categoricas.

Para comparar dos tipos de datos, construi una tabla de contingencia. Los datos a comparar fueron los siguientes:

- Variable 1: peso seco expresado en mg/planta. Fueron convertidos a datos categoricos utilizando un punto de corte (mayor a 25mg/planta: 'Alto', menor a 25mg/planta: 'Bajo'). Ese valor representa en general un peso seco alto.
- Variable 2: estante donde se ubicaron las plantas. Las opciones posibles son: 'Estante1' o 'Estante2'.

Entonces, para comprobar si existe una relacion entre la variable 1: 'Peso seco' y la variable 2: 'Estante', plantie dos hipotesis:
- H0: las variables son independientes.
- H1: las variables no son independientes, es decir, existe relacion entre las mismas.

Inicialmente como explique previamente, construi un script para convertir los datos numericos de peso seco a datos categoricos y dichos resultados los agregue a una columna extra en el dataframe llamada 'Peso seco categorico'.

Una vez convertidos los datos, arme la tabla de contingencia y agrupe los datos con la operacion 'groupby'.
El script utilizado fue el siguiente:

```python
   df2 = datos_final['Peso seco categorico'] + datos_final['Estante']
   a= datos_final['Peso seco categorico'] == 'Alto'
   b= datos_final['Estante'] == 'Estante1'
   groups = df2.groupby([a,b]).count() 
```


El resultado obtenido fue el siguiente:
```python
Peso seco categorico  Estante
False                 False      42
                      True       44
True                  False      54
                      True       38
```

Finalmente, utilice el test estadistico de chi-cuadrado para determinar asociacion entre las dos variables categoricas partiendo de la tabla de contingencia.

```python
ss.chisquare(groups, ddof=0, axis=0)
```

El resultado obtenido fue: Power_divergenceResult(statistic=3.1235955056179776, pvalue=0.3729589447466447). El p-value smayor a 0.05, indica que acepto H0, es decir que **no existe relacion entre la variable Estante y la variable Peso seco**.


## Analisis de correlacion entre dos variables.

Para realizar este punto del trabajo, utilice un dataset distinto al anterior. En este caso, la tabla cuenta con dos variables continuas a analizar:

- Peso seco de plantas expresado en mg/planta. Estos resultados fueron obtenidos para plantas inoculadas solo con la cepa 2011GFP.
- Promedio de peso fresco de nodulos por planta.

A priori, uno podria pensar que estas dos variables podrian estar correlacionadas, dado que tendria sentido que a mayor peso fresco de nodulos, mayor sea el peso seco de las plantas.

Inicialmente, realice un histograma para cada tipo de datos para observar como se distribuyen.

<img src="./Histograma_variables1y2_correlacion.png" 
     width="50%" 
     height=auto />


En la figura, se observa que los datos de peso seco podrian distribuirse normalmente, pero no seria asi para los datos promedio de los pesos fresco de los nodulos. Aun asi, realice un contraste de hipotesis para verificar si la distribucion de los datos es normal.

```python
#Planteo hipotesis para ver si se cumple normalidad para los dos tipos de datos:
'''
-H0: los datos se distribuyen normalmente.
-H1: los datos no se distribuyen normalmente.'''

print(ss.normaltest(peso_seco_correlacion, axis=0, nan_policy='propagate'))
#NormaltestResult(statistic=10.161384799109037, pvalue=0.006215603844332242)
print(ss.normaltest(peso_nodulos_correlacion, axis=0, nan_policy='propagate'))
#NormaltestResult(statistic=32.788994682394886, pvalue=7.585081842245872e-08)
```

Segun los resultados obtenidos, ninguno de los dos tipos de datos se distribuye normalmente. Por lo tanto, utilice un test no parametrico para evaluar si las dos variables continuas se correlacionan linealmente. El test utilizado fue **test de correlacion de Spearman**, el cual permite medir la relación entre dos variables, en casos donde no se cumple la distribucion normal de los datos.
A continuacion se muestra el script con el resultado obtenido.

```python
ss.spearmanr(peso_seco_correlacion, peso_nodulos_correlacion)
#SignificanceResult(statistic=0.15548804084084852, pvalue=0.4681458596212671)
```

El valor del estadistico indica el coeficiente de correlación de Spearman, el cual vale  -1 cuando existe correlacion negativa, 0 indica ausencia de correlación, y 1 indica una correlación positiva perfecta.

Segun estos resultados, ***ambos tipos de datos no estarian correlacionados***, dado que el estadistico de spearman dio un valor cercano a cero (0.155).






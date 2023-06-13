#import library.
import scipy.stats as ss
import statsmodels.stats.power as smp
import numpy as np
from statsmodels.stats.power import TTestIndPower
import pandas as pd
import matplotlib.pyplot as plt


#abri la carpeta donde tengo el dataset a analizar.


path = './Peso_seco.xlsx'
datos = pd.read_excel(path, sheet_name = 'Hoja3')
#print(datos)
datos_final = datos.dropna()
filtrado = datos_final[datos_final['Estante']== 'Estante1']
print(filtrado)
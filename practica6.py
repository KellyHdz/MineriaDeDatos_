import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
from scipy.stats import spearmanr
from scipy.stats import pearsonr
import pandas as pd

df = pd.read_csv('limpiezaCSV.csv')

df_RL1 = df.groupby("location")["total_cases"].mean().reset_index()
df_RL1['location'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
                      16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 
                      29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 
                      43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
                      57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
                      71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 
                      85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 
                      99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 
                      110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 
                      121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 
                      132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 
                      143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]

X = sm.add_constant(df_RL1['location'])
Y = df_RL1['total_cases']
model = sm.OLS(Y,X).fit()

print(model.summary())
plt.figure(figsize=(10, 6))
plt.scatter(df_RL1['location'], df_RL1['total_cases'], label='Promedios')
plt.plot(df_RL1['location'], model.predict(X), color='red', label='Recta')
plt.xlabel('Ciudades {}'.format)#(fecha_final.date()))
plt.ylabel('Promedio total de casos')
plt.title('Regresion lineal:promedio de total de casos por ciudad')
plt.legend()

plt.savefig('RL_CasosPorCiudad.png')
plt.tight_layout()
plt.close()
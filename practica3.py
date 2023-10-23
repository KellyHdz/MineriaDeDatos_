import pandas as pd
from tabulate import tabulate
from typing import Tuple, List

import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = "limpiezaCSV.csv"
df = pd.read_csv(data)

df_total = df.groupby(["location"]).agg({'total_cases': ['sum', 'count', 'mean', 'min', 'max']})
df_total = df_total.reset_index()
newCSVFile = "totalCasosPorCiudad.csv"
df_total.to_csv(newCSVFile, index=False)


df_total = df.groupby(["location"]).agg({'total_deaths': ['sum', 'count', 'mean', 'min', 'max']})
df_total = df_total.reset_index()
newCSVFile = "totalCasosPorCiudad_Muertos.csv"
df_total.to_csv(newCSVFile, index=False)


df_total = df.groupby(["location"]).agg({'total_cases': ['sum', 'count', 'mean', 'min', 'max']})
df_total = df_total.reset_index()
newCSVFile = "totalCasosPorCiudad_poblacional.csv"
df_total.to_csv(newCSVFile, index=False)


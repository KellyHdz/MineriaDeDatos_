import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols


df = pd.read_csv("limpiezaCSV.csv")
df_B1 = df.groupby(["location", "date"])[["total_cases"]].mean()
df_B1.boxplot(by = 'location', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("B_Casos.png")
plt.close()

df = pd.read_csv("limpiezaCSV.csv")
df_B1 = df.groupby(["location", "date"])[["total_deaths"]].mean()
df_B1.boxplot(by = 'location', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("B_Muertes.png")
plt.close()

df = pd.read_csv("limpiezaCSV.csv")
df_B1 = df.groupby(["location", "date"])[["population"]].mean()
df_B1.boxplot(by = 'location', figsize=(27,18))
plt.xticks(rotation=90)
plt.savefig("B_Pob.png")
plt.close()

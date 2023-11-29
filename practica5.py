import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

df = pd.read_csv("limpiezaCSV.csv")

df_RL1 = df.groupby(["location", "iso_code"])[["total_cases"]].sum()
df_RL1.reset_index(inplace=True)
df_RL1.set_index("location", inplace=True)
df_RL1.reset_index(inplace=True)
df_Anova = df_RL1.rename(columns={"total_cases" : "totalCasos"}).drop(['iso_code'], axis=1)
print(df_Anova.head())

model = ols("totalCasos ~ location", data=df_Anova).fit()
anova = sm.stats.anova_lm(model, typ=1)
print(anova)
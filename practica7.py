import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List
import numpy as np

df = pd.read_csv('limpiezaCSV.csv')

def create_cases_group(df):
    casos_groups = []
    for casos in df['total_cases']:
        if casos >= 0 and casos <= 10000:
            casos_group = '0-10000'
        elif casos > 10000 and casos <= 50000:
            casos_group = '10001-50000'
        elif casos > 50000 and casos <= 100000:
            casos_group = '50001-100000'
        else:
            casos_group = '100001'
        casos_groups.append(casos_group)
    df['casos_group'] = casos_groups

create_cases_group(df)

df['location'] = df['location'].astype(str)

colors = {'0-10000':'red', '10001-50000':'green', '50001-100000':'blue', '100001':'purple'}

def scatter_casos_groups(df, x_column, y_column, label_column, k_neighbors):
    fig, ax = plt.subplots()
    labels = df[label_column].unique()
    
    for label in labels:
        filter_df = df[df[label_column] == label]
        ax.scatter(filter_df[x_column],filter_df[y_column], label=label, color=colors[label])
    
    ax.legend()
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('Scatter Grupos de Casos')
    plt.savefig('Scat_GCasos.png')
    plt.close()

scatter_casos_groups(df, 'total_cases', 'location', 'casos_group', k_neighbors=5)


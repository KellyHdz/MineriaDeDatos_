import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime


data = pd.read_csv("CSV.csv")
new_data = data

new_data.dropna(inplace=True)
new_data.to_csv("limpiezaCSV.csv",index=False)

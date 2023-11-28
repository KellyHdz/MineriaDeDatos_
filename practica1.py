import pandas as pd
import requests
import io

def get_csv_from_url(url: str) -> pd.DataFrame:
    r = requests.get(url).content
    return pd.read_csv(io.StringIO(r.decode('utf-8')))

df = get_csv_from_url("https://raw.githubusercontent.com/KellyHdz/csv_MineriaDeDatos/main/CSV.csv?token=GHSAT0AAAAAACK3WDB7U5Y5KU46DM5BOWK2ZLFH3NQ")
df.to_csv("CSV.csv", index=False)

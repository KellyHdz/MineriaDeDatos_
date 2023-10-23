import pandas as pd
import requests
import io

def get_csv_from_url(url: str) -> pd.DataFrame:
    r = requests.get(url).content
    return pd.read_csv(io.StringIO(r.decode('utf-8')))

df = get_csv_from_url("https://raw.githubusercontent.com/KellyHdz/csv_MineriaDeDatos/main/csv.csv?token=GHSAT0AAAAAACHJWA33K5S7366GQXKZJHTEZJVXZ5Q")
df.to_csv("CSV.csv", index=False)

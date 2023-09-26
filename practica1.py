import pandas as pd
import requests
import io

def get_csv_from_url(url: str) -> pd.DataFrame:
    r = requests.get(url).content
    return pd.read_csv(io.StringIO(r.decode('utf-8')))

df = get_csv_from_url("https://raw.githubusercontent.com/KellyHdz/csv_MineriaDeDatos/main/DatosCovid.csv?token=GHSAT0AAAAAACHJWA33R6HOJFKETYEFHGT2ZITNVBA")
df.to_csv("DatosCovid.csv", index=False)

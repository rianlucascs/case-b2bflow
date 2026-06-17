import pandas as pd
from db import engine

df = pd.read_sql('SELECT * FROM "Leads" LIMIT 5', engine)
print(df)
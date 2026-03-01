import pandas as pd
df=pd.read_csv("cric.csv")
print(df.dropna(subset=["PlayerID","Wickets"]))

import pandas as pd
df = pd.read_csv("C:/mt/dataset/Avocado.csv")
df = df.copy()[df["type"]=="organic"]
df["Date"] = pd.to_datetime(df["Date"])


df.sort_values(by= "Date", ascending=True, inplace=True)
df["Date"] = pd.to_datetime(df["Date"])
alb_df = df[ df["region"]== "Albany"]
alb_df = alb_df.set_index("Date")
alb_df.sort_index(inplace =True)
print(df.head())

# Identify and remove duplicated values
import pandas as pd

df = pd.read_excel("Base_Vendas.xlsx")
print(f"\n{df}\n")

# 1° - sum up unique values, nunique - this counts how many
# unique values we have into a specified field.
df_nunique = df.nunique()
print(f"\n{df_nunique}\n")

# 2° - summarize which is an unique value and what it's not.
# using the method .duplicated(subset="Salesperson", keep="first")
# keep control how we can consider the duplicated value =  first, last, False
df_duplicated = df.duplicated(subset="Vendedor", keep="first")
print(f"\n{df_duplicated}\n")

# 3° - Create a new column to identify what's duplicated value
df["Duplicated Values"] = df.duplicated(subset="Vendedor", keep="first")
print(f"\n{df}\n")

# 4° - Remove duplicate values
df_cleaned = df.drop(columns="Duplicated Values").drop_duplicates(subset="Vendedor", keep="first")
print(f"\nData frame cleaned: \n{df_cleaned}\n")
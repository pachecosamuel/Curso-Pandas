import pandas as pd

df = pd.read_excel("Tratamento_Dados.xlsx")
print(f"\n {df} \n")

# 1° We gonna populate the cells with NaN with the average 
# of the presents fields
df_average = df["Total Vendas"].fillna(df["Total Vendas"].mean())
print(f"\n Fillna average: \n{df_average} \n")

df["Total Vendas"] = df_average
print(f"\n IT'S A TEST {df} \n")

df_default_value = df["Total Vendas"].fillna(1000)
print(f"\n Fillna default value: \n{df_default_value} \n")

# 2° Using the ffill method which fill with the last value
# the columns NaN
df_ffill = df["Total Vendas"].ffill()
print(f"\n FFill last valid value: \n{df_ffill} \n")


# 3° value_count - resume the sales made of each salesperson
df_amount_sales = df["Vendedor"].value_counts()
print(f"\n Value counts: \n{df_amount_sales} \n")

# 4° groupby - Group the informations
df_total_sales = df.groupby("Vendedor")
print(f"\n Group by and sum: \n{df_total_sales} \n")
